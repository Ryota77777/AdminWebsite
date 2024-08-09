import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '12g3j3l45jh3jnjhg'
    SQLALCHEMY_DATABASE_URI = 'postgresql://ryota:12345@localhost/user_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
