from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import emit
    
app = Flask(__name__)
socketio = SocketIO(app)
print('Starting Server....')
@app.route('/')
def index():
    return render_template('index.html')

@socketio.event
def windowdisplaEvent(RxData):
    socketio.emit('Web_windowdisplayEvent', RxData)
    print('Receive Data from windowdisplay')

@socketio.event
def motionEvent(RxData):
    socketio.emit('Web_motionEvent', RxData)
    print('Receive Data from motion')

@socketio.event
def windowdetectEvent(RxData):
    socketio.emit('Web_windowdetectEvent', RxData)
    print('Receive Data from windowdetect')

if __name__ == '__main__':
    app.run(host='192.168.1.167')
