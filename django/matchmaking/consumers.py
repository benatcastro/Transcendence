# consumers.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint

casual_ids = []
ranked_ids = []

class MatchmakingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("estoy dentro")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        mode = data.get('mode')
        user_id = data.get('user') if mode == "ranked" else data.get('user') or str(randint(1000, 9999))

        if mode == 'casual':
            ids = casual_ids
        else:
            ids = ranked_ids

        if data['action'] == 'create':
            if len(ids) == 0 or user_id not in ids:
                ids.append(user_id)

            await self.send(text_data=json.dumps({"user": user_id}))

        elif data['action'] == 'search':
            while True:
                if mode == 'casual':
                    rival = next((i for i in ids if i != user_id), None)
                    if rival:
                        await self.send(text_data=json.dumps({"rival": rival}))
                        break
                else:
                    # TODO: Algoritmo de bÃºsqueda de partida ranked
                    await asyncio.sleep(1)

        elif data['action'] == 'delete':
            if user_id in ids:
                ids.remove(user_id)

            await self.send(text_data=json.dumps({"status": "success"}))

        elif data['action'] == 'clear':
            ids.clear()
            await self.send(text_data=json.dumps({"status": "success"}))