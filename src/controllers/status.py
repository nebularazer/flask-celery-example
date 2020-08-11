from flask import jsonify
from flask import Blueprint
from celery.result import AsyncResult

status = Blueprint("status", __name__, url_prefix="/status")


@status.route("/<task_id>/", methods=["GET"])
def get(task_id):
    task = AsyncResult(task_id)
    if task.state == "PENDING":
        # job did not start yet
        response = {"state": task.state, "status": "Pending..."}
    elif task.state != "FAILURE":
        response = {
            "state": task.state,
            "current": task.info.get("current", 0),
            "total": task.info.get("total", 1),
            "status": task.info.get("status", ""),
        }
        if "result" in task.info:
            response["result"] = task.info["result"]
    else:
        # something went wrong in the background job
        response = {
            "state": task.state,
            "current": 1,
            "total": 1,
            "status": str(task.info),  # this is the exception raised
        }
    return jsonify(response)
