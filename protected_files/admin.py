from django.contrib import admin
from django.utils.text import format_lazy
from django.utils.timezone import now

from protected_files.models import ProtectedFiles, PublicFiles
from django.utils.translation import gettext_lazy as _


class ProtectedFilesAdmin(admin.ModelAdmin):
    readonly_fields = ('content_type', 'added_by', 'modify_by', 'date_added', 'date_modify')
    list_display = ('edit', 'file', 'content_type', 'added_by', 'modify_by', 'date_added', 'date_modify')
    list_filter = ('content_type', 'date_added', 'date_modify', 'added_by', 'modify_by',)

    def edit(self, object: ProtectedFiles):
        return format_lazy('<id:{pk}> {text}', text=_('EDIT'), pk=object.pk)

    edit.admin_order_field = 'pk'
    edit.short_description = _('EDIT')

    def save_model(self, request, obj: ProtectedFiles, form, change: bool):
        if not change:
            obj.added_by = request.user
        else:
            obj.modify_by = request.user
            obj.date_modify = now()

        super(ProtectedFilesAdmin, self).save_model(request, obj, form, change)


class PublicFilesAdmin(ProtectedFilesAdmin):
    pass


admin.site.register(ProtectedFiles, ProtectedFilesAdmin)
admin.site.register(PublicFiles, PublicFilesAdmin)
