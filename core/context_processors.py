from django.conf import settings


def producto(request):
    """Expone la variante y sus características a todas las plantillas."""
    return {
        'producto': settings.PRODUCT,
        'variante': settings.PRODUCT_VARIANT,
        'features': {
            'ENABLE_REPORTS': settings.ENABLE_REPORTS,
            'ENABLE_NOTIFICATIONS': settings.ENABLE_NOTIFICATIONS,
            'ENABLE_ADVANCED_SEARCH': settings.ENABLE_ADVANCED_SEARCH,
        },
    }
