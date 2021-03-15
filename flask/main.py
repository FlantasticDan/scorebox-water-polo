from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO, emit

from images import Logos
from manager import WaterPoloManager

VERSION = 'v0.0.1 (03152021)'
LOGOS = Logos()
MANAGER = None # WaterPoloManager

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet', logger=False, engineio_logger=False)

@app.route('/setup')
def setup():
    return render_template('setup.html', version=VERSION)

@app.route('/init', methods=['POST'])
def initialize():
    global LOGOS
    global MANAGER
    setup = request.form
    MANAGER = WaterPoloManager(**setup)
    files = request.files
    LOGOS.set_home(files['home_logo'].read(), files['home_logo'].filename)
    LOGOS.set_visitor(files['visitor_logo'].read(), files['visitor_logo'].filename)
    return 'OK'

@app.route('/home')
def home():
    global LOGOS
    output, mimetype = LOGOS.home()
    return send_file(output, mimetype=mimetype, as_attachment=False)

@app.route('/visitor')
def visitor():
    global LOGOS
    output, mimetype = LOGOS.visitor()
    return send_file(output, mimetype=mimetype, as_attachment=False)

@app.route('/overlay')
def overlay():
    global MANAGER
    if MANAGER:
        return render_template('overlay.html', **MANAGER.overlay_export())

@socketio.on('update')
def update(payload):
    return emit('update', payload, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=5000)