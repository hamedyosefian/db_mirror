from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import select

from app.database import SessionLocal
from app.models.databases import Database
from app.services.database_operations import create_backup
from apscheduler.triggers.cron import CronTrigger

scheduler = BackgroundScheduler()
scheduler.start()


def setup_scheduler_jobs():
    db = SessionLocal()
    databases = db.scalars(select(Database)).all()
    for database in databases:
        scheduler.add_job(
            create_backup,
            args=[database, 'diff'],
            trigger=CronTrigger.from_crontab(database.differential_backup_cron),
            id=f'differential_backup_job_{database.id}',
            name=f'Differential Backup job for {database.database_name}',
            replace_existing=True
        )

        scheduler.add_job(
            create_backup,
            args=[database, 'full'],
            trigger=CronTrigger.from_crontab(database.full_backup_cron),
            id=f'full_backup_job_{database.id}',
            name=f'Full Backup job for {database.database_name}',
            replace_existing=True
        )
    db.close()


def shutdown_scheduler():
    scheduler.shutdown()
