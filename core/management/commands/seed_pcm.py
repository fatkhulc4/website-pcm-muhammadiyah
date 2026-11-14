"""Mengisi database kosong dengan data riil PCM.

Pemakaian:
    python manage.py seed_pcm            # laptop
    docker compose exec web python manage.py seed_pcm
Aman dijalankan berulang kali (idempotent): data yang sama tidak diduplikasi.
"""
from datetime import datetime
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from core import models as m
from core.seed_data import DATA

IMAGE_DIR = Path(__file__).resolve().parents[2] / "seed_images"


def to_dt(value):
    """'2026-10-01T09:00' -> datetime aware; kosong -> None."""
    if not value:
        return None
    return timezone.make_aware(datetime.fromisoformat(value))


def attach(obj, field, filename, stdout):
    """Lampirkan gambar dari core/seed_images/ bila belum ada. Aman diulang."""
    if not filename or getattr(obj, field):
        return
    path = IMAGE_DIR / filename
    if not path.exists():
        stdout.write(f"  ! gambar tidak ditemukan: {filename}")
        return
    with path.open("rb") as f:
        getattr(obj, field).save(filename, File(f), save=True)


class Command(BaseCommand):
    help = "Isi database dengan data riil PCM dari core/seed_data.py"

    @transaction.atomic
    def handle(self, *args, **options):
        p = DATA["profil"]
        if p["name"].startswith("ISI_"):
            raise CommandError(
                "core/seed_data.py belum diisi. Isi data riil PCM dulu "
                "(jangan seed data contoh/karangan)."
            )

        # Profil: hanya satu baris. Field yang belum ada di model dilewati
        # (otomatis terisi setelah field-nya ditambahkan ke models.py).
        profil = m.OrganizationProfile.objects.first() or m.OrganizationProfile()
        for k, v in p.items():
            if k == "logo" or not hasattr(profil, k):
                continue
            if isinstance(v, list):          # misi: satu misi per baris
                v = "\n".join(v)
            setattr(profil, k, v)
        profil.save()
        attach(profil, "logo", p["logo"], self.stdout)

        for d in DATA["pimpinan"]:
            o, _ = m.Leader.objects.update_or_create(
                name=d["name"], position=d["position"],
                defaults={"period": d.get("period", ""),
                          "description": d.get("description", "")})
            attach(o, "photo", d.get("photo"), self.stdout)

        for d in DATA["ranting"]:
            m.Ranting.objects.update_or_create(
                name=d["name"],
                defaults={"address": d.get("address", ""),
                          "description": d.get("description", "")})

        for d in DATA["amal_usaha"]:
            o, _ = m.AmalUsaha.objects.update_or_create(
                name=d["name"],
                defaults={"category": d.get("category", "lainnya"),
                          "address": d.get("address", ""),
                          "phone": d.get("phone", ""),
                          "description": d.get("description", "")})
            attach(o, "photo", d.get("photo"), self.stdout)

        for d in DATA["berita"]:
            o, _ = m.News.objects.update_or_create(
                title=d["title"],
                defaults={"content": d["content"], "status": "published",
                          "published_at": to_dt(d["published_at"])})
            attach(o, "image", d.get("image"), self.stdout)

        for d in DATA["kegiatan"]:
            o, _ = m.Event.objects.update_or_create(
                title=d["title"], start_date=to_dt(d["start_date"]),
                defaults={"description": d.get("description", ""),
                          "location": d.get("location", ""),
                          "end_date": to_dt(d.get("end_date"))})
            attach(o, "image", d.get("image"), self.stdout)

        for d in DATA["tautan"]:
            m.RelatedLink.objects.update_or_create(
                title=d["title"],
                defaults={"url": d["url"], "description": d.get("description", ""),
                          "is_active": True})

        self.stdout.write(self.style.SUCCESS("seed_pcm selesai."))
