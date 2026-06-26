Using ETL pipeline from small_project to practice with airflow
Therefore, there are some modules such that are not installed in airflow
so we need to add them. There are two ways:
- One is custom dockerfile:
    + Change this part in .yml file:
        x-airflow-common:
        &airflow-common
        build:                        
            context: .
            dockerfile: Dockerfile    
- Another one is add _PIP_ADDITIONAL_REQUIREMENTS into .env
In this case I will use second option first for simplicity as you can read in the warning in .yml file

Use curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
to create docker-compose.yml for airflow

Create necessary folders:
mkdir -p dags logs plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

Initialize db for airflow. This db will store metadata about DAG, task run,...
docker-compose up airflow-init
Run containers:
docker compose up -d 
Open browser http://localhost:8080 to see dashboard
