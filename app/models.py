#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    passwd = db.Column(db.String(120), unique = True, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username

class Theme(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(15), unique = True, nullable = False)
    brief = db.Column(db.String(200), unique = True, nullable = False)

    def __repr__(self):
        return '<Theme %r>' % self.title
