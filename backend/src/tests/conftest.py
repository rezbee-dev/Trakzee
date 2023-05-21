# conftest.py provides fixtures 
# fixtures are functions that handle setup/teardown and other init type operations
# see: https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files

import pytest

from server.app import create_app, db

# scopes determine how often fixture is invoked
# Module = once per test module
@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('server.config.TestingConfig')
    with app.app_context():
        yield app  # testing happens here


# all code before the yield statement serves as setup code
# all code after, servies as teardown
@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()