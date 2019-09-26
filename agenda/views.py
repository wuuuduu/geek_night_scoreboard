import logging
from django.views.generic import TemplateView

from agenda.models import RoomModel
from pages.models import CMSPage

logger = logging.getLogger(__name__)


class AgendaView(TemplateView):
    template_name = 'agenda.html'
    cms_page_slug = 'agenda'

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)
        context['rooms'] = RoomModel.objects.all().prefetch_related('lecture_set')
        try:
            context['page'] = CMSPage.objects.get(slug=self.cms_page_slug, visible=True)
        except CMSPage.DoesNotExist as e:
            logger.debug('%s (%s)' % (e, self.cms_page_slug))
        return context


agenda_view = AgendaView.as_view()
