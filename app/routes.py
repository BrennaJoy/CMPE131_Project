from app import myapp_obj
import sys
sys.path.append('app')
from users import add_new_user, search_for_user
from flask import render_template, redirect, flash
from app.forms import LoginForm, CreateUserForm, SearchForm, SendMessage

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    if current_form.username.data == "" or current_form.password.data == "":
        flash('ERROR: Empty input')
    a = 1
    name = 'Carlos'
    return render_template('login.html', name=name, a=a, form=current_form)

@myapp_obj.route('/SignUp', methods=['POST', 'GET'])
def signUp():
	current_form = CreateUserForm()
	if current_form.validate_on_submit():
		print(current_form.username.data, current_form.password.data, current_form.name.data,
			current_form.email.data)
		#Remove print statement later. For debugging purposes
		if add_new_user(current_form.name.data, current_form.username.data, current_form.password.data, current_form.email.data):
			flash('Welcome to Twitcher!')
		return redirect('/')
	if current_form.username.data == "" or current_form.password.data == "" or current_form.name.data == "" or current_form.email.data == "":
		flash('Please Enter All Criteria')
	return render_template('signup.html', form=current_form)

@myapp_obj.route('/search', methods=['POST', 'GET'])
def search():
	current_form = SearchForm()
	if current_form.validate_on_submit():
		username = current_form.username.data
		search_for_user(username)
		flash(current_form.username.data)
		#flash is placeholder. shows up regardless of if username is good
	return render_template('search.html', form=current_form)

@myapp_obj.route('/')
def home():
	return render_template('login.html')

@myapp_obj.route('/homepage')
def homepage():
	return render_template('homepage.html')

@myapp_obj.route('/send', methods=['POST', 'GET'])
def send():
    current_form = SendMessage()
    if current_form.validate_on_submit():
        flash('Message Sent: ' + current_form.message.data)
        print(current_form.message.data)
    return render_template('send.html', form=current_form)

