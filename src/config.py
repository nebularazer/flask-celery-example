import os

BASEDIR = os.path.abspath(os.path.dirname(__name__))
SQLITE_DB = "sqlite:///" + os.path.join(BASEDIR, "db.sqlite")


class Config(object):
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16).hex())

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", SQLITE_DB)

    CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE", "Europe/Berlin")
    BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND", "redis://localhost:6379/0"
    )
    CELERY_SEND_SENT_EVENT = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:postgres@localhost:5432/celery"
    )


class ProductionConfig(Config):
    pass


# return active config
available_configs = dict(development=DevelopmentConfig, production=ProductionConfig)
selected_config = os.getenv("FLASK_ENV", "production")
config = available_configs.get(selected_config, "production")
