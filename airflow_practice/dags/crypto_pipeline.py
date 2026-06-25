from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.insert(0, '/opt/airflow')

default_args = {
    'owner': 'khang',
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

def extract_task():
    from extract import extract
    data = extract()
    return data

def transform_task(**context):
    from transform import transform
    raw = context['ti'].xcom_pull(task_ids='extract')
    rows = transform(raw)
    return rows

def load_task(**context):
    from load import create_table, load
    from sqlalchemy import create_engine
    import os
    rows = context['ti'].xcom_pull(task_ids='transform')
    engine = create_engine(
        f"postgresql+psycopg2://postgres:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('POSTGRES_DB')}"
    )
    create_table(engine)
    load(engine, rows)

with DAG(
    dag_id='crypto_etl_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 6, 25),
    schedule='@hourly',          #  New modern parameter
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_task
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_task
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_task
    )

    extract >> transform >> load