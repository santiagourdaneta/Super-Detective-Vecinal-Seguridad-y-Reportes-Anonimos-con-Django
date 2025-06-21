
Plataforma web construida con Django para fomentar la seguridad comunitaria. Permite a los usuarios enviar reportes anónimos sobre incidentes en el barrio, que son procesados y anonimizados por IA para ser compartidos y así mejorar la inteligencia y reacción vecinal.

# 🕵️‍♂️ Super Detective Vecinal: Seguridad y Reportes Anónimos 🕵️‍♀️

## Descripción del Proyecto

**Super Detective Vecinal** es una aplicación web diseñada para fortalecer la seguridad y la comunicación dentro de las comunidades. Permite a los residentes enviar **reportes de seguridad de forma anónima** sobre incidentes o preocupaciones en su barrio.

La plataforma utiliza **Django** como su potente backend, proporcionando un sistema robusto para la gestión de usuarios, la autenticación y el almacenamiento seguro de los reportes. Los mensajes enviados por los usuarios son procesados (lógica de anonimización/IA detrás) y luego se muestran de manera constructiva y anónima al resto de la comunidad, fomentando la inteligencia colectiva y la prevención.

## Características Principales

* **Reportes Anónimos:** Los usuarios pueden enviar mensajes de seguridad sin revelar su identidad.
* **Procesamiento de Mensajes:** Los reportes son analizados y transformados en mensajes anónimos y constructivos (uso de IA y lógica de anonimización).
* **Sistema de Autenticación:** Registro e inicio de sesión de usuarios seguros (Django's `User` model).
* **Gestión de Sesiones:** Manejo seguro de las sesiones de usuario.
* **Visualización de Reportes:** Mensajes procesados visibles para la comunidad.
* **Interfaz de Usuario Amigable:** Diseño intuitivo para facilitar el envío y la lectura de reportes.
* **Alertas Visibles:** Mensajes críticos destacados.

## Tecnologías Utilizadas

* **Python:** Lenguaje de programación principal.
* **Django:** Framework web para el backend, ORM, sistema de autenticación.
* **HTML5:** Estructura de las plantillas web.
* **CSS3:** Estilos y diseño responsivo.
* **PostgreSQL:** Base de datos.
* **Inteligencia Artificial / Procesamiento de Lenguaje Natural (NLP):** (Funcionalidad de "robot inteligente" y anonimización).

## Configuración y Ejecución Local

Sigue estos pasos para poner en marcha el proyecto en tu máquina local:

### Requisitos Previos

* **Python 3.x**
* **pip** (gestor de paquetes de Python)

### Pasos

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/santiagourdaneta/Super-Detective-Vecinal-Seguridad-y-Reportes-Anonimos-con-Django/
    cd Super-Detective-Vecinal-Seguridad-y-Reportes-Anonimos-con-Django
    ```

2.  **Crea y activa un entorno virtual:**
    Es una buena práctica aislar las dependencias de tu proyecto.
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instala las dependencias de Python:**
    Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura la base de datos y aplica migraciones:**
    Django usa migraciones para gestionar tu esquema de base de datos.
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario (opcional pero recomendado para acceder al admin):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear un usuario y contraseña.

6.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/`.

7.  **Accede a la Interfaz:**
    Abre tu navegador y ve a `http://127.0.0.1:8000/`.
    Para acceder al panel de administración de Django, ve a `http://127.0.0.1:8000/admin/` y usa las credenciales del superusuario.

## Despliegue (Producción)

Para desplegar esta aplicación en un entorno de producción, necesitarías:

* Un servidor web como Gunicorn/uWSGI (para servir Django) y Nginx/Apache (como proxy inverso).
* Configurar variables de entorno para `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, etc.
* Recopilar archivos estáticos (`python manage.py collectstatic`).
* Configurar HTTPS.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar esta aplicación, no dudes en abrir un *issue* o enviar un *pull request*.
