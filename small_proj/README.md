# Crypto Price ETL Pipeline

Simple ETL pipeline that extracts cryptocurrency prices from CoinGecko API,
transforms the data, and loads it into PostgreSQL — all running in Docker.

## Architecture
CoinGecko API → Extract → Transform → Load → PostgreSQL (Docker)

## Tech Stack
- Python 3.10
- SQLAlchemy + psycopg2
- PostgreSQL 15
- Docker Compose

## How to run
1. Copy `.env.example` to `.env` and fill in your values
2. Run: `docker-compose up --build`

## Project structure
- `extract.py` — calls CoinGecko API
- `transform.py` — cleans and structures data
- `load.py` — writes to PostgreSQL
- `pipeline.py` — orchestrates extract → transform → load

## What I learned
- Docker Compose multi-service setup
- Retry logic for database connection
- Environment variable management with .env
- Centralized logging (file + console) across modules
- Error handling for API and data transformation failures