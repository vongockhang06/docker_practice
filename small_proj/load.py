from sqlalchemy import text, create_engine
from dotenv import load_dotenv
import os
load_dotenv
def get_engine():
    url=(
        f"postgresql+psycopg2://"
        f"postgres:{os.getenv('DB_PASSWORD', 'password')}"
        f"@{os.getenv('DB_HOST', 'localhost')}"
        f"/{os.getenv('DB_NAME', 'testdb')}"
    )
    return create_engine(url=url)

def create_table(engine):
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS crypto_prices (
                id SERIAL PRIMARY KEY,
                coin TEXT,
                price_usd FLOAT,
                usd_24h_change FLOAT,
                collected_at TIMESTAMP
            )
        """))

def load(engine, records:list):
    with engine.begin() as conn:
        for row in records:
            conn.execute(text("""
                INSERT INTO crypto_prices
                VALUES (:coin, :price_usd, :usd_24h_change, :collected_at)
            """),row)
    print('Load successfully')