# flask-celery-example

An example to run flask with celery including:

- app factory setup
- periodic tasks with celery beat
- flask cli script for an ipython shell and url_map

# installation

## create virtualenv
```shell
python36 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## start redis backend (using docker)
```shell
docker run -d --name redis -p 6379:6379 redis
```

## run celery worker
```
celery -A celery_worker:celery worker --loglevel=DEBUG
```

## run celery beat for periodic tasks
```
celery -A celery_worker:celery beat --loglevel=INFO
```

## run flask app
```shell
env 'FLASK_APP=manage.py' flask run
```
