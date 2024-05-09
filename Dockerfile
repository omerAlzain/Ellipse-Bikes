# syntax=docker/dockerfile:1
FROM makinacorpus/geodjango:focal-3.8
#FROM faucet/python3:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python3 -m pip install -e . # So that the django-q2 scheduler can find the code