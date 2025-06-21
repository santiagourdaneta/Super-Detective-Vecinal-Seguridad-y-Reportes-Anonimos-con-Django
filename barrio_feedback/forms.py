# C:\Users\user\Downloads\barrio-seguro\mi_barrio_seguro\barrio_feedback\forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# Obtenemos el modelo de usuario actual de Django (es el que creamos con createsuperuser)
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields # Mantener los campos por defecto (username, password)
        # Si quisieras añadir más campos al registro, los listarías aquí:
        # fields = ('username', 'email', 'first_name', 'last_name',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields