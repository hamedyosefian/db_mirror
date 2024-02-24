import os
import subprocess
from datetime import datetime

import boto3

from app.config import settings
from app.database import SessionLocal
from app.dependencies import get_db
from app.models.databases import Database
from sqlalchemy import select

from app.services.db_connection_service import check_pg_dump_availability, check_database_connection


def create_backup():
    db = SessionLocal()
    try:
        backup_dir = 'backups'
        os.makedirs(backup_dir, exist_ok=True)

        if not check_pg_dump_availability():
            return {"error": "pg_dump is not available."}

        database_list = db.scalars(select(Database)).all()
        for database in database_list:
            if not check_database_connection(database.host, database.port, database.username, database.database_name, database.password):
                continue
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = f"{database.database_name}_{timestamp}.sql"
            backup_path = os.path.join(backup_dir, filename)

            os.environ['PGPASSWORD'] = database.password

            command = [
                "pg_dump",
                f"--host={database.host}",
                f"--port={database.port}",
                f"--username={database.username}",
                f"--dbname={database.database_name}",
                f"--file={backup_path}"
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Backup successful: {backup_path}")

                s3 = boto3.client("s3",
                                  aws_access_key_id=settings.S3_ACCESS_KEY,
                                  aws_secret_access_key=settings.S3_SECRET_key,
                                  endpoint_url=settings.S3_URL,
                                  )
                with open(backup_path, 'rb') as file_obj:
                    s3.upload_fileobj(Fileobj=file_obj, Bucket='backups', Key=filename)

                print(f"Uploaded to S3: s3://backups/{filename}")

                # Remove the local backup file after successful upload
                os.remove(backup_path)
                print(f"Local backup file removed: {backup_path}")

            except subprocess.CalledProcessError as e:
                print(f"Backup failed for {database.database_name}: {e}")

            finally:
                # Remove PGPASSWORD from environment
                os.environ.pop('PGPASSWORD', None)
    finally:
        db.close()
