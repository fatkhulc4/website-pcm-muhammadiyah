from .models import OrganizationProfile, RelatedLink


def site_context(request):
    """Data yang tersedia di SEMUA template (header dan footer)."""
    return {
        "site_profile": OrganizationProfile.objects.first(),
        "related_links": RelatedLink.objects.filter(is_active=True),
    }