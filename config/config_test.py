import os

assert os.getenv("ENV_NAME") == "test"
ENV_NAME = os.getenv("ENV_NAME")
TEST_SERVICE_BASE_URL = "http://127.0.0.1:5000"

DEBUG = False
TESTING = True
