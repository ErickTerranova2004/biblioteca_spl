from django.contrib import admin
from .models import Categoria, Libro

admin.site.register(Categoria)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'anio', 'disponibles')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'autor', 'isbn')
