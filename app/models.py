from app import db, myapp_obj
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class Users(db.Model, UserMixin):

    # List to store private messages of the user.
    messages = []

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(32), unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password 
        self.email = email

        # Append a tuple containing (name of sender, message they send) to this user's messages list.
    def add_message(self, timestamp, sender, message, image):
        self.messages.append((timestamp, sender, message, image))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.username}>'

@myapp_obj.before_first_request
def create_tables():
     db.create_all()

@login.user_loader
def load_user(id):
    return Users.query.get(id)

def add_usr(usr):
    u = Users(usr.username, usr.password, usr.email)
    db.session.add(u)
    db.session.commit()

def remove_usr(usr):
    db.session.delete(usr)
    db.session.commit()


