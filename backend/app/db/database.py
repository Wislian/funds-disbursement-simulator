import psycopg2
import os
from datetime import datetime


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
                colnames = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                result = []
                for row in rows:
                    row_dict = dict(zip(colnames, row))
                    for key, value in row_dict.items():
                        if isinstance(value, datetime):
                            row_dict[key] = value.strftime("%Y-%m-%d %H:%M:%S")
                    result.append(row_dict)
                
                return result
    def fetch_one(self, query, params=None):
        with psycopg2.connect(**self.connection_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                colnames = [desc[0] for desc in cursor.description]
                row = cursor.fetchone()
                if row:
                    row_dict = dict(zip(colnames, row))
                    for key, value in row_dict.items():
                        if isinstance(value, datetime):
                            row_dict[key] = value.strftime("%Y-%m-%d %H:%M:%S")
                    return row_dict
                return None

    def execute(self, query, params=None):
            with psycopg2.connect(**self.connection_params) as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, params or ())
                    conn.commit()