from flask import Flask
from flask_socketio import SocketIO

myapp_obj = Flask(__name__)

myapp_obj.config.update(
    SECRET_KEY='this-is-a-secret'
)

socketio = SocketIO(myapp_obj)


from app import routes

from app import chat







    


