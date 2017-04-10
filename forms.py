from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, Length, EqualTo

from models import User

import logging

def email_exists(form, field):
    logging.debug(User.email)
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')

class RegisterForm(Form):
    email = StringField('Email',
                        validators=[
                                DataRequired(),
                                Email(),
                                email_exists
                            ])
    phone = StringField('Phone')


    password = PasswordField('Password',
                             validators=[
                                DataRequired(),
                                Length(min=1),
                                EqualTo('password2', message='Password must match.')
                            ])
    password2 = PasswordField('Confirm Password',
                              validators=[
                                DataRequired()
                            ])

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class chargeForm(Form):
    dname = StringField('Device Name', validators=[DataRequired()])
    emails = StringField('Email', validators=[DataRequired()])
    terms = BooleanField('Agree on the Terms and Condition', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
