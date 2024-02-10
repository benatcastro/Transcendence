## tournament/manager.py
import asyncio
import random
import math
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class Tournament:
	def __init__(self):
		self.owner: str = "Default"
		self.name: str = "Default"
		self.players = [self.owner]

	def add_player(self, username: str):
		if len(self.players) == 0:
			self.owner = username
			self.players.append(username)

	def get_players(self):
		return self.players

	def remove_player(self, username: str):
		self.players.remove(username)


class TournamentManager(AsyncWebsocketConsumer):

	tournaments: Tournament = []

	async def connect(self):
		self.room_group_name = 'Tournament'

		# Unirse al grupo de la sala
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name,
		)

		await self.accept()

		message = "Connected to group " + self.room_group_name

		# Ejemplo: Enviar el mensaje recibido a todos en el grupo
		await self.send_group_message(message)

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name,
		)

	async def receive(self, text_data):

		message = "Send response"
		if text_data == "get_tournaments":
			message = self.get_tournaments()
			await self.send(text_data=f'{message}')
			return

		await self.send_group_message(message)

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

	def get_tournaments(self):
		tournaments_names: str = []
		for tournament in self.tournaments:
			tournaments_names.__add__(tournament.name)
		return tournaments_names

	# def create_tournaments(self, user: str, name: str):
	# 	self.tournaments.a