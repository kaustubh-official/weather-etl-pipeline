import requests

# Open-Meteo API endpoint - no API key needed
url = "https://api.open-meteo.com/v1/forecast"

# Parameters: latitude/longitude for a city, and what data we want
params = {
    "latitude": 20.2961,     # Bhubaneswar, India
    "longitude": 85.8245,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

print(data)