import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from flask import Flask, render_template
from flask_socketio import SocketIO
from PyQt5.QtCore import QRunnable


class MyFlaskApp:
    def __init__(self):
        self.flask_app = Flask(__name__, template_folder='static/html')
        self.flask_app.config['SECRET_KEY'] = 'mysecret'
        self.socketio = SocketIO(self.flask_app)

        @self.flask_app.route('/')
        def index():
            return render_template('index.html')

        @self.socketio.on('message')
        def handle_message(msg):
            print(f"Message from client: {msg}")
            self.socketio.send(f"Received: {msg}")


class FlaskThread(QRunnable):
    def __init__(self, socketio: SocketIO, flask_app: Flask):
        super().__init__()
        self.socketio = socketio
        self.flask_app = flask_app


    def run(self):
        self.socketio.run(self.flask_app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    my_flask_app = MyFlaskApp()

    threadPool = QtCore.QThreadPool()
    thread = FlaskThread(socketio=my_flask_app.socketio, flask_app=my_flask_app.flask_app)
    threadPool.start(thread)


    sys.exit(app.exec_())