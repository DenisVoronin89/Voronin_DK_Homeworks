FROM --platform=linux/amd64/v8 tiangolo/uwsgi-nginx-flask:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app


# For run this container:
# 1. In terminal execute command: docker build . -t app
# 2. When docker-container will be build execute: docker run -it -p 8000:8000 app

