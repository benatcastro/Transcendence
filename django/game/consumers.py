## game/consumers.py
import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Player():
	name: str = ""
	left: bool = False
	right: bool = False
	points: int = 0

class GameConsumer(AsyncWebsocketConsumer):
	player1 = Player()
	player2 = Player()
	
	async def connect(self):
		self.room_name = self.scope['query_string'].decode().split('&')[0].split('=')[1]
		self.room_group_name = f'pong_{self.room_name}'

		if (self.player1.name == ""):
			self.player1.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
			self.player1.left = False
			self.player1.right = False
			self.player1.points = 0
		else:
			self.player2.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
			self.player2.left = False
			self.player2.right = False
			self.player2.points = 0
		
		print("\n\nPlayer1 = " + json.dumps(self.player1.__dict__) + "\nPlayer2 = " + json.dumps(self.player2.__dict__) + "\n\n")

		# Unirse al grupo de la sala
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name,
		)

		await self.accept()

	async def disconnect(self, close_code):
		# Dejar el grupo de la sala
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name,
		)

	async def receive(self, text_data):
		incoming_user: str = text_data.split('_')[0]
		incoming_type: str = text_data.split('_')[1].split(':')[0]
		incoming_value: str = text_data.split('_')[1].split(':')[1]
		if (incoming_user == self.player1.name):
			if (incoming_type == "move"):
				if (incoming_value == "left1"):
					self.player1.left = True
				if (incoming_value == "right1"):
					self.player1.right = True
				if (incoming_value == "left0"):
					self.player1.left = False
				if (incoming_value == "right0"):
					self.player1.right = False
		if (incoming_user == self.player2.name):
			if (incoming_type == "move"):
				if (incoming_value == "left1"):
					self.player2.left = True
				if (incoming_value == "right1"):
					self.player2.right = True
				if (incoming_value == "left0"):
					self.player2.left = False
				if (incoming_value == "right0"):
					self.player2.right = False

		# print("\n\nPlayer1 = " + json.dumps(self.player1.__dict__) + "\nPlayer2 = " + json.dumps(self.player2.__dict__) + "\n\n")
		# Procesar el mensaje recibido desde el cliente
		# message = f'Hola desde el servidor {self.room_name}'
					
		message = json.dumps(self.player1.__dict__) + "_" + json.dumps(self.player2.__dict__)

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

		#print(message)
		# Enviar el mensaje al WebSocket
		await self.send(text_data=f'{message}')