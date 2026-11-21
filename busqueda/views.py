"""App opcional: búsqueda avanzada (ENABLE_ADVANCED_SEARCH)."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.decorators import feature_required
from core.models import Categoria, Libro


@login_required
@feature_required('ENABLE_ADVANCED_SEARCH')
def avanzada(request):
    g = request.GET
    libros = Libro.objects.select_related('categoria')
    if g.get('autor'):
        libros = libros.filter(autor__icontains=g['autor'])
    if g.get('categoria'):
        libros = libros.filter(categoria_id=g['categoria'])
    if g.get('desde'):
        libros = libros.filter(anio__gte=g['desde'])
    if g.get('hasta'):
        libros = libros.filter(anio__lte=g['hasta'])
    if g.get('solo_disponibles'):
        libros = libros.filter(disponibles__gt=0)
    return render(request, 'busqueda/avanzada.html', {
        'libros': libros, 'categorias': Categoria.objects.all(), 'f': g, 'buscado': bool(g)})
