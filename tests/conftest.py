import pytest
from db import db
from pythonrestapi.config import config
from pythonrestapi.application import application


@pytest.fixture(autouse=True, scope="function")
def reset_db():
    yield
    with application.app_context():
        db.drop_all()
        db.create_all()


@pytest.fixture
def base_url():
    return config["TEST_SERVICE_BASE_URL"]
