## game/consumers.py
import asyncio
import random
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class Player():
	def __init__(self):
		self.name: str = ""
		self.x: float = 0
		self.left: bool = False
		self.right: bool = False
		self.winner: bool = False
		self.points: int = 0
		self.speed: float = 0.5

	def Move(self, direction: str):
		if (direction == "left"):
			self.x -= self.speed
			if (self.x <= -10):
				self.x = -10	
		if (direction == "right"):
			self.x += self.speed
			if (self.x >= 10):
				self.x = 10
				
	def AddPoint(self):
		self.points += 1
		if (self.points == 7):
			self.winner = True
	
	def GetName(self):
		return self.name

class Ball():
	def __init__(self):
		self.name: str = "ball"
		self.x: float = 0
		self.z: float = 0
		self.speed: float = 0.025
		self.dirX: float = random.uniform(-1, 1)
		self.dirZ: float = random.uniform(-1, 1)

	def Move(self):
		self.x += self.speed * self.dirX
		self.z += self.speed * self.dirZ
		if (self.x >= 15 or self.x <= 15):
			self.dirX *= -1
		# if (self.z <= 15):
		# 	self.dirZ *= -1

class GameConsumer(AsyncWebsocketConsumer):
	player1 = Player()
	player2 = Player()
	ball = Ball()
	
	async def connect(self):
		self.room_name = self.scope['query_string'].decode().split('&')[0].split('=')[1]
		self.room_group_name = f'pong_{self.room_name}'

		if (self.player1.GetName() == "" or self.player2.GetName() == ""):
			if (self.player1.GetName() == ""):
				self.player1.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
			else:
				self.player2.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
		
		# Unirse al grupo de la sala
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name,
		)

		await self.accept()

		message = json.dumps(self.player1.__dict__) + "_" + json.dumps(self.player2.__dict__) + "_" + json.dumps(self.ball.__dict__)

		# Ejemplo: Enviar el mensaje recibido a todos en el grupo
		await self.send_group_message(message)

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

		self.ball.Move()

		if (incoming_user == self.player1.GetName()):
			if (incoming_type == "move"):
				self.player1.Move(incoming_value)
			if (incoming_type == "point"):
				self.player1.AddPoint()
		if (incoming_user == self.player2.GetName()):
			if (incoming_type == "move"):
				self.player2.Move(incoming_value)
			if (incoming_type == "point"):
				self.player2.AddPoint()
		if (incoming_user == "ball"):
			if (incoming_type == "move"):
				self.ball.Move()
		# if (incoming_user == "ball"):
		# 	if (incoming_type == "move"):
		# 		self.ball.Move()

		# Procesar el mensaje recibido desde el cliente
		# message = f'Hola desde el servidor {self.room_name}'
					
		message = json.dumps(self.player1.__dict__) + "_" + json.dumps(self.player2.__dict__) + "_" + json.dumps(self.ball.__dict__)
		print(self.ball.__dict__)

		# Ejemplo: Enviar el mensaje recibido a todos en el grupo
		await self.send_group_message(message)

		self.receive(text_data)

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