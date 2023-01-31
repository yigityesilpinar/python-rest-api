from typing import Any
from pythonrestapi.application_factory import create_app
from pythonrestapi.config import config
from dotenv import load_dotenv


load_dotenv()

application: Any = create_app(__name__, config=config)
