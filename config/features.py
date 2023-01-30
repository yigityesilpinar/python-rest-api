import os


def is_background_worker_enabled():
    return os.getenv("USE_BACKGROUND_WORKER", "false").lower() == "true"
