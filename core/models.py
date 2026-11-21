from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=120)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='libros')
    anio = models.PositiveIntegerField('año')
    isbn = models.CharField(max_length=20, unique=True)
    disponibles = models.PositiveIntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return f'{self.titulo} ({self.autor})'
