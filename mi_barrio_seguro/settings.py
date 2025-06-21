from pathlib import Path
import os
from dotenv import load_dotenv # Nueva importación

load_dotenv() # Carga las variables del archivo .env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&iad-9ms5idpphx(b5(l_z@!^^k%qnhrvu9nzsh40*&ap^_gpu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',      # Para el panel de control del robot
    'django.contrib.auth',       # Para los usuarios (autenticación)
    'django.contrib.contenttypes', # Un tipo de pieza de Django
    'django.contrib.sessions',   # Para recordar si alguien ya entró
    'django.contrib.messages',   # Para los mensajes que ya usamos
    'django.contrib.staticfiles',# Para los dibujos (CSS/JS)
    'barrio_feedback.apps.BarrioFeedbackConfig',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_barrio_seguro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # <--- ¡CAMBIA A ESTA LÍNEA!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'mi_barrio_seguro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Le dice a Django que usaremos PostgreSQL
        'NAME': 'seguridad_barrio_db',                     # <--- ¡El nombre de tu base de datos!
        'USER': 'postgres',                               # <--- ¡El usuario de PostgreSQL que usarás! (Podría ser 'postgres' o el que creaste, como 'super_robot_user')
        'PASSWORD': '1234',              # <--- ¡LA CONTRASEÑA de ese usuario!
        'HOST': 'localhost',                               # Esto suele ser 'localhost' si PostgreSQL está en tu misma computadora
        'PORT': '',                                        # Puedes dejarlo vacío o poner '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Al final de settings.py
LOGIN_REDIRECT_URL = '/' # A dónde ir después de iniciar sesión con éxito
LOGOUT_REDIRECT_URL = '/accounts/logout/' # A dónde ir después de cerrar sesión

# Configuración de Correo Electrónico (al final de settings.py)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER') # Lee del .env
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD') # Lee del .env
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER') # Desde qué correo se envían

ADMIN_EMAIL = 'xxxxxxxx@gmail.com' # ¡PON AQUÍ TU CORREO PARA RECIBIR LOS MENSAJES!