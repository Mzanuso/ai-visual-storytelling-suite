import websocket
import json
import requests
import asyncio
from datetime import datetime

class DiscordService:
    def __init__(self, token):
        self.token = token
        self.ws = None
        self.session_id = None
        self.heartbeat_interval = None

    async def connect(self):
        """Connect to Discord gateway"""
        try:
            response = requests.get(
                'https://discord.com/api/v9/gateway',
                headers={'Authorization': self.token}
            )
            gateway_url = response.json()['url']
            
            self.ws = websocket.WebSocketApp(
                f'{gateway_url}/?v=9&encoding=json',
                on_message=self._on_message,
                on_error=self._on_error,
                on_close=self._on_close
            )
            return True
        except Exception as e:
            print(f'Connection error: {e}')
            return False

    async def send_command(self, command, channel_id):
        """Send command to Discord"""
        try:
            payload = {
                'content': command,
                'tts': False
            }
            
            response = requests.post(
                f'https://discord.com/api/v9/channels/{channel_id}/messages',
                headers={'Authorization': self.token},
                json=payload
            )
            return response.status_code == 200
        except Exception as e:
            print(f'Command error: {e}')
            return False