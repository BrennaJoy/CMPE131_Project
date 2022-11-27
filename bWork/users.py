from flask import Flask, flash

user_dictionary = {}

class User:
	def __init__(self, name, username, password, email):
		self.post_history = None

		self.name = name
		self.username = username
		self.email = email
		#self.hashed_password = temp_has(password)

def add_new_user(name, username, password, email):
	if username not in user_dictionary.keys():
		new_user = User(name, username, password, email)
		user_dictionary[username] = new_user
		return True
	else:
		flash('This username already exists.')
		# The username already exists
		return False

