from flask import Flask, flash
import hashlib

user_dictionary = {}

class User:
	def __init__(self, name, username, password, email):
		self.post_history = None

		self.name = name
		self.username = username
		self.email = email
		self.hashed_password = hashlib.md5(password.encode())
		# Make sure that login page uses hashlib.md5(password.encode()) to
		# hash the passwords. Will compare to the same hash.

def add_new_user(name, username, password, email):
	if username not in user_dictionary.keys():
		new_user = User(name, username, password, email)
		if new_user.username.isalnum():
			user_dictionary[username] = new_user
			return True
		else:
			flash('Usernames must consist only of alphanumeric characters.')
			return False
	else:
		flash('This username already exists.')
		# The username already exists
		return False

def search_for_user(username):
	user_object = user_dictionary.get(username)
	if user_object is None:
		flash('No username found')
	elif username.isalnum() is False:
		flash('Please use alphanumeric characters')
	return user_object
