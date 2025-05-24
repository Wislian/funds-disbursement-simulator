import psycopg2
import os

class Database:
    def __init__(self):
        self.connection_params = {
            "dbname": os.getenv("DB_NAME", "postgres"),
            "user": os.getenv("DB_USER", "postgres"),
            "password": os.getenv("DB_PASSWORD", "postgres"),
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", 5432)
        }
    def fetch_all(self, query, params=None):
        with psycopg2.connect(**self.connection_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                return cursor.fetchall()

    def execute(self, query, params=None):
        with psycopg2.connect(**self.connection_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                conn.commit()