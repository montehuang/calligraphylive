#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
from app import create_app

app = create_app('develop')

if __name__ == '__main__':
    app.run()
