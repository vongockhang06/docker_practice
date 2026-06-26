from sqlalchemy import text, create_engine
from dotenv import load_dotenv
import os
import logging
logger=logging.getLogger(__name__)
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
                INSERT INTO crypto_prices (coin, price_usd, usd_24h_change, collected_at)
                VALUES (:coin, :price_usd, :usd_24h_change, :collected_at)
            """),row)
    logger.info(f"Loaded {len(records)} rows successfully")