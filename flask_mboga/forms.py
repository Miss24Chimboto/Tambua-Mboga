from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    """creating  registration form """
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(),
                         Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                             Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                     EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    """creating the login form"""
    email = StringField('Email', validators=[DataRequired(),
                         Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                             Length(min=8)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
