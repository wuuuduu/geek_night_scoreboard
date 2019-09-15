from pages.models import SponsorsCarousel


def sponsors_carousel_processor(request):
    return {
        'sponsors': SponsorsCarousel.objects.filter(visible=True)
    }
