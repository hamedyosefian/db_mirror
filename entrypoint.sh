#!/bin/bash
set -e

# Run Alembic migrations
alembic upgrade head

# Start FastAPI
#exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
exec gunicorn app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000