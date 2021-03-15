from secrets import token_hex

from flask_socketio import SocketIO
from consoles.sports import WaterPoloDaktronics

class WaterPoloManager:
    '''Water Polo Game State Manager'''
    def __init__(self, socketio: SocketIO, home_team, home_mascot, home_color, visitor_team, visitor_mascot, visitor_color, com_port) -> None:
        self.socketio = socketio

        self.home_name = home_team
        self.home_mascot = home_mascot
        self.home_color = home_color
        self.visitor_name = visitor_team
        self.visitor_mascot = visitor_mascot
        self.visitor_color = visitor_color

        self.console = WaterPoloDaktronics(com_port)
        self.console.on_update = self.updater
    
        self.nonce = token_hex(6)
    
    def updater(self, game_state):
        pass

