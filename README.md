# Weather ETL Pipeline

A simple ETL (Extract, Transform, Load) pipeline that fetches live weather data from the Open-Meteo API, cleans it, and stores it in a PostgreSQL database.

## What it does

- **Extract** (`extract.py`) — calls the Open-Meteo API to get current weather data for a given location
- **Transform** (`transform.py`) — flattens the nested API response into a clean, simple structure
- **Load** (`load.py`) — inserts the cleaned data into a PostgreSQL table, creating the table if it doesn't exist

## Tech stack

- Python
- PostgreSQL
- `requests` for API calls
- `psycopg2` for database connectivity
- `python-dotenv` for secure credential management

## Setup

1. Clone this repo
2. Create a virtual environment: `python -m venv venv`
3. Activate it and install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with your database password:
5. Make sure PostgreSQL is running and a database named `weather_db` exists
6. Run the pipeline: `python load.py`

## What I learned

Building this project taught me the ETL pattern, working with REST APIs, handling nested JSON data, writing parameterized SQL queries, and managing database credentials securely using environment variables. I also learned Git fundamentals including resolving merge conflicts.