FROM python:3.14-slim

# uv dari image resmi
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# 1) Dependensi dulu (layer ini di-cache selama uv.lock tidak berubah)
COPY pyproject.toml uv.lock .python-version README.md ./
RUN uv sync --locked --no-install-project --no-dev

# 2) Kode aplikasi
COPY . .
RUN uv sync --locked --no-dev

# 3) File statis (nilai dummy hanya untuk proses build, tidak disimpan)
RUN SECRET_KEY=build-only DEBUG=False python manage.py collectstatic --noinput

# 4) User non-root + folder media yang bisa ditulis
RUN useradd --create-home --uid 1000 app \
    && mkdir -p /app/media \
    && chown -R app:app /app/media /app/staticfiles
USER app

EXPOSE 8000
CMD ["sh", "-c", "gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2"]
