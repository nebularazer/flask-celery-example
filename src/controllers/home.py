from datetime import datetime
from datetime import timedelta

from flask import url_for
from flask import Blueprint
from flask import jsonify

from src.extensions import db
from src.tasks.long_task import long_task

home = Blueprint("home", __name__)


@home.before_app_first_request
def init_db():
    db.create_all()


@home.route("/")
def index():
    """Add a new task and start running it after 10 seconds."""
    eta = datetime.utcnow() + timedelta(seconds=10)
    task = long_task.apply_async(eta=eta)
    return (
        jsonify(
            {"_links": {"task": url_for("status.get", task_id=task.id, _external=True)}}
        ),
        202,
    )
