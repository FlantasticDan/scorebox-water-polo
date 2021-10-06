from secrets import token_hex
from threading import Thread
from typing import Dict

import socketio
import httpx

from consoles.sports import WaterPolo, WaterPoloDaktronics

def is_string_ip(string: str) -> bool:
    octets = string.split('.')
    return len(octets) == 4

class WaterPoloManager:
    '''Water Polo Game State Manager'''
    def __init__(self, home_team, home_mascot, home_color, visitor_team, visitor_mascot, visitor_color, com_port) -> None:
        self.nonce = token_hex(6)

        self.home_name = home_team
        self.home_mascot = home_mascot
        self.home_color = home_color
        self.visitor_name = visitor_team
        self.visitor_mascot = visitor_mascot
        self.visitor_color = visitor_color

        self.remote = is_string_ip(com_port)
        self.source = com_port

        if not self.remote:
            self.client = socketio.Client()
            self.client_thread = Thread(target=self.socket_client)
            self.client_thread.start()

            self.console = WaterPolo(com_port)
            self.console.on_update = self.updater

        else:
            httpx.get(f'http://{self.source}:9876/init/waterpolo')
    
    def updater(self, game_state):
        if self.client.connected:
            self.client.emit('update', game_state)
        
    def socket_client(self):
        self.client.connect('http://localhost:5000')
        self.client.wait()

    def overlay_export(self) -> Dict:
        return {
            'home_name': self.home_name,
            'home_mascot': self.home_mascot,
            'home_color': self.home_color,
            'visitor_name': self.visitor_name,
            'visitor_mascot': self.visitor_mascot,
            'visitor_color': self.visitor_color,
        }