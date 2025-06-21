from django.contrib import admin
from .models import Feedback # Traemos el "plano" de nuestro mensaje secreto

# Le decimos al robot que muestre los mensajes de Feedback en su panel de control
admin.site.register(Feedback)