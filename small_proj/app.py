from pipeline import run
from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
import time
load_dotenv(dotenv_path='../.env')
def connect_retry(retries=5,delay=2):
    url=(
        f"postgresql+psycopg2://"
        f"postgres:{os.getenv('POSTGRES_PASSWORD', 'password')}"
        f"@{os.getenv('DB_HOST', 'db')}"
        f"/{os.getenv('POSTGRES_DB', 'testdb')}"
        )
    for i in range(retries):
        try:
            engine=create_engine(url=url)
            with engine.connect() as conn:
                conn.execute(text('SELECT 1'))
            print('Connect successfully')
            return engine
        except Exception as e:
            print(f'Error: {e}, try to connect after {delay} seconds')
            time.sleep(delay)
    raise Exception("Cannot connect to database")

engine = connect_retry(10,2)
run(engine)
