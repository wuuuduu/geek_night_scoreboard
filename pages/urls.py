import logging

from django.urls import path

from pages.views import statute_view

logger = logging.getLogger(__name__)

app_name = 'pages'

urlpatterns = [
    path('statute/', statute_view, name='statute_view'),
]
