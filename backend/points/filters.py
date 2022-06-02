from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, ModelChoiceFilter

from points.models import TypeOfPointsModel, PlayerModel


class ProductFilter(FilterSet):
    # code = CharFilter(field_name='points_set__code', lookup_expr='exact', label=_('Code'))
    type_of_points = ModelChoiceFilter(
        field_name="points_set__type_of_points",
        queryset=TypeOfPointsModel.objects.all().order_by("name"),
        label=_("Category"),
        empty_label=_("OVERALL"),
    )

    def filter_queryset(self, queryset):
        qs = super(ProductFilter, self).filter_queryset(queryset)
        return (
            qs.annotate(points=Coalesce(Sum("points_set__value"), 0))
            .distinct()
            .order_by("-points")
        )

    class Meta:
        model = PlayerModel
        fields = []
