import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DB_HOST = os.getenv('db_host')
    DB_USER = os.getenv('db_user')
    DB_PASSWD = os.getenv('db_passwd')
    DB_SCHEMA = os.getenv('db_schema')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    if Config.DB_USER and Config.DB_PASSWD and Config.DB_HOST and Config.DB_SCHEMA:
        SQLALCHEMY_DATABASE_URI = str.format('mysql://%s:%s@%s:3306/%s') % (
            Config.DB_USER, Config.DB_PASSWD, Config.DB_HOST, Config.DB_SCHEMA)
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users-dev.sqlite')


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    if Config.DB_USER and Config.DB_PASSWD and Config.DB_HOST and Config.DB_SCHEMA:
        SQLALCHEMY_DATABASE_URI = str.format('mysql://%s:%s@%s:3306/%s') % (
            Config.DB_USER, Config.DB_PASSWD, Config.DB_HOST, Config.DB_SCHEMA)
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users-prod.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
