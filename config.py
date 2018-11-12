import os
basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES = {
    'user': 'migiwara',
     'pw': 'root',
    'db': 'BiosensorsServer',
    'host': 'localhost',
    'port': '5432',
}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
# %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'changedSecretKey'
    SQLALCHEMY_DATABASE_URI = os.environ['postgresql://%(db)s' % POSTGRES]


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True