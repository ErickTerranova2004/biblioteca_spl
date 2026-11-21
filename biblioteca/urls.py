"""URLs del proyecto BiblioSPL.

Las apps opcionales se incluyen solo si la variante activa las habilita
(include() condicional), de modo que en la Variante A sus rutas no existen.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('cuentas.urls')),
    path('', include('core.urls')),
]

if settings.ENABLE_REPORTS:
    urlpatterns.append(path('reportes/', include('reportes.urls')))

if settings.ENABLE_NOTIFICATIONS:
    urlpatterns.append(path('notificaciones/', include('notificaciones.urls')))

if settings.ENABLE_ADVANCED_SEARCH:
    urlpatterns.append(path('busqueda/', include('busqueda.urls')))
