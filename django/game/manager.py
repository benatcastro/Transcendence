## tournament/manager.py
import asyncio
import random
import math
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class Tournament:
	def __init__(self, owner: str, name: str):
		self.owner: str = owner
		self.name: str = name
		self.players = [self.owner]
		self.started = False

	def add_player(self, username: str):
		if len(self.players) == 0:
			self.owner = username
			self.players.append(username)

	def get_players(self):
		return self.players

	def remove_player(self, username: str):
		self.players.remove(username)


class TournamentManager(AsyncWebsocketConsumer):

	tournaments = []

	async def connect(self):
		self.room_group_name = 'Tournament'

		# Unirse al grupo de la sala
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name,
		)

		await self.accept()

		# message = "Connected to group " + self.room_group_name

		# Ejemplo: Enviar el mensaje recibido a todos en el grupo
		# await self.send_group_message(message)

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name,
		)

	async def receive(self, text_data):
		data = json.loads(text_data)
		if data["type"] == "get_tournament":
			await self.send(text_data=f'{ json.dumps(await self.get_tournaments())}')
			return
		if data["type"] == "create_tournament":
			await self.create_tournaments(data["user"], data["t_name"])
		if data["type"] == "join_tournament":
			await self.join_tournaments(data["user"], data["t_name"])
		if data["type"] == "leave_tournament":
			await self.leave_tournaments(data["user"], data["t_name"])

		await self.send_group_message(json.dumps(await self.get_tournaments()))

	# self.receive(text_data)

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
		await self.send(text_data=f'{message}')

	async def get_tournaments(self):
		tournaments_names = []
		for tournament in self.tournaments:
			tournaments_names.append(tournament.__dict__)
		return tournaments_names

	async def create_tournaments(self, user: str, name: str):
		for tournament in self.tournaments:
			if tournament.name == name:
				return
		self.tournaments.append(Tournament(user, name))

	async def join_tournaments(self, user: str, name: str):
		for tournament in self.tournaments:
			if tournament.name == name and not tournament.players.__contains__(user):
				tournament.players.append(user)
				return

	async def leave_tournaments(self, user: str, name: str):
		for tournament in self.tournaments:
			if tournament.name == name and tournament.players.__contains__(user):
				tournament.players.remove(user)
				if tournament.owner == name:
					self.tournaments.remove(tournament)
				return
