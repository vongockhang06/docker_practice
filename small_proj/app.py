from logger_config import setup_pipeline_logging
setup_pipeline_logging()

from pipeline import run
from sqlalchemy import create_engine, text
import os
import time
import logging
logger = logging.getLogger(__name__)
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
            logger.info('Connected to database successfully')
            return engine
        except Exception as e:
            logger.warning(f'Connection attempt {i+1} failed: {e}, retrying in {delay}s')
            time.sleep(delay)
    logger.error("Cannot connect to database after all retries")
    raise Exception("Cannot connect to database")

engine = connect_retry(10,2)
run(engine)
