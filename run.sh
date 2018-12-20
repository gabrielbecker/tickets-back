#!/bin/sh

umask 002

python /app/manage.py migrate
# python /app/manage.py collectstatic --noinput
pip install -r /app/requirements.txt

gunicorn --worker-class=$GUNICORN_WORKER_CLASS --workers=$GUNICORN_WORKER_COUNT --reload --log-level info --log-file=- --access-logfile=- blueticket.wsgi --chdir /app -b 0.0.0.0:$GUNICORN_PORT