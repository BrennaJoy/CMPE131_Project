from flask import Flask, flash
from app.models import Users, add_usr, remove_usr

user_dictionary = {}

class User:

	def __init__(self, name, username, password, email):
		self.post_history = None

		self.name = name
		self.username = username
		self.email = email
		self.password = password

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
	if (search_for_user(username) != None):
		user = search_for_user(username)
		name = user.username
		remove_usr(user)
		print(name + ' has been deleted.')
	else:
		flash('User does not exist.')


