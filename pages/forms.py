from django import forms
from django_summernote.widgets import SummernoteWidget

from pages.models import CMSPage


class CMSPageForm(forms.ModelForm):
    class Meta:
        model = CMSPage
        fields = '__all__'
        widgets = {
            'public_content': SummernoteWidget()
        }
