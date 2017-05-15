class Config(object):
    DEBUG = False
    SECRET_KEY = 'bf0926d3-1fd6-4d26-bb79-fb845c'

    CELERY_TIMEZONE = 'Europe/Berlin'
    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_SEND_TASK_SENT_EVENT = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
