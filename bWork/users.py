from flask import Flask

user_dictionary = {}


class Users:
	def __init__(self, name, username, password, email):
		self.post_history = None
		
		self.name = name
		self.username = username
		self.email = email
		#self.hashed_password = temp_has(password)

def add_new_user(name, use
