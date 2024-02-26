from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import select

from app.database import SessionLocal
from app.models.databases import Database
from app.services.backup_service import create_backup

scheduler = BackgroundScheduler()
scheduler.start()


def setup_scheduler_jobs():
    db = SessionLocal()
    databases = db.scalars(select(Database)).all()
    for database in databases:
        scheduler.add_job(
            create_backup,
            args=[database],
            trigger="interval",
            minutes=database.backup_period,
            id=f'backup_job_{database.id}',
            name=f'Backup job for {database.database_name}',
            replace_existing=True
        )
    db.close()


def shutdown_scheduler():
    scheduler.shutdown()
