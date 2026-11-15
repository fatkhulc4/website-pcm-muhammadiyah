from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class OrganizationProfile(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50, blank=True)
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    history = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True, help_text="Satu misi per baris")
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    member_count = models.PositiveIntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to="organization/", blank=True)
    hero_image = models.ImageField(upload_to="organization/", blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profil Organisasi"
        verbose_name_plural = "Profil Organisasi"
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Profil Organisasi"
        verbose_name_plural = "Profil Organisasi"


class Leader(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    period = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to="leaders/", blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Urutan tampil (kecil tampil lebih dulu)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pimpinan"
        verbose_name_plural = "Pimpinan"
        ordering = ["order", "id"]
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pimpinan"
        verbose_name_plural = "Pimpinan"


class Ranting(models.Model):
    name = models.CharField(max_length=150)
    chairman = models.CharField("Ketua", max_length=150, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ranting"
        verbose_name_plural = "Ranting"


class AmalUsaha(models.Model):
    CATEGORY_CHOICES = [
        ("pendidikan", "Pendidikan"),
        ("kesehatan", "Kesehatan"),
        ("sosial", "Sosial"),
        ("ekonomi", "Ekonomi"),
        ("lainnya", "Lainnya"),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="lainnya"
    )
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="amal_usaha/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Amal Usaha"
        verbose_name_plural = "Amal Usaha"


class News(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270, unique=True, blank=True)
    summary = models.TextField(blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to="news/", blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "berita"
            candidate = base
            number = 1

            while News.objects.filter(slug=candidate).exclude(
                pk=self.pk
            ).exists():
                candidate = f"{base}-{number}"
                number += 1

            self.slug = candidate

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Berita"
        verbose_name_plural = "Berita"
        ordering = ["-created_at"]


class PublishedNewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            status="published",
            published_at__lte=timezone.now()
        )


News.add_to_class("published", PublishedNewsManager())


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to="events/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kegiatan"
        verbose_name_plural = "Kegiatan"


class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dokumen"
        verbose_name_plural = "Dokumen"


class IncomingMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Pesan Masuk"
        verbose_name_plural = "Pesan Masuk"


class RelatedLink(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    description = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tautan Terkait"
        verbose_name_plural = "Tautan Terkait"
        ordering = ["order", "id"]