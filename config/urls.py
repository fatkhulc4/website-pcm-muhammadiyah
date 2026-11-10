from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    # Menyajikan media dari disk (laptop & Docker). Di produksi (Vercel/Render)
    # media harus di object storage, sehingga baris ini tidak dipakai.
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT},
    ),
]
