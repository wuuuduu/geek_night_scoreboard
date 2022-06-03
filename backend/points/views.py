# Create your views here.
import logging

from django.contrib import messages
from django.db import transaction
from django.views.generic import FormView
from django_filters.views import FilterView

from pages.models import CMSPage
from points.filters import ProductFilter
from points.forms import PointModelForm
from points.models import PlayerModel, PointModel
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class AddPointsView(FormView):
    template_name = "add_points.html"
    form_class = PointModelForm
    success_url = "/points/add/"
    cms_page_slug = "points/add"

    def get_context_data(self, **kwargs):
        context = super(AddPointsView, self).get_context_data(**kwargs)
        try:
            context["page"] = CMSPage.objects.get(slug=self.cms_page_slug, visible=True)
        except CMSPage.DoesNotExist as e:
            logger.debug("%s (%s)" % (e, self.cms_page_slug))
        return context

    def form_valid(self, form):
        code = form.cleaned_data.get("code")
        player_name = form.cleaned_data.get("acquired_by_player")
        with transaction.atomic():
            player, player_created = PlayerModel.objects.get_or_create(
                username=player_name
            )
            point: PointModel = PointModel.objects.select_for_update().get(
                code=code, acquired_by_player__isnull=True
            )
            point.acquired_by_player = player
            point.save(update_fields=["acquired_by_player"])
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _("We have added %s points to your score. Thank you!") % point.value,
        )
        return super().form_valid(form)


add_points_view = AddPointsView.as_view()


class HighScoresView(FilterView):
    def dispatch(self, request, *args, **kwargs):
        if not request.GET:
            # it forces to use filter_queryset method from ProductFilter class
            request.GET._mutable = True
            request.GET.update({"page": 1})
        return super(HighScoresView, self).dispatch(request, *args, **kwargs)

    model = PlayerModel
    filterset_class = ProductFilter
    template_name = "highscores.html"
    context_object_name = "players"
    paginate_by = 20
    cms_page_slug = "highscores"

    def get_context_data(self, **kwargs):
        context = super(HighScoresView, self).get_context_data(**kwargs)
        try:
            context["page"] = CMSPage.objects.get(slug=self.cms_page_slug, visible=True)
        except CMSPage.DoesNotExist as e:
            logger.debug("%s (%s)" % (e, self.cms_page_slug))
        return context


high_scores_view = HighScoresView.as_view()
