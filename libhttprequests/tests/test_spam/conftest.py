import pytest

from libhttprequests.spam.db import DBConnection


@pytest.fixture(scope='session')
def connection():
    # Setup
    db_connection = DBConnection()
    # Tear Down
    yield db_connection
    db_connection.close()


@pytest.fixture
def session(connection):
    # Setup
    db_session = connection.generate_session()
    yield db_session
    # Tear Down
    db_session.roll_back()
    db_session.close()
