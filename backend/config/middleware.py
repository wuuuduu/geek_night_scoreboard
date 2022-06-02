from django.utils.deprecation import MiddlewareMixin


class XRealIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if "HTTP_X_REAL_IP" in request.META:
            request.META["HTTP_X_PROXY_REMOTE_ADDR"] = request.META["REMOTE_ADDR"]
            request.META["REMOTE_ADDR"] = request.META["HTTP_X_REAL_IP"]
