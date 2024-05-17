import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from flask import Flask, render_template
from flask_socketio import SocketIO
from PyQt5.QtCore import QRunnable


class MyFlaskApp:

    class FlaskThread(QRunnable):
        def __init__(self, socketio: SocketIO, flask_app: Flask, port: int):
            super().__init__()
            self.socketio = socketio
            self.flask_app = flask_app
            self.port = port
            self.setAutoDelete(True)

        def run(self):
            self.socketio.run(self.flask_app, host='0.0.0.0', port=self.port, allow_unsafe_werkzeug=True, debug=False)


    def __init__(self, port: int):
        self.flask_app = Flask(__name__, template_folder='static/html')
        self.flask_app.config['SECRET_KEY'] = 'mysecret'
        self.flask_app.config['TEMPLATES_AUTO_RELOAD'] = True
        self.socketio = SocketIO(self.flask_app)
        self.callbacks = {}
        self.thread = self.FlaskThread(socketio=self.socketio, flask_app=self.flask_app, port=port)

        @self.flask_app.route('/')
        def index():
            return render_template('index.html')

        @self.socketio.on('message')
        def handle_message(msg):
            print(f"Message from client: {msg}")
            if msg in self.callbacks.keys():
                self.callbacks[msg]()
            else:
                print("No callback registered")

    def register_callback(self, message: str, function):
        self.callbacks[message] = function




if __name__ == "__main__":
    app = QApplication(sys.argv)

    my_flask_app = MyFlaskApp(port=5000)
    my_flask_app.register_callback(message="goal_home_plus", function=lambda: print('callback for: goal_home_plus'))
    threadPool = QtCore.QThreadPool()
    threadPool.start(my_flask_app.thread)

    sys.exit(app.exec_())
