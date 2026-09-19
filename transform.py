from extract import fetch_weather_data

def clean_weather_data(raw_data):
    
    current = raw_data["current"]
    units = raw_data["current_units"]

    cleaned = {
        "latitude": raw_data["latitude"],
        "longitude": raw_data["longitude"],
        "recorded_time": current["time"],
        "temperature_c": current["temperature_2m"],
        "humidity_percent": current["relative_humidity_2m"],
        "wind_speed_kmh": current["wind_speed_10m"]
    }

    return cleaned

if __name__ == "__main__":
    raw = fetch_weather_data()
    cleaned = clean_weather_data(raw)
    print(cleaned)