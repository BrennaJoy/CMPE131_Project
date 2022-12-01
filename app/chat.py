from app import socketio
from flask_socketio import SocketIO, send, emit, join_room, leave_room

@socketio.on('message')
def send_chat(message):
	print("Message sent: " + message)
	send('message', broadcast = True)

@socketio.on('join')
def user_join(user):
	emit('User joined')

@socketio.on('leave')
def user_leave(user):
	emit('User left')