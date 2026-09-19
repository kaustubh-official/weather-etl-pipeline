import psycopg2
import os
from dotenv import load_dotenv
from extract import fetch_weather_data
from transform import clean_weather_data

load_dotenv()  # reads the .env file

def load_weather_data(cleaned_data):
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
        (latitude, longitude, recorded_time, temperature_c, humidity_percent, wind_speed_kmh)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (
        cleaned_data["latitude"],
        cleaned_data["longitude"],
        cleaned_data["recorded_time"],
        cleaned_data["temperature_c"],
        cleaned_data["humidity_percent"],
        cleaned_data["wind_speed_kmh"]
    ))

    conn.commit()  # actually save the changes
    cursor.close()
    conn.close()
    print("Data loaded successfully!")

if __name__ == "__main__":
    raw = fetch_weather_data()
    cleaned = clean_weather_data(raw)
    load_weather_data(cleaned)