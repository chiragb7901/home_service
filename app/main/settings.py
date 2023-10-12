import os
#from environs import Env, EnvError

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = 'postgresql+psycopg2://super:super_admin@parthverma-2936.postgres.pythonanywhere-services.com:12936/credpay'
# postgres_local_base = 'postgresql://postgres:root@localhost:5432/credpay'

#env = Env()
#env.read_env()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    # uncomment the line below to use mysql
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/home_service'

    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
    #      basedir, "flask_boilerplate.db"
    #  )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'development'

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY