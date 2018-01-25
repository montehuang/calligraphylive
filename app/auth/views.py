#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from . import auth
from .. import db
from flask_login import login_user, login_required, logout_user
from flask import render_template, redirect, request, url_for, flash
from ..models import User, Theme
from .forms import LoginForm, RegisterForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('Invalid username or password!')
	return render_template('auth/login.html', form = form)

@auth.route('/register', methods=['GET', 'POST'])	
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
			username=form.username.data,
			password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Register success, You can login now')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))