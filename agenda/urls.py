import logging

from django.urls import path

from agenda.views import agenda_view

logger = logging.getLogger(__name__)

app_name = 'agenda'

urlpatterns = [
    path('', agenda_view, name='agenda_view'),
]
