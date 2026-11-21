from django.urls import path
from . import views

app_name = 'reportes'
urlpatterns = [
    path('', views.panel, name='panel'),
    path('catalogo.pdf', views.exportar_pdf, name='pdf'),
    path('catalogo.csv', views.exportar_csv, name='csv'),
]
