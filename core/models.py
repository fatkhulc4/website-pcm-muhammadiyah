from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class OrganizationProfile(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    logo = models.ImageField(
        upload_to="organization/",
        blank=True
    )
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

    def __str__(self):
        return self.name


class Ranting(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


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


class News(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270, unique=True, blank=True)
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


class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class IncomingMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class RelatedLink(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    description = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title