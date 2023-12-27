from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from project.websocket.consumers import SomeConsumer  # Importa tus funciones de manejo

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    # Define tus rutas aquí
                    # Por ejemplo:
                    # path(r'ws/some_path/$', consumers.SomeConsumer.as_asgi()),
                    path('ws/socket/', SomeConsumer.as_asgi()),
                ]
            )
        ),
    }
)

