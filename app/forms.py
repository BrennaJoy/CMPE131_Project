from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

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
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=0, max=50)])
    submit = SubmitField('Send')

