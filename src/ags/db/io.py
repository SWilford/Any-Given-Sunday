import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv(
    "DATABASE_URL", "postgresql://ags_user:ags_pass@localhost:5432/ags_db"
)


def get_connection():
    return psycopg.connect(DB_URL)
