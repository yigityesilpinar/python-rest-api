import os

ENV_NAME = "test"
DB_NAME = "test_db"

DEBUG = False
TESTING = True

DATABASE_URL = os.getenv("TEST_DATABASE_URL")
