from flask_login import login_user, logout_user, user_logged_in, login_required, current_user
from app import myapp_obj
import sys
from app.models import Users
sys.path.append('app')
from users import add_new_user, search_for_user, remove_user
from flask import render_template, redirect, flash, request, url_for
from app.forms import LoginForm, CreateUserForm, SearchForm, SendMessage, DeleteConfirm
import datetime 
from werkzeug.utils import secure_filename
import os

# folders for our uploadable images
UPLOAD_FOLDER = os.path.join( os.getcwd(), 'app/static')
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
myapp_obj._static_folder = UPLOAD_FOLDER

@myapp_obj.route('/')
def home():
    return render_template('base.html')

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = Users.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or user.password != current_form.password.data:
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        print(current_form.username.data, current_form.password.data)
        return redirect('/homepage')

    return render_template('login.html', form=current_form)
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
@login_required 
def search():
	current_form = SearchForm()
	if current_form.validate_on_submit():
		username = current_form.username.data
		search_for_user(username)
		flash(current_form.username.data)
		#flash is placeholder. shows up regardless of if username is good
	return render_template('search.html', form=current_form)

@myapp_obj.route('/homepage')
@login_required
def homepage():
	return render_template('homepage.html')

# Private messaging form, allows user to send message to another user. This page also displays any messages 
# that this current user has received. 
@myapp_obj.route('/send', methods=['POST', 'GET'])
@login_required
def send():
    # SendMessage form
    print("using send message")
    current_form = SendMessage()
    user_messages = []
    # Check if the user exists and send the user's messages list to the template to display it.
    if (search_for_user(current_user.username) != None):
        user_messages = search_for_user(current_user.username).messages 
    # On form submission, check if the receiever user exist, otherwise prompt the sender to enter the correct username.
    if current_form.validate_on_submit():
        if (search_for_user(current_form.receiver.data) == None):
            flash('Please make sure you entered the correct username.')
        # Search for a user and add the sender's message to their messages list.
        else:
            receiver_user = search_for_user(current_form.receiver.data)
            time = datetime.datetime.now().strftime("[%d/%m/%Y-%H:%M:%S] ")
            # deal with sending photos
            print(request.files)
            if 'file' in request.files:
                file = request.files['file']
                sec_filename = secure_filename(file.filename)
                full_filename = os.path.join(myapp_obj.config['UPLOAD_FOLDER'], sec_filename)
            else:
                sec_filename = None
                
            receiver_user.add_message(' ' + time, current_user.username, ': ' + current_form.message.data, sec_filename)          
            flash('Sent: ' + current_form.message.data + ' to ' + current_form.receiver.data)       
    return render_template('send.html', form=current_form, msg=user_messages)

# Account deletion confirmation page, delete user from database if they submit the form.
@myapp_obj.route('/deleteconfirm', methods=['POST', 'GET'])
@login_required
def deleteconfirm():
    current_form = DeleteConfirm()
    # Remove user from database if confirm button is clicked.
    if current_form.validate_on_submit():
        name = current_user.username
        logout_user()
        remove_user(name)
        # Redirect to homepage after account deletion.
        return redirect("/")
    return render_template('deleteconfirm.html', form = current_form)

# When user presses a 'reaction' button on a message from /send, this route will process the reaction 
# and send the reaction as a message to the other user. Send thumbs up emoji.
@myapp_obj.route('/processreaction1', methods=['POST'])
@login_required
def processreaction1():
    sender = request.form['sender']
    message = request.form['message']

    if (search_for_user(sender) == None):
        return redirect('/send')
    else:
        time = datetime.datetime.now().strftime("[%d/%m/%Y-%H:%M:%S] ")
        receiver_user = search_for_user(sender)
        receiver_user.add_message(' ' + time, current_user.username, ": (\"" + message + "\") " + "👍", None)                            
        return redirect('/send')


# When user presses a 'reaction' button on a message from /send, this route will process the reaction 
# and send the reaction as a message to the other user. Send thumbs down emoji.
@myapp_obj.route('/processreaction2', methods=['POST'])
@login_required
def processreaction2():
    sender = request.form['sender']
    message = request.form['message']

    if (search_for_user(sender) == None):
        return redirect('/send')
    else:
        time = datetime.datetime.now().strftime("[%d/%m/%Y-%H:%M:%S] ")
        receiver_user = search_for_user(sender)
        receiver_user.add_message(' ' + time, current_user.username, ": (\"" + message + "\") " + "👎", None)                            
        return redirect('/send')

@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

## User prfoile page
@myapp_obj.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': ''},
    ]
    return render_template('Userprofile.html', user=user, posts=posts)

## Edit profile
@myapp_obj.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)
