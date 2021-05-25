from os import environ

class BaseConfig(object):
    ENV = 'development'
    DEBUG = False
    SECRET_KEY = '35327e19d209614d7150e4c45f8ec1a2'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') and environ.get('DATABASE_URL').replace("://", "ql://", 1) or 'postgresql://testuser:testuser@localhost:5432/testdb'

class DevConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False