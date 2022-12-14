from coffeapi.level3.domain import Conflicted, DoesNotExist
from coffeapi.level3.framework.http import Conflict, NotFound

class FrameworkCommonExceptionExceptionHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exc):
        if isinstance(exc, DoesNotExist):
            return NotFound()
        elif isinstance(exc, Conflicted):
            return Conflict()