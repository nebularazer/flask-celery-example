from flask import Blueprint
from flask import jsonify

from src.extensions import db
from src.models.message import Message

messages = Blueprint("messages", __name__, url_prefix="/messages")


@messages.route("/")
def index():
    messages = Message.query.all()
    if not messages:
        message = Message(text="Hello World")
        db.session.add(message)
        db.session.commit()
        messages.append(message)

    return jsonify([message.text for message in messages])
