from flask import Flask, render_template, request
from flask_socketio import SocketIO

from consoles.sports import WaterPoloDaktronics

VERSION = 'v0.0.1 (03142021)'

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/overlay')
def overlay():
    return render_template('overlay.html')

if __name__ == '__main__':
    socketio.run(app)