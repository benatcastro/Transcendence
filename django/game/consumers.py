## game/manager.py
import asyncio
import random
import math
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class Player:
	def __init__(self, name: str = ""):
		self.name: str = name
		self.x: float = 0
		self.y: float = 0
		self.left: bool = False
		self.right: bool = False
		self.winner: bool = False
		self.points: int = 0
		self.speed: float = 1
		self.dirX: int = 1
		self.limit: int = 10

	def Move(self, direction: str):
		if direction == "left":
			self.dirX = -1	
		if direction == "right":
			self.dirX = 1
		self.x += self.speed * self.dirX
		if self.x >= self.limit:
			self.x = self.limit
		if self.x <= -self.limit:
			self.x = -self.limit
		
	def AddPoint(self):
		self.points += 1
		if self.points == 7:
			self.winner = True

	def GetName(self):
		return self.name


class Ball:
	def __init__(self):
		self.name: str = "ball"
		self.x: float = 0
		self.z: float = 0
		self.speed: float = 0.5
		self.SetNewDirection()

	def SetNewDirection(self):
		dirxList = [0.25, 0.5, -0.25, -0.5]
		dirzList = random.randint(0, 1)
		if dirzList == 0:
			self.dirZ = -1
		else:
			self.dirZ = 1
		self.dirX = random.choice(dirxList)

		magnitude = math.sqrt(self.dirX**2 + self.dirZ**2)
		if magnitude != 0:
			self.dirX /= magnitude
			self.dirZ /= magnitude

	def Move(self, player1: Player, player2: Player):
		self.x += self.speed * self.dirX
		self.z += self.speed * self.dirZ
		if self.x >= 14.5 or self.x <= -14.5:
			self.dirX *= -1
		if self.z <= -16:
			if player1.y < 0:
				player2.AddPoint()
			else:
				player1.AddPoint()
			self.z = 0
			self.x = 0

			self.SetNewDirection()

		if self.z >= 16:
			if player1.y > 0:
				player2.AddPoint()
			else:
				player1.AddPoint()
			self.z = 0
			self.x = 0
			
			self.SetNewDirection()

		if self.z <= -14.5:
			if player1.y < 0:
				if abs(self.x - player1.x <= 3):
					angle = (self.x - player1.x) / 3
					self.dirX = math.sin(angle)
					self.dirZ *= -1
			else:
				if abs(self.x - -player2.x) <= 3:
					angle = (self.x - -player2.x) / 3
					self.dirX = math.sin(angle)
					self.dirZ *= -1
		if self.z >= 14.5:
			if player1.y > 0:
				if abs(self.x - player1.x) <= 3:
					angle = (self.x - player1.x) / 3
					self.dirX = math.sin(angle)
					self.dirZ *= -1
			else:
				if abs(self.x - -player2.x) <= 3:
					angle = (self.x - -player2.x) / 3
					self.dirX = math.sin(angle)
					self.dirZ *= -1


class Games:
	def __init__(self, room: str):
		self.room = room
		self.player1 = Player()
		self.player2 = Player()
		self.ball = Ball()


class GameConsumer(AsyncWebsocketConsumer):
	games = []
	
	async def connect(self):
		self.room_name = self.scope['query_string'].decode().split('&')[0].split('=')[1]
		print("\n\nROOM_NAME: ", self.room_name, "\n\n")
		self.room_group_name = f'pong_{self.room_name}'

		mygame = False
		for game in self.games:
			if game.room == self.room_name:
				mygame = True
				if game.player1.GetName() == "" or game.player2.GetName() == "":
					if game.player1.GetName() == "":
						game.player1.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
						game.player1.y = 1
					else:
						game.player2.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
						game.player2.y = -1

		if not mygame:
			game = Games(self.room_name)
			self.games.append(game)

			if game.player1.GetName() == "" or game.player2.GetName() == "":
				if game.player1.GetName() == "":
					game.player1.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
					game.player1.y = 1
				else:
					game.player2.name = self.scope['query_string'].decode().split('&')[1].split('=')[1]
					game.player2.y = -1
		
		# Unirse al grupo de la sala
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name,
		)

		await self.accept()

		for game in self.games:
			if game.room == self.room_name:
				message = json.dumps(game.player1.__dict__) + "_" + json.dumps(game.player2.__dict__) + "_" + json.dumps(game.ball.__dict__)

				# Ejemplo: Enviar el mensaje recibido a todos en el grupo
				await self.send_group_message(message)


	async def disconnect(self, close_code):
		# Dejar el grupo de la sala
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name,
		)

	async def receive(self, text_data):
		data = json.loads(text_data)
		#if self.room_name == data["room"]:
		for game in self.games:
			if game.room == data["room"]:
				if "disconnect" == data["user"]:
					await self.disconnect(0)
				if game.player1.name == data["user"]:
					game.player1.Move(data["value"])
				if game.player2.name == data["user"]:
					game.player2.Move(data["value"])
				if data["user"] == "ball":
					game.ball.Move(game.player1, game.player2)
				message = json.dumps(game.player1.__dict__) + "_" + json.dumps(game.player2.__dict__) + "_" + json.dumps(game.ball.__dict__)
				if game.player1.points >= 7 or game.player2.points >= 7:
					del game
				# 	del game.player1
				# 	del game.player2
				# 	del game.ball
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