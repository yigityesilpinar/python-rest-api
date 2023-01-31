#!/bin/bash

poetry run flask db upgrade

exec poetry run gunicorn --bind  0.0.0.0:${PORT} "pythonrestapi.application"