## game/consumers.py
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'pong_{self.room_name}'

        # Unirse al grupo de la sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Dejar el grupo de la sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Procesar el mensaje recibido desde el cliente
        data = json.loads(text_data)
        message = data['message']

        # Ejemplo: Enviar el mensaje recibido a todos en el grupo
        await self.send_group_message(message)

    async def send_group_message(self, message):
        # Enviar mensaje a todos en el grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'game_message',
                'message': message
            }
        )

    async def game_message(self, event):
        # Enviar el mensaje recibido al cliente
        message = event['message']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))