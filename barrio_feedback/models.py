# C:\Users\user\Downloads\barrio-seguro\mi_barrio_seguro\barrio_feedback\models.py

from django.db import models

class Feedback(models.Model):
    mensaje_original = models.TextField()
    mensaje_anonimo_y_constructivo = models.TextField(blank=True, null=True)
    destinatario = models.CharField(max_length=100, blank=True, null=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    procesado = models.BooleanField(default=False)

    def __str__(self):
        return f"Feedback de {self.fecha_envio.strftime('%Y-%m-%d %H:%M')}"