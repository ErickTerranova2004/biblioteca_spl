from functools import wraps

from django.conf import settings
from django.http import Http404


def feature_required(flag):
    """Bloquea una vista si la característica no está activa en la variante."""
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if not getattr(settings, flag, False):
                raise Http404('Característica no disponible en esta variante')
            return view(request, *args, **kwargs)
        return wrapper
    return decorator
