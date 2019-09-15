import logging
from urllib.parse import quote

from django.http import HttpResponseForbidden, HttpResponse
from django.views.static import serve

logger = logging.getLogger(__name__)


def has_permission_to_file(request, path):
    return request.user.is_authenticated


# Development serving files if user has permission to read.
def development_serve(request, path, document_root=None, show_indexes=False):
    if has_permission_to_file(request, path):
        return serve(request, path, document_root, show_indexes)
    else:
        return HttpResponseForbidden()


def production_serve(request):
    logger.info('User %s requested file %s', request.user, quote(request.path, safe=''))
    if has_permission_to_file(request, request.path):
        response = HttpResponse()
        response.status_code = 200
        response['Content-Type'] = ''
        response['X-Accel-Redirect'] = quote(request.path, safe='')

        return response
    else:
        logger.warning('Access denied for user %s to file %s', request.user, quote(request.path, safe=''))
        return HttpResponseForbidden()
