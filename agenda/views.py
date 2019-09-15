from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from agenda.models import RoomModel


class AgendaView(TemplateView):
    template_name = 'agenda.html'

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)
        context['rooms'] = RoomModel.objects.all().prefetch_related('lecture_set')
        return context


agenda_view = AgendaView.as_view()