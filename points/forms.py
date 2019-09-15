from django import forms
from django.core.exceptions import ValidationError
from django_select2.forms import Select2Widget
from django_summernote.widgets import SummernoteWidget

from django.utils.translation import gettext_lazy as _

from points.models import PointModel, PlayerModel


class PointModelForm(forms.Form):
    acquired_by_player = forms.ModelChoiceField(
        widget=Select2Widget,
        required=True,
        queryset=PlayerModel.objects.all(),
        label=_('Your nick')
    )

    code = forms.CharField(
        max_length=50,
        required=True,
        label=_('Code')
    )

    class Meta:
        fields = ('acquired_by_player', 'code')

    def clean_code(self):
        code = self.cleaned_data.get('code')
        acquired_by_player = self.cleaned_data.get('acquired_by_player')
        try:
            point: PointModel = PointModel.objects.get(code=code)
            if point.acquired_by_player is not None:
                if point.acquired_by_player == acquired_by_player:
                    raise ValidationError(_('We are sorry, you have already used the entered code!'))
                else:
                    raise ValidationError(_('We are sorry, the entered code is already used by someone else!'))
        except PointModel.DoesNotExist:
            raise ValidationError(_('We are sorry, but the entered code is invalid! :('))
        return code
