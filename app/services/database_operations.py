import os
import subprocess
import time
from datetime import datetime

import psycopg2
import boto3

from app.config import settings


def check_pg_dump_availability():
    try:
        subprocess.run(["pg_dump", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("pg_dump is available.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("pg_dump is not available.")
        return False


def check_database_connection(host, port, username, dbname, password):
    conn_string = f"host={host} port={port} user={username} dbname={dbname} password={password}"
    try:
        conn = psycopg2.connect(conn_string)
        conn.close()
        print(f"Successfully connected to the database: {dbname}")
        return True
    except psycopg2.OperationalError as e:
        print(f"Failed to connect to the database: {dbname}. Error: {e}")
        return False


def remove_differential_backups_s3(database, bucket_name, diff_backup_prefix):
    s3 = boto3.client("s3",
                      aws_access_key_id=settings.S3_ACCESS_KEY,
                      aws_secret_access_key=settings.S3_SECRET_key,
                      endpoint_url=settings.S3_URL)

    try:
        # List all objects within the specified differential backup folder (path)
        diff_backup_objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=diff_backup_prefix)
        if 'Contents' in diff_backup_objects:
            for obj in diff_backup_objects['Contents']:
                print(f"Removing {obj['Key']} from S3")
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print("Differential backups removed from S3.")
        else:
            print("No differential backups found to remove.")
    except Exception as e:
        print(f"Failed to delete differential backups from S3. Reason: {e}")


def create_backup(database, backup_type):
    if not check_pg_dump_availability():
        return {"error": "pg_dump is not available."}

    # Retry mechanism
    max_retries = 3
    retry_delay = 10  # seconds
    for attempt in range(max_retries):
        if attempt > 0:
            print(f"Retrying backup for {database.database_name}, attempt {attempt + 1}")
            time.sleep(retry_delay)

        if check_database_connection(database.host, database.port, database.username, database.database_name, database.password):
            break
    else:
        print("Max retries reached, aborting backup.")
        return

    # Proceed with backup after successful connection check
    backup_dir = f'backups/{database.id}-{database.database_name}/{backup_type}'
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"{database.database_name}_{backup_type}_{timestamp}.sql"
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
                          endpoint_url=settings.S3_URL)
        with open(backup_path, 'rb') as file_obj:
            s3.upload_fileobj(Fileobj=file_obj, Bucket='backups', Key=f"{database.id}-{database.database_name}/{backup_type}/{filename}")

        print(f"Uploaded to S3: s3://backups/{filename}")
        os.remove(backup_path)
        print(f"Local backup file removed: {backup_path}")

        if backup_type == 'full':
            diff_backup_prefix = f"{database.id}-{database.database_name}/diff/"
            remove_differential_backups_s3(database, 'backups', diff_backup_prefix)

    except subprocess.CalledProcessError as e:
        print(f"Backup failed for {database.database_name}: {e}")
    finally:
        os.environ.pop('PGPASSWORD', None)
