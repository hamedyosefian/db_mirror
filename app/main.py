from fastapi import FastAPI
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
