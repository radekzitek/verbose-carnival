import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        log_message = (
            f"Incoming request: {request.method} {request.path}\n"
            f"Headers: {request.headers}\n"
            f"Body: {request.body.decode('utf-8', errors='ignore')}"
        )
        logger.debug(log_message)

        response = self.get_response(request)

        return response
