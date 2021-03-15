from secrets import token_hex
from threading import Thread

import socketio

from consoles.sports import WaterPoloDaktronics

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

        self.client = socketio.Client()
        self.client_thread = Thread(target=self.socket_client)
        self.client_thread.start()

        self.console = WaterPoloDaktronics(com_port)
        self.console.on_update = self.updater
    
    def updater(self, game_state):
        if self.client.connected:
            self.client.emit('update', game_state)
        
    def socket_client(self):
        self.client.connect('http://localhost:5000')
        self.client.wait()
