"""Flask configuration
Remember to export the following variables tothe GLOBAL ENV in terminal 
export SESSION_COOKIE_NAME
export SECRET_KEY
export PROD_DATABASE_URI
export DEV_DATABASE_URI
export SQLALCHEMY_DATABASE_URI
"""
from os import environ, path
from dotenv import load_dotenv
from flask_login import LoginManager

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config():
    """Base config."""
    SECRET_KEY = 'JHLIUGYUGIOUGOIUYGOUYGIUJGHOPIUGIUYUYGOYT7676'
    SESSION_COOKIE_NAME = 'knbhjbguyg7986t87t7g8t7gg8yuuh9i'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False