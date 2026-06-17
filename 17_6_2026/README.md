This is the third exercise.
Same as second one but try to use python to connect to postgres database in containers.
docker compose up --build: ignore the old snapshot to rebuild everything
docker compose up -d
docker compose down/start/stop
docker rm $(docker ps -aq)
docker volume ls
docker volume rm
docker compose logs db
docker compose down -v