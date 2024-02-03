import os
import subprocess
from datetime import datetime

import psycopg2
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from fastapi import FastAPI, Depends
from sqlalchemy import select

from app.dependencies import get_db
from app.models.databases import Database
from app.utils.scheduler import setup_scheduler_jobs, shutdown_scheduler

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


setup_scheduler_jobs()


@app.on_event("startup")
def startup_event():
    setup_scheduler_jobs()


@app.on_event("shutdown")
def shutdown_event():
    shutdown_scheduler()
