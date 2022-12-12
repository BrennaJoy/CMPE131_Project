from flask import Flask, flash
from app.models import Users, add_usr
import hashlib

user_dictionary = {}

class User:

	def __init__(self, name, username, password, email):
		self.post_history = None

		self.name = name
		self.username = username
		self.email = email
		self.password = password
		# Make sure that login page uses hashlib.md5(password.encode()) to
		# hash the passwords. Will compare to the same hash.

def add_new_user(name, usrn, password, email):
	user_object = Users.query.filter_by(username = usrn).first()
	if user_object is None:
		new_user = User(name, usrn, password, email)
		if new_user.username.isalnum():
			add_usr(new_user)
			return True
		else:
			flash('Usernames must consist only of alphanumeric characters.')
			return False
	else:
		flash('This username already exists.')
		# The username already exists
		return False

def search_for_user(usr):
	user_object = Users.query.filter_by(username=usr).first()
	if user_object is None:
		flash('No username found')
	return user_object

def remove_user(username):
	# Check if user exists in database before removing them from it.
	# Will also need to check if they are currently logged in.
	if (user_dictionary.get(username) != None):
		name = user_dictionary.get(username).username
		user_dictionary.pop(username)
		print(name + ' has been deleted.')
	else:
		flash('User does not exist.')


