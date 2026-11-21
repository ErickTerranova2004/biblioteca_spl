from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.shortcuts import render

from .models import Categoria, Libro


@login_required
def inicio(request):
    contexto = {
        'total_libros': Libro.objects.count(),
        'total_ejemplares': Libro.objects.aggregate(t=Sum('disponibles'))['t'] or 0,
        'total_categorias': Categoria.objects.count(),
        'recientes': Libro.objects.order_by('-creado')[:5],
    }
    return render(request, 'core/inicio.html', contexto)


@login_required
def catalogo(request):
    q = request.GET.get('q', '').strip()
    libros = Libro.objects.select_related('categoria')
    if q:  # búsqueda simple: común a todas las variantes
        libros = libros.filter(Q(titulo__icontains=q) | Q(autor__icontains=q))
    contexto = {'libros': libros, 'q': q}
    # Bandera de configuración: la opción de exportar solo se ofrece en la Variante B
    if settings.ENABLE_REPORTS:
        contexto['mostrar_exportar'] = True
    return render(request, 'core/catalogo.html', contexto)
