# Websockets
│   ├── project
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── websocket
│   │   │   ├── consumers.py
│   │   │   ├── __init__.py
│   │   │   └── routing.py
│   │   └── wsgi.py

## configuracion asgi para el modo asyncrono y pueda funcionar los sockets

Está configurando un servidor ASGI (Asynchronous Server Gateway Interface) utilizando Django Channels.
### file project.asgi.py
```sh
# Importa la aplicación ASGI de Django
from django.core.asgi import get_asgi_application

# Importa las capas de autenticación de Channels y el enrutador de URL
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# Importa las rutas de WebSocket definidas en el módulo 'routing' dentro del paquete 'websocket'
from project.websocket.routing import websocket_urlpatterns

# Importa el módulo 'routing' del paquete 'websocket'
import project.websocket.routing

# Configura la variable de entorno 'DJANGO_SETTINGS_MODULE' con la ruta al archivo de configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

# Configura el enrutador de protocolo con dos capas: "http" y "websocket"
application = ProtocolTypeRouter({
    # Capa "http": Utiliza la aplicación ASGI de Django para manejar las solicitudes HTTP
    "http": get_asgi_application(),

    # Capa "websocket": Utiliza una pila de middleware de autenticación y un enrutador de URL para WebSocket
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # Especifica las rutas de WebSocket utilizando las definidas en 'websocket_urlpatterns'
            project.websocket.routing.websocket_urlpatterns
        )
    ),
})

```
### file websocket.consumers.py
Este archivo maneja eventos como la conexión, desconexión y recepción de mensajes en una conexión WebSocket. Puedes personalizar y extender este consumidor para implementar la lógica específica que necesites para WebSocket.
```sh
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class SomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Método llamado cuando se establece una conexión WebSocket.
        print("WebSocket connected")
        await self.accept()  # Acepta la conexión.

    async def disconnect(self, close_code):
        # Método llamado cuando se cierra la conexión WebSocket.
        print("WebSocket disconnected")

    async def receive(self, text_data):
        # Método llamado cuando se recibe un mensaje desde el cliente WebSocket.
        print(f"Server Supeer Andy hero SAMA message received: {text_data}")
        await self.send(text_data="You said: " + text_data)
        # Envía un mensaje de vuelta al cliente WebSocket.

```
### file websocket.routing.py
Este código se ocupa de definir las rutas de WebSocket en Django Channels.
```sh
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket/$', consumers.SomeConsumer.as_asgi()),
]

```
# Importa las Dependencias Necesarias:
- re_path: Función para definir rutas de URL utilizando expresiones regulares.

- Importa el Consumidor: from . import consumers: Importa el módulo consumers de la misma aplicación (paquete).

- Define websocket_urlpatterns: websocket_urlpatterns es una lista que contiene las rutas de URL para las conexiones WebSocket.

- re_path(r'ws/socket/$', consumers.SomeConsumer.as_asgi()),:Utiliza re_path para definir una ruta de URL utilizando una expresión regular.
La expresión regular 'ws/socket/$' coincide con las solicitudes WebSocket en la ruta ws/socket/.Asocia esta ruta al consumidor SomeConsumer utilizando consumers.SomeConsumer.as_asgi().
### file project.settings.py
```sh
ASGI_APPLICATION = "project.websocket.routing.application"

CORS_ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

```

## CHANNEL_LAYERS:
### Especifica la configuración para el sistema de capas de canales (Channels Layer).

- "default": Define un conjunto predeterminado de capas.
- "BACKEND": "channels_redis.core.RedisChannelLayer": Indica que se utilizará el backend de Redis para gestionar las capas de canales.
- "CONFIG": Contiene la configuración específica para el backend de Redis.
- "hosts": [("redis", 6379)]: Especifica la ubicación del servidor Redis al que se conectará la capa de canales. En este caso, se asume que hay un servicio Redis llamado "redis" ejecutándose en el puerto 6379.

## CORS_ALLOW_HEADERS:
Configura las cabeceras permitidas para las solicitudes CORS (Cross-Origin Resource Sharing).

Establece las cabeceras que el servidor permitirá en las solicitudes CORS.

## ASGI_APPLICATION:
Indica la aplicación ASGI (Asynchronous Server Gateway Interface) que se utilizará para manejar las conexiones WebSocket.

En este caso, se refiere a la aplicación definida en el módulo routing del paquete websocket de la aplicación project.
### Añadiendo nuevas cosas al docker-compose para hacer funcionar los websockets

El servidor Redis es una base de datos en memoria que se utiliza para almacenar datos de manera eficiente y rápida. Algunas de sus funciones clave son:

- Almacenamiento en caché: Guarda datos temporalmente para acceder rápidamente a ellos.

- Colas de mensajes: Utilizado para implementar colas de tareas asíncronas.

- Sesiones web: Almacena sesiones de usuario de manera eficiente.

- Conteo de visitas: Realiza un seguimiento en tiempo real del recuento de visitas.

- Estructuras de datos avanzadas: Ofrece listas, conjuntos y otras estructuras útiles.

En Django Channels, se utiliza como backend para manejar conexiones WebSocket y facilitar la comunicación en tiempo real. En la configuración, estamos usando Redis para las capas de canal y también estás configurando CORS (Cross-Origin Resource Sharing) para permitir solicitudes desde diferentes dominios.
```sh
  redis:
    container_name: redis
    image: "redis:latest"
    expose:
      - "6379"
  django:
    container_name: django
    build: ./django
    command: sh -c "python manage.py makemigrations &&
                    python manage.py migrate &&
                    uvicorn project.asgi:application --host 0.0.0.0 --port ${APP_PORT} --reload"
```
