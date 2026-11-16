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
