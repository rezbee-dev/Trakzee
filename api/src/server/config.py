import os


class BaseConfig:
    TESTING = False
    SECRET_KEY = "my_secret_key"


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    url = os.environ.get("DATABASE_URL")

    # See: https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
    if url is not None and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = url
    SECRET_KEY = os.getenv("SECRET_KEY", BaseConfig.SECRET_KEY)


# def app_settings(env):
#     # todo: check if param exists or use os.getenv
#     if(os.getenv('APP_ENV') == 'dev'):
#         return DevelopmentConfig()
#     elif os.getenv('APP_ENV') == 'test':
#         return TestingConfig()
#     elif os.getenv('APP_ENV') == 'production':
#         return ProductionConfig()
#     else:
#         raise Exception('APP_ENV not set!')
