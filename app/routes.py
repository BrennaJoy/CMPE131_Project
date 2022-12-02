from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm, SendMessage

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


@myapp_obj.route('/')
def home():
    return render_template('base.html')

@myapp_obj.route('/send', methods=['POST', 'GET'])
def send():
    current_form = SendMessage()
    if current_form.validate_on_submit():
        flash('Message Sent: ' + current_form.message.data)
        print(current_form.message.data)
    return render_template('send.html', form=current_form)