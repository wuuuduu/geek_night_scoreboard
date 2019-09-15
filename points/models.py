from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils.timezone import now
from ordered_model.models import OrderedModel
from django.utils.translation import gettext_lazy as _

from pages.helpers import clean_html


class PlayerModel(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False, unique=True)
    date_added = models.DateTimeField(null=False, default=now, editable=False)

    class Meta:
        verbose_name = _('Player')
        verbose_name_plural = _('Players')

    def __str__(self):
        return f'{self.username}'


class TypeOfPointsModel(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class PointModel(models.Model):
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    value = models.PositiveIntegerField(null=False, blank=False)
    acquired_by_player = models.ForeignKey(
        PlayerModel,
        related_name='points_set',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    type_of_points = models.ForeignKey(
        TypeOfPointsModel,
        related_name='points_set',
        on_delete=models.CASCADE,
        null=False
    )

    description = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        verbose_name = _('Points')
        verbose_name_plural = _('Points')

    def __str__(self):
        return f'{self.code} ({self.value}) - {self.acquired_by_player}'
