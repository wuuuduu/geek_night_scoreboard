from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import logging

# Get an instance of a logger

logger = logging.getLogger(__name__)

urlpatterns = [
    path(f"{settings.ADMIN_URL}/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("", include("agenda.urls")),
    path("", include("points.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass
