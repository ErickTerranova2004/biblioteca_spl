from django.conf import settings
from django.db import models


class Notificacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creada']
        verbose_name_plural = 'notificaciones'

    def __str__(self):
        return self.mensaje
