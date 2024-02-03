from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.services.backup_service import create_backup

scheduler = BackgroundScheduler()
scheduler.start()


def setup_scheduler_jobs():
    scheduler.add_job(
        create_backup,
        trigger=IntervalTrigger(minutes=1),
        id='backup_job',
        name='Backup databases with schedule',
        replace_existing=True
    )


def shutdown_scheduler():
    scheduler.shutdown()
