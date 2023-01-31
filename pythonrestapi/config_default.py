import os
from typing import Callable, Final, List, Optional, Set, TypeVar

T = TypeVar("T")


def getenv_set(name: str, action: Callable[[str], T] = lambda x: x, default: Optional[Set[T]] = None) -> Set[T]:
    """Get environment variable and return it as a set.

    Environment variable should contain entries separated by commas,
    any whitespace around values is trimmed if present.

    Accepts optional transformer (action), which is identity function by default.
    If env var is not present or empty, return empty set.
    """

    value = os.getenv(name, "")
    if not value:
        return default or set()

    return {action(entry.strip()) for entry in value.split(",") if entry and entry.strip()}


def getenv_list(name: str) -> List[str]:
    return [entry.strip() for entry in os.getenv(name, "").split(",") if entry and entry.strip()]


def getenv_strings(name: str) -> Set[str]:
    return getenv_set(name, lambda s: s)


def getenv_boolean(name: str, default: bool = False) -> bool:
    return os.getenv(name, "true" if default else "false").lower() == "true"


def getenv_int(name: str, default: str) -> int:
    return int(os.getenv(name, default))


def getenv_float(name: str, default: str) -> float:
    return float(os.getenv(name, default))


ENV_NAME = "default"

MAILGUN_API_KEY = os.environ["MAILGUN_API_KEY"]
MAILGUN_DOMAIN = os.environ["MAILGUN_DOMAIN"]
TASK_QUEUE_REDIS_URL = os.environ["TASK_QUEUE_REDIS_URL"]
USE_BACKGROUND_WORKER = os.environ["USE_BACKGROUND_WORKER"]
DATABASE_URL = os.environ["DATABASE_URL"]
JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
