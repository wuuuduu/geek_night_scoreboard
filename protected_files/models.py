from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from protected_files.validators import validate_file_size_and_content_type
from django.utils.translation import gettext_lazy as _


class DefaultUserInfo(models.Model):
    added_by = models.ForeignKey(get_user_model(), default=None, null=True, editable=False, on_delete=models.SET_NULL,
                                 related_name="+")
    modify_by = models.ForeignKey(get_user_model(), default=None, null=True, editable=False, blank=True, on_delete=models.SET_NULL,
                                  related_name="+")

    class Meta:
        abstract = True


class DefaultDateInfo(models.Model):
    date_added = models.DateTimeField(null=False, default=now, editable=False)
    date_modify = models.DateTimeField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.pk and 'update_fields' not in kwargs:
            self.date_modify = now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class FileContentTypes(DefaultDateInfo):
    content_type = models.CharField(max_length=255,
                                    unique=True,
                                    editable=False,
                                    null=False)

    def __str__(self):
        return self.content_type


class ProtectedFiles(DefaultDateInfo, DefaultUserInfo):
    file = models.FileField(upload_to='protected/',
                            validators=[validate_file_size_and_content_type]
                            )
    content_type = models.ForeignKey(FileContentTypes,
                                     related_name="public_file_content_type",
                                     on_delete=models.PROTECT,
                                     null=False,
                                     blank=True
                                     )

    class Meta:
        verbose_name = _("Protected file")
        verbose_name_plural = _("Protected files")

    def __str__(self):
        return '{}'.format(self.file)


class PublicFiles(DefaultDateInfo, DefaultUserInfo):
    file = models.FileField(upload_to='public/',
                            validators=[validate_file_size_and_content_type]
                            )
    content_type = models.ForeignKey(FileContentTypes,
                                     related_name="file_content_type",
                                     on_delete=models.PROTECT,
                                     null=False,
                                     blank=True
                                     )

    class Meta:
        verbose_name = _("Public file")
        verbose_name_plural = _("Public files")

    def __str__(self):
        return '{}'.format(self.file)
