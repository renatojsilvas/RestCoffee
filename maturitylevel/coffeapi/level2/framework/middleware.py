from coffeapi.level2.domain import DoesNotExist
from coffeapi.level2.framework.http import NotFound

class FrameworkCommonExceptionExceptionHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exc):
        if isinstance(exc, DoesNotExist):
            return NotFound()