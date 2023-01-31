import os
from flask import Flask
import redis
from rq import Queue


def configure_task_queue(app: Flask):

    task_queue_redis_url = app.config.get("TASK_QUEUE_REDIS_URL")
    if not task_queue_redis_url:
        raise RuntimeError("Redis url must be defined in environment")
    connection = redis.from_url(task_queue_redis_url)
    app.queue = Queue("emails", connection=connection)  # type: ignore
