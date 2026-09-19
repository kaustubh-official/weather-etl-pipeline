import psycopg2
import os
from dotenv import load_dotenv
from extract import fetch_weather_data
from transform import clean_weather_data

load_dotenv()
def load_weather_data(cleaned_data, city_name):
    conn = psycopg2.connect(
        host="localhost",
        database="weather_db",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_readings (
            id SERIAL PRIMARY KEY,
            city_name TEXT,
            latitude FLOAT,
            longitude FLOAT,
            recorded_time TIMESTAMP,
            temperature_c FLOAT,
            humidity_percent FLOAT,
            wind_speed_kmh FLOAT
        );
    """)

    cursor.execute("""
        INSERT INTO weather_readings 
        (city_name, latitude, longitude, recorded_time, temperature_c, humidity_percent, wind_speed_kmh)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (
        city_name,
        cleaned_data["latitude"],
        cleaned_data["longitude"],
        cleaned_data["recorded_time"],
        cleaned_data["temperature_c"],
        cleaned_data["humidity_percent"],
        cleaned_data["wind_speed_kmh"]
    ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Data loaded successfully for {city_name}!")
if __name__ == "__main__":
    cities = [
        ("Bhubaneswar", 20.2961, 85.8245),
        ("Delhi", 28.6139, 77.2090),
        ("Mumbai", 19.0760, 72.8777),
        ("Chennai", 13.0827, 80.2707),
        ("Kolkata", 22.5726, 88.3639),
    ]
    for city_name, lat, lon in cities:
        raw = fetch_weather_data(lat, lon)
        cleaned = clean_weather_data(raw)
        load_weather_data(cleaned, city_name)