from django.contrib import admin
from django.db.models import Sum
from django.db.models.functions import Coalesce

from points.models import PointModel, PlayerModel, TypeOfPointsModel


class InlinePointModelAdmin(admin.TabularInline):
    model = PointModel
    extra = 1

    def get_queryset(self, request):
        qs = super(InlinePointModelAdmin, self).get_queryset(request)
        return qs.select_related("acquired_by_player", "type_of_points")


class PlayerModelAdmin(admin.ModelAdmin):
    search_fields = ("username",)
    list_filter = ("date_added",)
    list_display = ("username", "points", "date_added")
    inlines = [InlinePointModelAdmin]

    def get_queryset(self, request):
        qs = super(PlayerModelAdmin, self).get_queryset(request)
        return qs.annotate(points=Coalesce(Sum("points_set__value"), 0)).order_by(
            "-points"
        )

    def points(self, obj: PlayerModel):
        return obj.points

    points.admin_order_field = "points"


class PointModelAdmin(admin.ModelAdmin):
    class IsAcquiredByPlayerFilter(admin.SimpleListFilter):
        title = "Is acquired by player"
        parameter_name = "is_acquired_by_player"

        def value(self):
            value = super().value()
            if value == "1":
                return True
            elif value == "0":
                return False
            elif value is not None:
                raise ValueError()

        def lookups(self, request, model_admin):
            return (
                ("1", "True"),
                ("0", "False"),
            )

        def queryset(self, request, queryset):
            value = self.value()
            if value is not None:
                return queryset.filter(acquired_by_player__isnull=not value)
            return queryset

    search_fields = (
        "code",
        "value",
        "acquired_by_player__username",
        "type_of_points__name",
        "description",
    )
    list_filter = (
        "type_of_points__name",
        IsAcquiredByPlayerFilter,
        "value",
        "acquired_by_player__username",
    )
    list_display = (
        "code",
        "type_of_points",
        "value",
        "acquired_by_player",
        "description",
    )

    def get_queryset(self, request):
        qs = super(PointModelAdmin, self).get_queryset(request)
        return qs.select_related("acquired_by_player", "type_of_points")


admin.site.register(PointModel, PointModelAdmin)
admin.site.register(PlayerModel, PlayerModelAdmin)
admin.site.register(TypeOfPointsModel)
