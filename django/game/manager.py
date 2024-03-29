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
		self.players = []
		self.status = []
		self.started = False
		self.add_player(owner)

	def add_player(self, username: str):
		if len(self.players) == 0:
			self.owner = username
		self.players.append(username)
		self.status.append(0)

	def get_players(self):
		return self.players

	def remove_player(self, username: str):
		for idx, player in enumerate(self.players):
			if player == username:
				self.status[idx] = -1
		self.players.remove(username)
		if not self.started:
			self.status.remove(-1)

	def set_status(self, username: str, n: int):
		for idx, player in enumerate(self.players):
			if player == username:
				self.status[idx] = n

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
		if data["type"] == "start_tournament":
			await self.start_tournaments(data["user"], data["t_name"])
		if data["type"] == "end_tournament":
			await self.end_tournaments(data["t_name"])
		if data["type"] == "find_match":
			await self.find_match(data["t_name"])
		if data["type"] == "set_status":
			await self.set_status(data["t_name"], data["user"], data["value"])
		if data["type"] == "disconnect":
			await self.leave_tournaments(data["user"], data["t_name"])
			await self.disconnect(0)

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
				tournament.add_player(user)
				return
		self.tournaments.append(Tournament(user, name))

	async def join_tournaments(self, user: str, name: str):
		if user == "" or name == "" or not user or not name:
			return
		for tournament in self.tournaments:
			if tournament.name == name and not tournament.players.__contains__(user):
				tournament.add_player(user)
				return

	async def leave_tournaments(self, user: str, name: str):
		for tournament in self.tournaments:
			if tournament.name == name and tournament.players.__contains__(user):
				for player in tournament.players:
					if player == user:
						tournament.remove_player(player)
				if tournament.owner == user and not tournament.started:
					self.tournaments.remove(tournament)
					del tournament
				return

	async def start_tournaments(self, user: str, name: str):
		for tournament in self.tournaments:
			if tournament.name == name and tournament.owner == user:
				tournament.started = True
				return

	async def end_tournaments(self, name: str):
		for tournament in self.tournaments:
			if tournament.name == name:
				self.tournaments.remove(tournament)
				del tournament
				return

	async def find_match(self, name: str):
		for tournament in self.tournaments:
			if tournament.name == name:
				p1: str = ""
				p2: str = ""
				for i, player in enumerate(tournament.players):
					if tournament.status[i] == 0:
						if p1 == "":
							p1 = player
						elif p1 != "" and p2 == "" and p1 != player:
							p2 = player
						if p1 != "" and p2 != "":
							await self.set_status(name, p1, 1)
							await self.set_status(name, p2, 1)
							await self.send_group_message(p1 + "_" + p2)
							p1 = ""
							p2 = ""

	async def set_status(self, name: str, user: str, value: int):
		for tournament in self.tournaments:
			if tournament.name == name:
				tournament.set_status(user, value)
