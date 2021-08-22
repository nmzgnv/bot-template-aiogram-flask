import os

from config import DEBUG, LOCAL_DATABASE_URL, DATABASE_URL, USE_LOCAL_VARIABLES
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = DEBUG
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = LOCAL_DATABASE_URL if USE_LOCAL_VARIABLES else DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
