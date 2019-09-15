from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from ordered_model.admin import OrderedModelAdmin

from agenda.forms import LectureForm
from agenda.models import RoomModel, LectureModel
from django.utils.translation import gettext_lazy as _


class RoomAdmin(OrderedModelAdmin):
    list_display = ('name', 'lectures', 'move_up_down_links')

    def lectures(self, obj: RoomModel):
        html = '<a href="{url}?{params}" target="_BLANK">{text}</a> '.format(
            url=reverse(
                'admin:%s_%s_changelist' % (LectureModel._meta.app_label, LectureModel._meta.model_name)),
            text=_('Lectures'),
            params="room__id__exact={pk}".format(pk=obj.pk)

        )

        return mark_safe(html)


class LectureAdmin(OrderedModelAdmin):
    form = LectureForm
    list_display = ('change', 'author', 'room', 'start_date', 'end_date', 'move_up_down_links')
    list_filter = ('room',)

    def change(self, obj: LectureModel):
        return _('Change')

    change.admin_order_field = 'pk'
    change.short_description = _('Change')


admin.site.register(RoomModel, RoomAdmin)
admin.site.register(LectureModel, LectureAdmin)
