
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),

    # Berita
    path("berita/", views.berita, name="berita"),
    path(
        "berita/<slug:slug>/",
        views.detail_berita,
        name="detail_berita",
    ),

    # Informasi organisasi
    path("profil/", views.profil, name="profil"),
    path("pimpinan/", views.pimpinan, name="pimpinan"),
    path("ranting/", views.ranting, name="ranting"),
    path("amal-usaha/", views.amal_usaha, name="amal_usaha"),
    path("agenda/", views.agenda, name="agenda"),    
    path("unduhan/", views.unduhan, name="unduhan"),
    path("kontak/", views.kontak, name="kontak"),
]