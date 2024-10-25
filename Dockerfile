FROM python:3.11


ENV PYTHONWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .
