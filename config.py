import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLITE_DB = 'sqlite:///' + os.path.join(BASEDIR, 'db.sqlite')


class Config(object):
    DEBUG = False
    SECRET_KEY = 'bf0926d3-1fd6-4d26-bb79-fb845c'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', SQLITE_DB)

    CELERY_TIMEZONE = 'Europe/Berlin'
    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_SEND_TASK_SENT_EVENT = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost:3306/db'


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
