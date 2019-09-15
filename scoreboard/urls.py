import logging

from django.urls import path

from pages.views import contact_view, download_view, sponsors_view

logger = logging.getLogger(__name__)

app_name = 'scoreboard'

urlpatterns = []
