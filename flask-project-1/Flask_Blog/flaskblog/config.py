from os import environ

class BaseConfig(object):
    SECRET_KEY = '35327e19d209614d7150e4c45f8ec1a2'

class LocalDevConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:testuser@localhost:5432/testdb'

class LocalProdConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:testuser@localhost:5432/testdb'

class HerokuDevConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') and environ.get('DATABASE_URL').replace("://", "ql://", 1)

class HerokuProdConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') and environ.get('DATABASE_URL').replace("://", "ql://", 1)