from django.contrib import admin
from .models import (
    OrganizationProfile,
    Leader,
    Ranting,
    AmalUsaha,
    News,
    Event,
    Document,
    IncomingMessage,
    RelatedLink,
)


admin.site.site_header = "Admin Website PCM Masaran"
admin.site.site_title = "Admin PCM Masaran"
admin.site.index_title = "Kelola Konten Website PCM Masaran"


@admin.register(OrganizationProfile)
class OrganizationProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "period")
    search_fields = ("name", "position")
    list_filter = ("period",)


@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "address")


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "phone")
    search_fields = ("name", "address")
    list_filter = ("category",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "published_at")
    search_fields = ("title", "content")
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_date")
    search_fields = ("title", "location")
    list_filter = ("start_date",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")
    search_fields = ("title",)


@admin.register(IncomingMessage)
class IncomingMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("is_read", "created_at")
    readonly_fields = ("name", "email", "subject", "message", "created_at")


@admin.register(RelatedLink)
class RelatedLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "is_active")
    search_fields = ("title",)
    list_filter = ("is_active",)