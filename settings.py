import os
from dotenv import load_dotenv

load_dotenv()

TASK_QUEUE_REDIS_URL = os.getenv("TASK_QUEUE_REDIS_URL")
QUEUES = ["emails", "default"]
