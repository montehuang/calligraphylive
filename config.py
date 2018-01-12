#!/home/monte/webdev/venv/bin/python
# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    @staticmethod
    def init_app():
        pass

class DevelopConfig(Config):
    DEBUG = True
    SECRET_KEY = 'Monte Live key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                          'live.db')

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'Monte Live testing key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                          'live.db')

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'Monte live production key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'develop' : DevelopConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
}
