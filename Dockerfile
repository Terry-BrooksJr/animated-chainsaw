# syntax=docker/dockerfile:1

FROM python:3.7.6-buster

WORKDIR /app


COPY requirements.txt requirements.txt 

RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE=true
ENV SESSION_COOKIE_NAME=':?sjvrA8"u&=P88e'
ENV SECRET_KEY='6xQ3ZvFf(HP,#zP2'
ENV AWS_db_HOST='ls-1f93c81433121e3e0e6e4d94c74e5c45e2223926.c5brfcn0ty5g.us-east-2.rds.amazonaws.com'
ENV AWS_db_USER='terrybrooksjr'
ENV AWS_db_PASSWORD='Qu33nLady!'
ENV GOOGLE_RECAPTCHA_SECRET_KEY='6Le6n30fAAAAAHKYHH99ypINCaKRHnnzr6yfallV'
ENV GOOGLE_RECAPTCHA_SITE_KEY='6Le6n30fAAAAALzbo2fp0Kts8H0CUA97YXjlmrv9'
LABEL "com.BrooksJr.SLCSM"="Safari Life CSM Image"