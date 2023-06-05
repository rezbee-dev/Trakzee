import os

from server.config import BaseConfig


def test_development_config(test_app):
    test_app.config.from_object("server.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == BaseConfig.SECRET_KEY
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 4


def test_testing_config(test_app):
    test_app.config.from_object("server.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == BaseConfig.SECRET_KEY
    assert test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_TEST_URL")
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 4


def test_production_config(test_app):
    test_app.config.from_object("server.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == os.getenv("SECRET_KEY", BaseConfig.SECRET_KEY)
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
    assert test_app.config["BCRYPT_LOG_ROUNDS"] == 13
