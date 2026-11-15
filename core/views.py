from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone

from .models import (
    OrganizationProfile,
    Leader,
    Ranting,
    AmalUsaha,
    News,
    Event,
)


def home(request):
    profile = OrganizationProfile.objects.first()

    news_list = News.published.all()[:3]

    event_list = Event.objects.filter(
        start_date__gte=timezone.now()
    ).order_by("start_date")[:3]

    context = {
        "profile": profile,
        "news_list": news_list,
        "event_list": event_list,
    }

    return render(request, "core/home.html", context)


def berita(request):
    news_queryset = News.published.all()

    paginator = Paginator(news_queryset, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "core/berita.html",
        {"page_obj": page_obj},
    )


def detail_berita(request, slug):
    news = get_object_or_404(
        News.published.all(),
        slug=slug,
    )

    return render(
        request,
        "core/detail_berita.html",
        {"news": news},
    )


def profil(request):
    profile = OrganizationProfile.objects.first()

    return render(
        request,
        "core/profil.html",
        {"profile": profile},
    )


def pimpinan(request):
    penasehat = [
        "Drs. H. Sutarno, MM",
        "Ir. H. Suroto",
    ]

    pleno = [
        {"jabatan": "Ketua", "nama": "H. Siyamto Umardani, S. Ag", "koordinator": []},
        {"jabatan": "Wakil Ketua I", "nama": "Giyamto, S. Pd", "koordinator": [
            "Majelis Pemberdayaan Masyarakat",
            "Lazizmu",
        ]},
        {"jabatan": "Wakil Ketua II", "nama": "H. Sumarno, S. Th. I", "koordinator": [
            "Lembaga Pembinaan Haji dan Umroh",
            "Lembaga Pembinaan dan Pengawasan Keuangan",
        ]},
        {"jabatan": "Wakil Ketua III", "nama": "Parlan Sinung Darsono", "koordinator": [
            "Majelis Pembinaan Kader – Sumber Daya Insani",
            "Lembaga Sosial Budaya dan Olah Raga",
            "Pembinaan Angkatan Muda Muhammadiyah dan Ortom",
        ]},
        {"jabatan": "Wakil Ketua IV", "nama": "H. Suyatno, S. Sos, M. Si", "koordinator": [
            "Majelis Pemberdayaan Wakaf",
            "Majelis Lingkungan Hidup",
        ]},
        {"jabatan": "Wakil Ketua V", "nama": "Muhammad Marjuki, S. Pd", "koordinator": [
            "Majelis Tarjih, Tajdid, dan Tabligh",
            "Lembaga Pengembangan Cabang Ranting dan Pembinaan Masjid",
        ]},
        {"jabatan": "Wakil Ketua VI", "nama": "Dr. H. Basuki Agus Suparno, MSI", "koordinator": [
            "Majelis Pustaka dan Informasi",
            "Majelis Hukum, HAM, dan Lembaga Bantuan Hukum",
        ]},
        {"jabatan": "Wakil Ketua VII", "nama": "Dr. Purwadi, M. Pd", "koordinator": [
            "Majelis Dikdasmen",
            "Lembaga Pengembangan Pesantren Muhammadiyah",
        ]},
        {"jabatan": "Wakil Ketua VIII", "nama": "Dr. H. Suharno, ST. MT", "koordinator": [
            "Majelis Ekonomi dan Kewirausahaan",
            "Lembaga Hikmah dan Kebijakan Publik",
        ]},
        {"jabatan": "Sekretaris", "nama": "Muhammad Effendi, S. Psi", "koordinator": []},
        {"jabatan": "Wakil Sekretaris", "nama": "Drs. H. Taslim Daryanto, M. Pd", "koordinator": [
            "MPKU dan Pelayanan Sosial",
        ]},
        {"jabatan": "Bendahara", "nama": "Dwi Daryanto, S. Pd. I", "koordinator": []},
        {"jabatan": "Wakil Bendahara", "nama": "Muslih, S. Pd", "koordinator": [
            "Lembaga Resiliensi Bencana",
        ]},
    ]

    return render(
        request,
        "core/pimpinan.html",
        {"penasehat": penasehat, "pleno": pleno},
    )


def ranting(request):
    ranting_list = [
        "Masaran", "Krikilan", "Gebang", "Pringanom", "Sepat",
        "Krebet", "Jirapan", "Dawungan", "Karangmalang", "Sidodadi",
        "Kliwonan", "Pilang", "Jati",
    ]

    return render(
        request,
        "core/ranting.html",
        {"ranting_list": ranting_list},
    )


def amal_usaha(request):
    amal_list = AmalUsaha.objects.all()

    return render(
        request,
        "core/amal_usaha.html",
        {"amal_list": amal_list},
    )


def kegiatan(request):
    event_list = Event.objects.order_by("start_date")

    return render(
        request,
        "core/kegiatan.html",
        {"event_list": event_list},
    )


def kontak(request):
    return render(request, "core/kontak.html")