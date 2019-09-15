from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
import logging

# Get an instance of a logger
from django.views.generic import TemplateView, RedirectView

from protected_files.views import development_serve, production_serve

logger = logging.getLogger(__name__)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('agenda.urls')),
    path('', include('points.urls')),
    path('', include('pages.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns + (
                      static(settings.MEDIA_URL,
                             view=development_serve,
                             document_root=settings.MEDIA_ROOT))
else:

    urlpatterns = [
                      url(r'^media/', production_serve, name='protected_media')
                  ] + urlpatterns
