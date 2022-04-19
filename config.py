"""Flask configuration
Remember to export the following variables tothe GLOBAL ENV in terminal 
export SESSION_COOKIE_NAME
export SECRET_KEY
export PROD_DATABASE_URI
export DEV_DATABASE_URI
export SQLALCHEMY_DATABASE_URI
"""
from decouple import config
from dotenv import load_dotenv
from os import path
from flask_login import LoginManager

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config():
    """Base config."""
    SECRET_KEY = config('SECRET_KEY')
    SESSION_COOKIE_NAME = config('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = config('AWS_db_HOST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    host = config('AWS_db_HOST')
    user = config ('AWS_db_USER')                                                                                                     
    # RBAC_USE_WHITE = TruE
    RECAPTCHA_PRIVATE_KEY=config('GOOGLE_RECAPTCHA_PRIVATE_KEY')
    TESTING = True
    RECAPTCHA_PUBLIC_KEY=config('GOOGLE_RECAPTCHA_PUBLIC_KEY')
    TESTING = True
