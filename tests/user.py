import pytest
import requests
from tests.factories import create_user


@pytest.mark.usefixtures("base_url")
class TestUserResources:
    def test_new_user_register(self, base_url):
        email = "somebody@gmail.com"
        password = "1234@abcd"
        resp = requests.post(
            f"{base_url}/register",
            headers={"Content-type": "application/json"},
            json=dict(email=email, password=password),
        )
        assert resp.status_code == 201
        response_data = resp.json()
        assert response_data == dict(
            message="User created.",
        )

    def test_already_registered_user_register(self, base_url):
        email = "somebody@gmail.com"
        password = "1234@abcd"
        create_user(email=email, password=password)
        resp = requests.post(
            f"{base_url}/register",
            headers={"Content-type": "application/json"},
            json=dict(email=email, password=password),
        )
        assert resp.status_code == 409
        response_data = resp.json()
        assert response_data == dict(code=409, message="email already exist", status="Conflict")
