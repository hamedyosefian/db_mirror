from fastapi import FastAPI

from app.routers import database_router, backup_router

app = FastAPI()


@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "Hello World"}


app.include_router(database_router.router, prefix="/database", tags=["Database"])
app.include_router(backup_router.router, prefix="/backup", tags=["Backup"])
