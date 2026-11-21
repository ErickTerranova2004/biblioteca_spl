from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Categoria, Libro

LIBROS = [
    ('Ingeniería del software: un enfoque práctico', 'Roger S. Pressman', 'Ingeniería de software', 2010, '978-6071503145', 4),
    ('Ingeniería de software', 'Ian Sommerville', 'Ingeniería de software', 2011, '978-6073206037', 3),
    ('Software Product Lines: Practices and Patterns', 'Clements y Northrop', 'Ingeniería de software', 2001, '978-0201703320', 2),
    ('Design Patterns', 'Gamma, Helm, Johnson y Vlissides', 'Arquitectura', 1994, '978-0201633610', 2),
    ('Clean Architecture', 'Robert C. Martin', 'Arquitectura', 2017, '978-0134494166', 3),
    ('Two Scoops of Django', 'Greenfeld y Roy', 'Desarrollo web', 2022, '978-1735467221', 2),
    ('Django for Beginners', 'William S. Vincent', 'Desarrollo web', 2022, '978-1735467207', 5),
    ('Domain-Specific Languages', 'Martin Fowler', 'Lenguajes', 2010, '978-0321712943', 1),
    ('Fluent Python', 'Luciano Ramalho', 'Lenguajes', 2022, '978-1492056355', 3),
    ('Base de datos: diseño y gestión', 'Elmasri y Navathe', 'Bases de datos', 2016, '978-8478290857', 2),
    ('Gestión de la configuración del software', 'Jessica Keyes', 'Ingeniería de software', 2004, '978-0849319761', 1),
    ('Refactoring', 'Martin Fowler', 'Arquitectura', 2018, '978-0134757599', 2),
]


class Command(BaseCommand):
    help = 'Carga datos de demostración (libros y usuario demo/demo12345)'

    def handle(self, *args, **opts):
        for t, a, c, y, isbn, d in LIBROS:
            cat, _ = Categoria.objects.get_or_create(nombre=c)
            Libro.objects.get_or_create(isbn=isbn, defaults=dict(titulo=t, autor=a, categoria=cat, anio=y, disponibles=d))
        if not User.objects.filter(username='demo').exists():
            User.objects.create_superuser('demo', 'demo@unemi.edu.ec', 'demo12345', first_name='Bibliotecario')
        self.stdout.write(self.style.SUCCESS(f'{Libro.objects.count()} libros cargados. Usuario: demo / demo12345'))
