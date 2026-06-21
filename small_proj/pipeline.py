from extract import extract
from transform import transform
from load import create_table, load
import logging
logger = logging.getLogger(__name__)

def run(engine):
    logger.info("Starting extract step...")
    raw = extract()

    logger.info("Starting transform step...")
    rows = transform(raw)

    logger.info("Starting load step...")
    create_table(engine)
    load(engine, rows)
    
    logger.info("Pipeline finished successfully")