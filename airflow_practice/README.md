use ETL pipeline from small_project to practice with airflow

Use curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
to create docker-compose.yml for airflow

Create necessary folders:
mkdir -p dags logs plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

Initialize db for airflow: docker-compose up airflow-init
docker compose up -d 
Open browser http://localhost:8080 to see dashboard