# C:\Users\user\Downloads\barrio-seguro\mi_barrio_seguro\barrio_feedback\views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail # Aunque no la usamos directamente, es una buena práctica mantenerla si se explora en el futuro
from django.conf import settings

# Importaciones específicas para el envío manual de correo (solución SSL/TLS)
import ssl
import smtplib
from email.mime.text import MIMEText

from .models import Feedback
from .ai_processor import procesar_mensaje_ia
from .forms import CustomUserCreationForm

# --- Vista Principal: Envío y Visualización de Mensajes ---
@login_required # Solo usuarios logueados pueden acceder a esta vista
def index(request):
    """
    Maneja la lógica para enviar y mostrar los mensajes de feedback.
    Requiere que el usuario esté autenticado.
    """
    if request.method == 'POST':
        mensaje_original = request.POST.get('mensaje_original')
        destinatario = request.POST.get('destinatario')

     

        if mensaje_original:
            feedback_obj = Feedback.objects.create(
                mensaje_original=mensaje_original,
                destinatario=destinatario,

               
            )
            feedback_obj.mensaje_anonimo_y_constructivo = procesar_mensaje_ia(mensaje_original)
            feedback_obj.procesado = True
            feedback_obj.save()

            messages.success(request, "¡Gracias! Tu mensaje ha sido enviado al Super Detective Vecinal.")

            # --- Lógica de Envío de Correo al Administrador ---
            try:
                subject = "Nuevo Mensaje de Seguridad en el Barrio"
                email_body = f"""
¡Alerta del Super Detective Vecinal!

Se ha recibido un nuevo mensaje de seguridad:

Mensaje Original:
{mensaje_original}

Versión Procesada y Anónima (por el robot):
{feedback_obj.mensaje_anonimo_y_constructivo}

Destinatario Sugerido: {destinatario if destinatario else 'No especificado'}

Puedes ver más detalles en el panel de administración:
http://127.0.0.1:8000/admin/barrio_feedback/feedback/{feedback_obj.id}/

Atentamente,
Tu Super Detective Vecinal.
                """
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [settings.ADMIN_EMAIL]

                # Crea un contexto SSL que NO VERIFIQUE el certificado (SOLO PARA DESARROLLO)
                # ¡ADVERTENCIA! No usar en producción.
                context = ssl._create_unverified_context()

                msg = MIMEText(email_body)
                msg['Subject'] = subject
                msg['From'] = from_email
                msg['To'] = ", ".join(recipient_list)

                # Conecta al servidor SMTP usando smtplib.SMTP y luego starttls()
                with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                    server.starttls(context=context) # Inicia el cifrado TLS con el contexto
                    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    server.sendmail(from_email, recipient_list, msg.as_string())

                messages.info(request, "El administrador ha sido notificado por correo.")
            except Exception as e:
                messages.error(request, f"¡Hubo un problema al enviar el correo al administrador! Error: {e}")
            # --- Fin Lógica de Envío de Correo ---

        else:
            messages.error(request, "¡Ups! No puedes enviar un mensaje vacío. Por favor, escribe algo.")

        return redirect('index')
    else:
        feedbacks = Feedback.objects.filter(procesado=True).order_by('-fecha_envio')
        return render(request, 'barrio_feedback/index.html', {'feedbacks': feedbacks})

# --- Vista de Registro de Usuarios ---
def register_view(request):
    """
    Maneja la lógica para el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "¡Tu cuenta ha sido creada con éxito! Ahora puedes iniciar sesión.")
            return redirect(reverse_lazy('login'))
        else:
            messages.error(request, "¡Hubo un error al crear tu cuenta! Por favor, revisa los datos.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})