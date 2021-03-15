from flask import Flask, render_template, request, send_file
from flask_socketio import SocketIO

from consoles.sports import WaterPoloDaktronics

from images import Logos

VERSION = 'v0.0.1 (03142021)'
LOGOS = Logos()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@app.route('/setup')
def setup():
    return render_template('setup.html', version=VERSION)

@app.route('/init', methods=['POST'])
def initialize():
    global LOGOS
    setup = request.form
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
    return render_template('overlay.html')

if __name__ == '__main__':
    socketio.run(app)