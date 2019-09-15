import logging

from django.urls import path

from points.views import high_scores_view, add_points_view

logger = logging.getLogger(__name__)

app_name = 'points'

urlpatterns = [
    path('highscores/', high_scores_view, name='high_scores_view'),
    path('points/add/', add_points_view, name='add_points_view')
]
