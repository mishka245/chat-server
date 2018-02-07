from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("/index/index.html")

@socketio.on("my event")
def handler(data):
    print(data)
    socketio.emit("my response", data)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

