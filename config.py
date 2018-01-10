class Config(object):
    @staticmethod
    def init_app():
        pass

class DevelopConfig(Config):
    DEBUG = True
    SECRET_KEY = 'Monte Live key'

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'Monte Live testing key'

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'Monte live production key'

config = {
    'develop' : DevelopConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
}
