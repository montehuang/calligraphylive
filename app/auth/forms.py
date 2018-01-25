#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
class LoginForm(FlaskForm):
	email = StringField('Email', validators = [Required(), Length(1,64), Email()])
	password = PasswordField('password', validators = [Required()])
	submit = SubmitField('login')

class RegisterForm(FlaskForm):
	email = StringField('Email', validators = [Required(), Length(1,64), Email()])
	username = StringField('UserName', validators = [Required(), Length(6, 80), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'User name must use letter,number,dot,underline!')])
	password = PasswordField('password', validators = [Required(), EqualTo('password2', 'passwords must match!')])
	password2 = PasswordField('confirm password', validators = [Required()])
	submit = SubmitField('register')
	