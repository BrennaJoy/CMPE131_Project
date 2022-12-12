from app import myapp_obj
import sys
sys.path.append('app')
from users import add_new_user, search_for_user, remove_user
from flask import render_template, redirect, flash, request
from app.forms import LoginForm, CreateUserForm, SearchForm, SendMessage, DeleteConfirm
import datetime 
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.join( os.getcwd(), 'images')
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
		return redirect('/homepage')
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

# Private messaging form, allows user to send message to another user. This page also displays any messages 
# that this current user has received. 
# IMPORTANT: As of now, there is no way to verify current logged in user, so the only way to view sent messages
# is to send messages to 'JohnDoe', this also means that an account with the username 'JohnDoe' has to be created 
# and added to the database first. 
@myapp_obj.route('/send', methods=['POST', 'GET'])
def send():
    # SendMessage form
    print("using send message")
    current_form = SendMessage()
    user_messages = []
    # Check if the user exists and send the user's messages list to the template to display it.
    if (search_for_user("JohnDoe") != None):
        user_messages = search_for_user("JohnDoe").messages # JohnDoe is temporary.
    # On form submission, check if the receiever user exist, otherwise prompt the sender to enter the correct username.
    if current_form.validate_on_submit():
        if (search_for_user(current_form.receiver.data) == None):
            flash('Please make sure you entered the correct username.')
        # Search for a user and add the sender's message to their messages list.
        else:
            receiver_user = search_for_user(current_form.receiver.data)
            time = datetime.datetime.now().strftime("[%d/%m/%Y-%H:%M:%S] ")
            # Sender name 'JohnDoe' is temporary, will replace with sender username.
            # deal with sending photos
            print(request.files)
            if 'file' in request.files:
                file = request.files['file']
                sec_filename = secure_filename(file.filename)
                file.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], sec_filename))
                print(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], sec_filename))
            else:
                sec_filename = None
            receiver_user.add_message(' ' + time, 'JohnDoe', ': ' + current_form.message.data, sec_filename)          
            flash('Sent: ' + current_form.message.data + ' to ' + current_form.receiver.data)
    return render_template('send.html', form=current_form, msg=user_messages)

# Account deletion confirmation page, delete user from database if they submit the form.
@myapp_obj.route('/deleteconfirm', methods=['POST', 'GET'])
def deleteconfirm():
    current_form = DeleteConfirm()
    # Remove user from database if confirm button is clicked.
    if current_form.validate_on_submit():
        name = current_form.username.data
        # JohnDoe is temporary, will replace with a way to get the currently logged in user.
        remove_user(name)
        # Redirect to homepage after account deletion.
        return redirect("/")
    return render_template('deleteconfirm.html', form = current_form)

# When user presses a 'reaction' button on a message from /send, this route will process the reaction 
# and send the reaction as a message to the other user. Send thumbs up emoji.
@myapp_obj.route('/processreaction1', methods=['POST'])
def processreaction1():
    sender = request.form['sender']
    message = request.form['message']

    if (search_for_user(sender) == None):
        return redirect('/send')
    else:
        time = datetime.datetime.now().strftime("[%d/%m/%Y-%H:%M:%S] ")
        receiver_user = search_for_user(sender)
        receiver_user.add_message(' ' + time, 'Test React', ": (\"" + message + "\") " + "👍", None)                            
        return redirect('/send')


# When user presses a 'reaction' button on a message from /send, this route will process the reaction 
# and send the reaction as a message to the other user. Send thumbs down emoji.
@myapp_obj.route('/processreaction2', methods=['POST'])
def processreaction2():
    sender = request.form['sender']
    message = request.form['message']

    if (search_for_user(sender) == None):
        return redirect('/send')
    else:
        time = datetime.datetime.now().strftime("[%d/%m/%Y-%H:%M:%S] ")
        receiver_user = search_for_user(sender)
        receiver_user.add_message(' ' + time, 'Test React', ": (\"" + message + "\") " + "👎", None)                            
        return redirect('/send')





