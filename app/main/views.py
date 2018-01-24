#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from . import main
from ..models import User, Theme
from flask import render_template

@main.route('/')
def index():
	themes = Theme.query.all()
	return render_template('index.html', themes = themes)	
	