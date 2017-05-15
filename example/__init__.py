import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

from config import config

celery = Celery()
db = SQLAlchemy()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('CONFIG', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    celery.config_from_object(app.config)

    db.init_app(app)

    from example.views import home
    app.register_blueprint(home)

    return app
