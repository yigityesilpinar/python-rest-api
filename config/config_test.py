import os

assert os.getenv("ENV_NAME") == "test"
ENV_NAME = os.getenv("ENV_NAME")

DEBUG = False
TESTING = True
