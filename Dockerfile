FROM python:3.7.6-buster
MAINTAINER python_student

RUN mkdir /SLCMS/
COPY ./requirements.txt /SLCMS/
COPY ./wsgi.py ./wsgi.py

RUN pip3 install --upgrade pip
RUN pip3 install -r /SLCMS/requirements.txt

WORKDIR /SLCMS/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true
