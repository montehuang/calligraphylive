#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password_hash = db.Column(db.String(128), unique = True, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def password(self):
        raise AttributeError('password is not readable!')
        
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key = True)  
    title = db.Column(db.String(15), unique = True, nullable = False)
    brief = db.Column(db.String(200), unique = True, nullable = False)

    def __repr__(self):
        return '<Theme %r>' % self.title

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))