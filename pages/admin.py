import logging
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pages.forms import CMSPageForm
from pages.models import CMSPage, SponsorsCarousel
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


# Register your models here.

class CMSPageAdmin(admin.ModelAdmin):
    form = CMSPageForm


class SponsorsCarouselAdmin(OrderedModelAdmin):
    list_display = ('change', 'image', 'description', 'move_up_down_links')

    def change(self, obj):
        return _('Change')
    change.short_description = _('Change')


admin.site.register(CMSPage, CMSPageAdmin)
admin.site.register(SponsorsCarousel, SponsorsCarouselAdmin)
