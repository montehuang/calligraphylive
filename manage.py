#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from app import create_app, db
from app.models import User, Theme
from flask_script import Manager
from flask_migrate import Migrate
import click

app = create_app('develop')

manager = Manager(app)
migrate = Migrate(app, db)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Theme=Theme)

if __name__ == '__main__':
    manager.run()
