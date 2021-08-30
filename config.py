"""FLASK CONFIG"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
DB_HOST = environ.get('DB_HOST')
DB_PASS = environ.get('DB_PASS')
DB_USER = environ.get('DB_USER')
SECRET_KEY = environ.get('SECRET_KEY')
