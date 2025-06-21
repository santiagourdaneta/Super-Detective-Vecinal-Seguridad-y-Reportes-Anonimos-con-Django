from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # <--- NUEVA LÍNEA


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # <--- ¡ESTA ES LA LÍNEA NUEVA!
    path('', include('barrio_feedback.urls')),
]