FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN chown -R :0 /app && \
    chmod -R g+rwx /app && \
    pip install --upgrade pip && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r /app/requirements.txt && \
    apk --purge del .build-deps


ARG arg_revision=''
ARG arg_build_date=''

ENV GUNICORN_WORKER_CLASS=sync \
    GUNICORN_WORKER_COUNT=4 \
    GUNICORN_PORT=6600 \
    REVISION=$arg_revision \
    BUILD_DATE=$arg_build_date

EXPOSE $GUNICORN_PORT

CMD ["/app/run.sh"]