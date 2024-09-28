from sqlalchemy import create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PASSWORD')

SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_db():
    try:
        db = SessionLocal()
        db.execute(text('SELECT 1'))
        print('Database is up')
        db.close()
        return {
            'status': 'UP',
            'database': {
                'name': engine.url.database,
                'user': engine.url.username,
                'host': engine.url.host,
                'port': engine.url.port,
                'tables': inspect(engine).get_table_names(),
            },
        }
    except Exception as e:
        print(e)
        return {
            'status': 'DOWN',
        }