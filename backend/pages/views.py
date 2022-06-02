import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from pages.models import CMSPage

logger = logging.getLogger(__name__)


class StatuteView(TemplateView):
    template_name = "pages/statute.html"
    cms_page_slug = "statute"

    def get_context_data(self, **kwargs):
        context = super(StatuteView, self).get_context_data(**kwargs)
        try:
            context["page"] = CMSPage.objects.get(slug=self.cms_page_slug, visible=True)
        except CMSPage.DoesNotExist as e:
            logger.debug("%s (%s)" % (e, self.cms_page_slug))
        return context


statute_view = StatuteView.as_view()
