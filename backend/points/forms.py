from django import forms
from django.core.exceptions import ValidationError
from django_select2.forms import Select2Widget, Select2TagWidget, Select2TagMixin
from django_summernote.widgets import SummernoteWidget

from django.utils.translation import gettext_lazy as _

from points.models import PointModel, PlayerModel


class CustomSelect2TagWidget(Select2Widget):
    def build_attrs(self, base_attrs, extra_attrs=None):
        """Add select2's tag attributes."""
        default_attrs = {
            "data-minimum-input-length": 1,
            "data-tags": "true",
            "data-maximum-input-length": 32,
        }
        default_attrs.update(base_attrs)
        return super().build_attrs(default_attrs, extra_attrs=extra_attrs)


class AcquireByPlayerModelChoiceField(forms.ModelChoiceField):
    def to_python(self, value):
        if value in self.empty_values:
            return None
        return value


class PointModelForm(forms.Form):
    acquired_by_player = AcquireByPlayerModelChoiceField(
        widget=CustomSelect2TagWidget,
        required=True,
        queryset=PlayerModel.objects.all(),
        label=_("Your nick"),
        to_field_name="username",
    )

    code = forms.CharField(max_length=50, required=True, label=_("Code"))

    class Meta:
        fields = ("acquired_by_player", "code")

    def clean_acquired_by_player(self):
        value = self.cleaned_data["acquired_by_player"]
        if value:
            return value[:100]

        return value

    def clean_code(self):
        code = self.cleaned_data.get("code")
        acquired_by_player = self.cleaned_data.get("acquired_by_player")
        try:
            point: PointModel = PointModel.objects.select_related(
                "acquired_by_player"
            ).get(code=code)
            if point.acquired_by_player is not None:
                if point.acquired_by_player.username == acquired_by_player:
                    raise ValidationError(
                        _("We are sorry, you have already used the entered code!")
                    )
                else:
                    raise ValidationError(
                        _(
                            "We are sorry, the entered code is already used by someone else!"
                        )
                    )
        except PointModel.DoesNotExist:
            raise ValidationError(
                _("We are sorry, but the entered code is invalid! :(")
            )
        return code
