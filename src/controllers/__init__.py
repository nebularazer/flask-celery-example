from flask import Flask

from .home import home
from .messages import messages
from .status import status


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(home)
    app.register_blueprint(messages)
    app.register_blueprint(status)
