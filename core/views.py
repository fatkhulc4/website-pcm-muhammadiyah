
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
    leaders = Leader.objects.all()

    return render(
        request,
        "core/pimpinan.html",
        {"leaders": leaders},
    )


def ranting(request):
    ranting_list = Ranting.objects.all()

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
