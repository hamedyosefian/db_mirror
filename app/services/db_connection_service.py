import subprocess
import psycopg2


def check_pg_dump_availability():
    try:
        subprocess.run(["pg_dump", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("pg_dump is available.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("pg_dump is not available. Please make sure PostgreSQL is installed and pg_dump is in your system's path.")
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
