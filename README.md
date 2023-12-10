# UML Diagrams

## Class Diagrams

### Backend Class Diagram

![Backend Class Diagram](uml/Class_Diagram_Backend.png)

### Gameplay Class Diagram

![Gameplay Class Diagram](uml/GamePlay_Class.png)

### Security Class Diagram

![Security Class Diagram](uml/Seecurity_Class.png)

### Graphics Class Diagram

![Graphics Class Diagram](uml/Graphics_Class.png)

### User Class Diagram

![User Class Diagram](uml/User_Class.png)

## Component Diagrams

### Backend Component Diagram

![Backend Component Diagram](uml/Component_Diagram_Backend.png)

### DevOps Component Diagram

![DevOps Component Diagram](uml/Devops_Component.png)

### Gameplay Component Diagram
![Gameplay Component Diagram](uml/GamePlay_Component.png)

### Security Component Diagram

![Security Component Diagram](uml/Security_Component.png)

### Graphics Component Diagram

![Graphics Component Diagram](uml/Graphic_Component.png)

### User Component Diagram

![User Component Diagram](uml/User_Component.png)

## Sequence Diagrams

### Backend Sequence Diagram

![Backend Sequence Diagram](uml/Sequence_Diagram_Backend.png)

### Gameplay Sequence Diagram

![Gameplay Sequence Diagram](uml/GamePlay_Sequence.png)

### Security Sequence Diagram

![Security Sequence Diagram](uml/Security_Sequence.png)

### Graphics Sequence Diagram

![Graphics Sequence Diagram](uml/Graphic_Sequence.png)

### User Sequence Diagram

![User Sequence Diagram](uml/User_Sequence.png)


# Django
## _Static Files_

# Information on how to configure static files and hot reload
- [Whitenose Link](https://whitenoise.readthedocs.io/en/latest/django.html)
-  [livesync](https://github.com/fabiogibson/django-livesync)
-  [Django-Extensions](https://django-extensions.readthedocs.io/en/latest/)
Django Extensions es una colección de extensiones personalizadas para Django Framework.Estos incluyen comandos de administración, campos de bases de datos adicionales, extensiones de administración y mucho más.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/)

## Tech

- Whitnoise:
En el archivo principal setting.py añadimos:
WHITENOISE_AUTOREFRESH = True  # Habilita la actualización en tiempo real para archivos estáticos

- django-extensions:
django-extensions es una biblioteca de terceros para Django que proporciona un conjunto de utilidades y comandos adicionales para facilitar el desarrollo. Incluye características como comandos de shell mejorados, manejo de archivos, generadores de códigos y más.

- livesync:
django-livesync es una extensión de django-extensions que agrega la capacidad de recargar automáticamente el servidor de desarrollo de Django cuando se detectan cambios en el código fuente. Esto facilita la visualización inmediata de los efectos de los cambios sin necesidad de reiniciar manualmente el servidor. La opción --livesync se utiliza al ejecutar el servidor de desarrollo para habilitar esta funcionalidad de recarga en tiempo real.

- Werkzeug:
Depurador para django con las siguientes funciones:
Principales características de Werkzeug:

  - **Servidor de Desarrollo:** Proporciona un servidor de desarrollo que facilita la ejecución y prueba de aplicaciones web durante el desarrollo local. Incluye recarga automática del servidor cuando hay cambios en el código fuente.

  - **Depurador Interactivo:** Ofrece un depurador interactivo que se activa en caso de errores, proporcionando información detallada sobre el estado de la aplicación en el momento del error.

  - **Manejo de Solicitudes y Respuestas HTTP:** Contiene utilidades para manejar solicitudes y respuestas HTTP, facilitando la construcción de aplicaciones web.

  - **Utilidades Generales:** Incluye varias utilidades que son útiles para el desarrollo web, como manipulación de URL, manejo de cookies, y más.


## Requirements django


For installation in docker...

```sh
pip install -r requirements.txt
```
or
```sh
pip3 install -r requirements.txt
```
| Package | version |
| ------ | ------ |
| django-rest-framework | 0.1.0 |
| gunicorn | 21.2.0 |
| whitenoise | 6.6.0 |
| django-livesync | 0.5 |
| django-extensions | 3.2.3 |
| Werkzeug | 3.0.1 |

## Docker

- FROM python:3.8: Utiliza la imagen oficial de Python 3.8 como base para tu imagen.

- ENV DockerHOME=/home/app/webapp: Establece una variable de entorno llamada DockerHOME con el valor /home/app/webapp.

- RUN mkdir -p $DockerHOME: Crea el directorio especificado por DockerHOME y sus subdirectorios, si es necesario.

- WORKDIR $DockerHOME: Establece el directorio de trabajo actual dentro del contenedor.

- ENV PYTHONDONTWRITEBYTECODE 1 y ENV PYTHONUNBUFFERED 1: Establecen variables de entorno para la configuración de Python, como se explicó en respuestas anteriores.

- RUN pip install --upgrade pip: Actualiza la herramienta pip a la última versión.

- COPY . $DockerHOME: Copia el contenido del directorio actual (donde se encuentra el Dockerfile) al directorio especificado por DockerHOME dentro del contenedor.

- RUN pip install -r requirements.txt: Instala las dependencias de Python especificadas en el archivo requirements.txt.

- EXPOSE 8000: Informa a Docker que el contenedor escuchará en el puerto 8000. Esto es más una documentación para el usuario que ejecuta el contenedor y no tiene un impacto directo en la red del contenedor.

- CMD python manage.py runserver: Especifica el comando predeterminado que se ejecutará cuando el contenedor se inicie. En este caso, se inicia el servidor de desarrollo de Django.

  -  PYTHONDONTWRITEBYTECODE=1: Evita que Python genere archivos de bytecode (.pyc) al importar módulos. Estos archivos no son necesarios en entornos de contenedor y desarrollo, y desactivarlos puede reducir el tamaño del contenedor.

  - PYTHONUNBUFFERED=1: Deshabilita el búfer de salida en Python, asegurando que la salida esté disponible de inmediato en la consola. Esto es útil para obtener logs y mensajes de salida sin esperar a que se llene un búfer, especialmente en entornos de contenedor y desarrollo.
