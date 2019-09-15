from django import forms
from django.core.exceptions import ValidationError
from django_summernote.widgets import SummernoteWidget

from agenda.models import LectureModel
from django.utils.translation import gettext_lazy as _


class LectureForm(forms.ModelForm):
    class Meta:
        model = LectureModel
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget()
        }

    def clean_end_date(self):
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if end_date <= start_date:
            raise ValidationError(_('End date must be greater than start date.'))

        return end_date
