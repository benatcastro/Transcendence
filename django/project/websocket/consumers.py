import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class SomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")
        await self.accept()

    async def disconnect(self, close_code):
        print("WebSocket disconnected")

    async def receive(self, text_data):
        print(f"Server Supeer Andy hero SAMA message received: {text_data}")
        await self.send(text_data="You said: " + text_data)
