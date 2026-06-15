##ex1: write simple docker file and simple app.py

##ex2:
##Pull and run Postgres by docker
docker run --name pg-test \
 -e POSTGRES_PASSWORD=password \
 -e POSTGRES_DB=testdb \
 -p 5433:5432 \
 -d postgres:15

##Checking
docker ps

##Go into container
docker exec -it pg-test psql -U postgres -d testdb

##SQL code for create table for checking
CREATE TABLE test (id SERIAL, name TEXT);
INSERT INTO test (name) VALUES ('Khang');
SELECT * FROM test;

