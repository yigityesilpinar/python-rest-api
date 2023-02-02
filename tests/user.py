import requests


class TestUserResources:
    def test_user_register(self):
        resp = requests.post(
            "http://127.0.0.1:5000/register",
            headers={"Content-type": "application/json"},
            json={"email": "yigityesilpinar@gmail.com", "password": "1234tamam"},
        )
        assert resp.status_code == 201
        response_data = resp.json()
        assert response_data == dict(
            message="User created.",
        )
