class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = '35327e19d209614d7150e4c45f8ec1a2'
    SQLALCHEMY_DATABASE_URI = 'postgresql://testuser:testuser@localhost:5432/testdb'
