from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    submit = SubmitField('Create User')

class SearchForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	submit = SubmitField('Search')

class SendMessage(FlaskForm):
    receiver = StringField('Send to:', validators = [DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=0, max=150)])
    submit = SubmitField('Send')

class DeleteConfirm(FlaskForm):
    submit = SubmitField('Confirm')

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    author = StringField('Author', validators = [DataRequired()])
    submit = SubmitField('Submit:')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class postmssgform(FlaskForm):
	text = TextAreaField('Enter a message')
	post = SubmitField('Post the message !')
