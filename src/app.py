from flask import Flask

from src.config import config
from src.extensions import register_extensions
from src.controllers import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_blueprints(app)

    return app


def create_worker_app():
    """Minimal App without routes for celery worker."""
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app, worker=True)

    return app
