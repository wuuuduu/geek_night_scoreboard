from django.db import models
from django.utils.timezone import now
from ordered_model.models import OrderedModel
from django.utils.translation import gettext_lazy as _

from pages.helpers import clean_html


class RoomModel(OrderedModel):
    name = models.CharField(max_length=144, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")


class LectureModel(OrderedModel):
    author = models.CharField(max_length=255, null=False, blank=True)
    description = models.CharField(max_length=1000, null=False, blank=False)
    start_date = models.DateTimeField(default=now, null=False, blank=False)
    end_date = models.DateTimeField(default=now, null=False, blank=False)
    room = models.ForeignKey(
        RoomModel,
        related_name="lecture_set",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return (
            f"{self.author} - {self.room} - "
            f'{self.start_date.strftime("%Y-%m-%d %H:%I")} - {self.end_date.strftime("%Y-%m-%d %H:%I")}'
        )

    class Meta:
        ordering = ("order",)
        verbose_name = _("Lecture")
        verbose_name_plural = _("Lectures")

    def save(self, **kwargs):
        self.description = clean_html(self.description)
        return super(LectureModel, self).save(**kwargs)
