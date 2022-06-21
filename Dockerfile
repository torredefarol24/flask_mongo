# syntax=docker/dockerfile:1.2
FROM python:3.8-slim-buster

WORKDIR /usr/app/src

ENV FLASK_APP=server.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 27017

CMD [ "python", "-m" , "flask", "run", "--host=172.30.1.1", "--port=6161"]