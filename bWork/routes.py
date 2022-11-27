from bWork import myapp_obj
from flask import render_template, redirect, flash
from bWork.forms import LoginForm, CreateUserForm

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
		flash('Welcome to Twitcher!')
		print(current_form.username.data, current_form.password.data, current_form.name.data,
			current_form.email.data)
		return redirect('/')
	if current_form.username.data == "" or current_form.password.data == "" or current_form.name.data == "" or current_form.email.data == "":
		flash('Please Enter All Criteria')
	return render_template('signup.html', form=current_form)

@myapp_obj.route('/')
def home():
    return render_template('base.html')

