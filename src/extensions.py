from celery import Celery
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
celery = Celery()


def register_extensions(app, worker=False):
    db.init_app(app)

    # load celery config
    celery.config_from_object(app.config)

    if not worker:
        # register celery irrelevant extensions
        pass
