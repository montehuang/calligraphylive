#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
