# For run this container:
# 1. In terminal execute command: docker build . -t app
# 2. When docker-container will be build execute: docker run -it -p 8000:8000 app


FROM python:3.9-buster

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn app:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000