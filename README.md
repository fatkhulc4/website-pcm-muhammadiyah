# Website PCM Masaran

Proyek ini dibuat sebagai tugas mata kuliah Pemrograman Web berbasis Framework dan **bukan website resmi** Pimpinan Cabang Muhammadiyah (PCM) Masaran.

## Kelompok

| No |        Nama       |    NIM     |
|----|-------------------|------------|
| 1  | Nova Ayu Damayanti| L200240005 |
| 2  | Fatkhul Choiri    | L200240049 |
| 3  | Vera Jeni Vertika | L200240061 |
| 4  | Thoriq Fahma Amin | L200240063 |

## PCM yang Dipilih

- **Nama:** PCM Masaran
- **Wilayah:** Kecamatan Masaran, Kabupaten Sragen, Jawa Tengah
- **Tujuan website:** Website ini dibuat untuk memperkenalkan PCM Masaran kepada masyarakat sekaligus menjadi sarana publikasi berita, agenda, dan dokumen, serta menerima pesan dari masyarakat melalui formulir kontak. Seluruh isinya dapat dikelola pengurus lewat panel admin tanpa mengubah kode.

### Sumber Data

|        Data       |       Sumber      | Tanggal diambil | Pemberi izin |
|-------------------|-------------------|-----------------|--------------|
| Logo Muhammadiyah | Wikimedia Commons | 30 Oktober 2026 |       -      |
| Profil, struktur pimpinan, ranting, amal usaha | Pengurus PCM Masaran | 30 Oktober 2026 | Bapak Jumadi (Ketua Pustaka Informasi ) |
| Berita dan agenda | Pengurus PCM Masaran | 30 Oktober 2026 | Bapak Jumadi (Ketua Pustaka Informasi ) |
| Foto | Pengurus PCM Masaran | 30 Oktober 2026 | Bapak Jumadi (Ketua Pustaka Informasi ) |

## Produksi

| Item | Pilihan | Alasan |
|------|---------|--------|
| URL produksi | https://website-pcm-muhammadiyah-production.up.railway.app/ | Harus tetap menyala sampai penilaian selesai |
| Platform | Render (Web Service memakai `Dockerfile`, paket gratis) <!-- perbarui setelah deploy --> | Memakai `Dockerfile` yang sama dengan Docker lokal, HTTPS disediakan otomatis, dan paket gratis cukup untuk penilaian |
| Database | PostgreSQL di Supabase (Session pooler, port 5432) | Database terkelola dan gratis. Session pooler mendukung IPv4 dan cocok dengan koneksi Django biasa. Row Level Security aktif di semua tabel |
| Penyimpanan gambar | Supabase Storage lewat endpoint S3 dan `django-storages` (bucket publik `media`) | Disk server platform deploy tidak permanen, sehingga gambar upload akan hilang setelah redeploy jika disimpan lokal. Sudah diuji: gambar yang diunggah dari admin tersimpan di bucket |

## Catatan layanan gratis

- **Railway:** Menggunakan kredit uji coba (*trial credit* dengan batas saldo/waktu tertentu). Layanan web akan berhenti berjalan otomatis jika masa uji coba atau saldo kredit habis. Sisa kredit dapat dipantau melalui dashboard Railway.
- **Supabase:** Proyek pada paket gratis akan dijeda (*paused*) otomatis apabila tidak ada aktivitas database selama 7 hari berturut-turut, dan dapat diaktifkan kembali melalui tombol **Resume project** di dashboard. Informasi lengkap dapat dilihat pada [dokumentasi Supabase](https://supabase.com/docs/guides/platform/free-plan-pausing).

## Cara Menjalankan

### Dengan uv (di laptop)

Prasyarat: Python 3.14 atau lebih baru dan [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/fatkhulc4/website-pcm-muhammadiyah.git
cp .env.example .env      # lalu isi nilainya, minimal SECRET_KEY
uv sync
uv run python manage.py migrate
uv run python manage.py seed_pcm
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Buka `http://localhost:8000`. Panel admin ada di `http://localhost:8000/admin/`.

Jika `DATABASE_URL` dan `STORAGE_BUCKET` dikosongkan, proyek memakai SQLite dan folder `media/` lokal.

### Dengan Docker

Docker telah dikonfigurasi menggunakan Dockerfile dan compose.yaml untuk menjalankan aplikasi Django dan PostgreSQL dalam container.

Prasyarat: Docker Desktop sudah terpasang dan berjalan.

```bash
cp .env.example .env      # lalu isi nilainya
docker compose up --build
```

Buka `http://localhost:8000`.

Panel admin tersedia di `http://localhost:8000/admin/`.

Untuk mengisi data awal PCM Masaran:

```bash
docker compose exec web uv run --no-sync python manage.py seed_pcm
```

Untuk membuat akun administrator:

```bash
docker compose exec web uv run --no-sync python manage.py createsuperuser
```

Untuk menghentikan container:

```bash
docker compose down
```

Untuk menghentikan container sekaligus menghapus volume database dan media:

```bash
docker compose down -v
```

## Environment Variable

| Variabel | Fungsi |
|----------|--------|
| `SECRET_KEY` | Kunci rahasia Django. Wajib diisi |
| `DEBUG` | Mode debug. Bawaannya `False` |
| `ALLOWED_HOSTS` | Daftar host yang diizinkan, dipisah koma |
| `CSRF_TRUSTED_ORIGINS` | Daftar origin tepercaya untuk CSRF, dipisah koma |
| `HTTPS_ONLY` | `True` hanya di server HTTPS. Mengaktifkan redirect SSL, cookie aman, dan HSTS |
| `HSTS_SECONDS` | Durasi HSTS dalam detik. Mulai dari 3600, naikkan setelah HTTPS terbukti stabil |
| `DATABASE_URL` | URL PostgreSQL. Kosong berarti SQLite lokal |
| `POSTGRES_PASSWORD` | Password database PostgreSQL untuk Docker Compose. Wajib diisi di `.env` saat memakai `docker compose` |
| `STORAGE_BUCKET` | Nama bucket. Kosong berarti media disimpan di folder lokal |
| `STORAGE_ENDPOINT` | Endpoint S3 dari Supabase Storage |
| `STORAGE_REGION` | Region bucket |
| `STORAGE_ACCESS_KEY` | Access key S3 |
| `STORAGE_SECRET_KEY` | Secret key S3 |
| `STORAGE_PUBLIC_DOMAIN` | Domain publik bucket tanpa `https://`, dipakai untuk membentuk URL gambar |

Semua variabel `STORAGE_*` selain `STORAGE_BUCKET` wajib terisi jika `STORAGE_BUCKET` dipakai. Aplikasi akan berhenti dengan pesan error jika ada yang kosong.


