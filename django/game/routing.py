## game/routing.py
from django.conf.urls import url
from game.consumers import Pong

websocket_urlpatterns = [
    url(r'^ws/play/(?P<room_code>\w+)/$', Pong.as_asgi()),
]