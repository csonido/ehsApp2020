import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    UPLOAD_FOLDER = 'D:/Dev/Uploads'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/main'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "1577121640147"


