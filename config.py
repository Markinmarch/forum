import os
from dotenv import load_dotenv

load_dotenv(dotenv_path = '.env')

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '')
ADMIN_KEY = os.getenv('ADMIN_EMAIL', '')
POSTGRES_USER = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DATABASE = 'forum'
MAIN_URL = 'localhost:8000'