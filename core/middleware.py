import threading

_thread_locals = threading.local()

def get_current_user():
    """
    Retrieves the current user from the thread-local storage.
    Used by signals to identify the actor of a mutation.
    """
    return getattr(_thread_locals, 'user', None)

class RequestUserMiddleware:
    """
    Middleware that stores the current authenticated user in thread-local storage.
    Enables audit logging signals to access the actor without a request object.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = getattr(request, 'user', None)
        response = self.get_response(request)
        # Clear after request to prevent memory leaks or cross-request leakage
        if hasattr(_thread_locals, 'user'):
            del _thread_locals.user
        return response
