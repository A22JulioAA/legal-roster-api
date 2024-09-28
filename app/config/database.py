from sqlalchemy import create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = 'postgres'
DB_NAME = 'legal-roster-db'
DB_PORT = '5432'
DB_HOST = 'localhost'
DB_PASSWORD = 'abc123.'

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
        print('Database Info: ')
        print(f'Database name: {engine.url.database}')
        print(f'Database user: {engine.url.username}')
        print(f'Database host: {engine.url.host}')
        print(f'Database port: {engine.url.port}')
        print(f'Database tables: {inspect(engine).get_table_names()}')
        db.close()
        return True
    except Exception as e:
        print(e)
        return False