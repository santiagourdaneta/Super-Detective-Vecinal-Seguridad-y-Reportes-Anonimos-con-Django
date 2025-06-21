from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.index, name='send_feedback'),
    path('register/', views.register_view, name='register'), # <--- ¡Nueva Línea!
]