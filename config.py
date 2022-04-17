"""Flask configuration
Remember to export the following variables tothe GLOBAL ENV in terminal 
export SESSION_COOKIE_NAME
export SECRET_KEY
export PROD_DATABASE_URI
export DEV_DATABASE_URI
export SQLALCHEMY_DATABASE_URI
"""
from os import environ, path, getenv
from dotenv import load_dotenv
from flask_login import LoginManager

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config():
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('AWS_HOST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    host = getenv('AWS_HOST')
    user = getenv('AWS_USER')
    # RBAC_USE_WHITE = True
    RECAPTCHA_PRIVATE_KEY = getenv('GOOGLE_RECAPTCHA_PRIVATE_KEY')
    TESTING = True
    RECAPTCHA_PUBLIC_KEY=getenv('GOOGLE_RECAPTCHA_SITE_KEY')
    TESTING = True
