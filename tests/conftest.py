import pytest
from db import db
from pythonrestapi.application import application


@pytest.fixture(autouse=True, scope="session")
def reset_db():
    yield
    with application.app_context():
        db.drop_all()
        db.create_all()
