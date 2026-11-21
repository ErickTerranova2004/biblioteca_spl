"""Cuando se registra un libro nuevo, se notifica a todos los usuarios."""
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Libro
from .models import Notificacion


@receiver(post_save, sender=Libro)
def avisar_libro_nuevo(sender, instance, created, **kwargs):
    if created:
        Notificacion.objects.bulk_create([
            Notificacion(usuario=u, mensaje=f'Nuevo libro disponible: «{instance.titulo}» de {instance.autor}')
            for u in get_user_model().objects.filter(is_active=True)
        ])
