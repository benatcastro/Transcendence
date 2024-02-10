## game/routing.py
from django.urls import re_path
from . import consumers
from . import manager

websocket_urlpatterns = [
    re_path(r'ws/game/$', consumers.GameConsumer.as_asgi()),
    re_path(r'ws/tournament/$', manager.TournamentManager.as_asgi()),
]
