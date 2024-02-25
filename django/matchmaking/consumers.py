# consumers.py
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from random import randint

casual_ids = []
ranked_ids = []

GenericNames1 = ["Gatita", "Capitan", "Tiburon", "Humano", "Alienigena", "Boss", "Dragon", "WatashiWa", "Mamut"]
GenericNames2 = ["Generico", "Sexy", "Badass", "Basado", "Magica", "Heteronormativo", "Ancestral", "Destroyer", "Fuerte"]
GenericNames3 = ["69", "XD", "10/10", "Lvl100", "Amateur", "Facha", "Random", "CSM", "Legendario", "AndyString"]


class MatchmakingConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        mode = data.get('mode')
        user_id = data.get('user') if mode == "ranked" else data.get('user') or str(GenericNames1[randint(0, len(GenericNames1) - 1)] + GenericNames2[randint(0, len(GenericNames2) - 1)] + GenericNames3[randint(0, len(GenericNames3) - 1)])

        # if mode == 'casual':
        #     ids = casual_ids
        # else:
        #     ids = ranked_ids

        # print("\n\n" + user_id + "\n\n" + mode + "\n\n" + text_data)
        # print(ids.count)

        if data['action'] == 'create':
            if mode == 'casual':
                if len(casual_ids) == 0 or user_id not in casual_ids:
                    casual_ids.append(user_id)
            if mode == 'ranked':
                if len(ranked_ids) == 0 or user_id not in ranked_ids:
                    ranked_ids.append(user_id)
            await self.send(text_data=json.dumps({"user": user_id}))

        elif data['action'] == 'search':
            if mode == 'casual':
                rival = next((i for i in casual_ids if i != user_id), None)
                if rival:
                    room = ""
                    if rival > user_id:
                        room = rival + "_" + user_id
                    else:
                        room = user_id + "_" + rival
                    await self.send(text_data=json.dumps({"rival": rival, "room": room}))
                    # break
            else:
                # TODO: Algoritmo de busqueda de partida ranked
                await asyncio.sleep(1)
            # while True:

        elif data['action'] == 'delete':
            if user_id in ids:
                ids.remove(user_id)

            await self.send(text_data=json.dumps({"status": "success"}))

        elif data['action'] == 'clear':
            ids.clear()
            await self.send(text_data=json.dumps({"status": "success"}))

        else:
            print("\n\nERROR\n\n")
