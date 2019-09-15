import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from pages.models import CMSPage

logger = logging.getLogger(__name__)


class StatuteView(TemplateView):
    template_name = 'pages/statute.html'
    slug = 'statute'

    def get_context_data(self, **kwargs):
        context = super(StatuteView, self).get_context_data(**kwargs)
        context['page'] = CMSPage.objects.get(slug=self.slug)
        return context


statute_view = StatuteView.as_view()
