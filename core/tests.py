from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import (
    AmalUsaha,
    Event,
    IncomingMessage,
    News,
    OrganizationProfile,
    RelatedLink,
)


def buat_berita(title, status="published", hari=-1):
    """Pembantu: buat berita. hari<0 = masa lalu, hari>0 = masa depan."""
    return News.objects.create(
        title=title,
        content="Isi berita.",
        status=status,
        published_at=timezone.now() + timedelta(days=hari),
    )


class HalamanPublikTest(TestCase):
    """Semua halaman publik harus menjawab 200."""

    def test_semua_halaman_publik_200(self):
        nama_url = [
            "core:home", "core:profil", "core:pimpinan", "core:ranting",
            "core:amal_usaha", "core:berita", "core:agenda",
            "core:unduhan", "core:kontak",
        ]
        for nama in nama_url:
            with self.subTest(url=nama):
                response = self.client.get(reverse(nama))
                self.assertEqual(response.status_code, 200)

    def test_halaman_tidak_ada_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")
        self.assertEqual(response.status_code, 404)


class BeritaTest(TestCase):
    def test_berita_draf_404(self):
        berita = buat_berita("Masih Draf", status="draft")
        response = self.client.get(
            reverse("core:detail_berita", args=[berita.slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_berita_masa_depan_404(self):
        berita = buat_berita("Belum Waktunya", hari=5)
        response = self.client.get(
            reverse("core:detail_berita", args=[berita.slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_berita_terbit_bisa_dibuka(self):
        berita = buat_berita("Sudah Terbit")
        response = self.client.get(
            reverse("core:detail_berita", args=[berita.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sudah Terbit")

    def test_slug_dibuat_otomatis_dan_unik(self):
        a = buat_berita("Judul Sama")
        b = buat_berita("Judul Sama")
        self.assertEqual(a.slug, "judul-sama")
        self.assertEqual(b.slug, "judul-sama-1")

    def test_manager_published_hanya_berita_terbit(self):
        buat_berita("Terbit")
        buat_berita("Draf", status="draft")
        buat_berita("Masa Depan", hari=3)
        self.assertEqual(News.published.count(), 1)

    def test_paginasi_6_per_halaman(self):
        for i in range(7):
            buat_berita(f"Berita {i}")
        halaman1 = self.client.get(reverse("core:berita"))
        halaman2 = self.client.get(reverse("core:berita") + "?page=2")
        self.assertEqual(len(halaman1.context["page_obj"]), 6)
        self.assertEqual(len(halaman2.context["page_obj"]), 1)


class AgendaTest(TestCase):
    def test_agenda_dipisah_akan_datang_dan_lampau(self):
        Event.objects.create(
            title="Kajian Depan", description="x",
            start_date=timezone.now() + timedelta(days=3),
        )
        Event.objects.create(
            title="Kajian Lalu", description="x",
            start_date=timezone.now() - timedelta(days=3),
        )
        response = self.client.get(reverse("core:agenda"))
        self.assertEqual(
            [e.title for e in response.context["upcoming"]], ["Kajian Depan"]
        )
        self.assertEqual(
            [e.title for e in response.context["past"]], ["Kajian Lalu"]
        )


class KontakTest(TestCase):
    data_valid = {
        "name": "Budi",
        "email": "budi@example.com",
        "subject": "Tanya kegiatan",
        "message": "Kapan pengajian rutin diadakan?",
    }

    def test_formulir_valid_tersimpan_dan_ada_pesan_sukses(self):
        response = self.client.post(
            reverse("core:kontak"), self.data_valid, follow=True
        )
        self.assertEqual(IncomingMessage.objects.count(), 1)
        self.assertContains(response, "berhasil dikirim")

    def test_formulir_tidak_valid_tidak_tersimpan(self):
        data = {**self.data_valid, "email": "bukan-email"}
        response = self.client.post(reverse("core:kontak"), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(IncomingMessage.objects.count(), 0)

    def test_pesan_terlalu_pendek_ditolak(self):
        data = {**self.data_valid, "message": "pendek"}
        self.client.post(reverse("core:kontak"), data)
        self.assertEqual(IncomingMessage.objects.count(), 0)


class ContextProcessorTest(TestCase):
    def test_profil_dan_tautan_ada_di_semua_halaman(self):
        OrganizationProfile.objects.create(name="PCM Uji")
        RelatedLink.objects.create(title="PP Muhammadiyah", url="https://muhammadiyah.or.id")
        response = self.client.get(reverse("core:profil"))
        self.assertEqual(response.context["site_profile"].name, "PCM Uji")
        self.assertEqual(len(response.context["related_links"]), 1)


class AdminTest(TestCase):
    def test_profil_hanya_boleh_satu(self):
        from django.contrib.auth import get_user_model
        user = get_user_model().objects.create_superuser("admin", "a@a.com", "pw12345!")
        self.client.force_login(user)
        url = reverse("admin:core_organizationprofile_add")
        self.assertEqual(self.client.get(url).status_code, 200)
        OrganizationProfile.objects.create(name="PCM Uji")
        self.assertEqual(self.client.get(url).status_code, 403)
