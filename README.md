# flask-celery-example

An example to run flask with celery including:

- app factory setup
- send a long running task from flask app
- send periodic tasks with celery beat

based on [flask-celery-example by Miguel Grinberg](https://github.com/miguelgrinberg/flask-celery-example) and his [bloc article](http://blog.miguelgrinberg.com/post/using-celery-with-flask)


# endpoints
- / adds a task to the queue and schedule it to start in 10 seconds
- /message - shows messages in the database (revered every 10 seconds by celery task)
- /status/<task_id> - show the status of the long running task


# installation

## install dependencies with [poetry](https://python-poetry.org/)
``` bash
poetry install
poetry shell
```

## start redis backend (using docker)
``` bash
docker run -d --name redis -p 6379:6379 redis
```

## run celery worker
```
source .env
celery -A src.worker:celery worker --loglevel=DEBUG
```

## run celery beat for periodic tasks
```
source .env
celery -A src.worker:celery beat --loglevel=INFO
```

## run flask app
``` bash
source .env
# check the available routes
flask routes
# start flask development server
flask run
```
