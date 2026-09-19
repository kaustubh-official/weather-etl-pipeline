import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 20.2961,     # Bhubaneswar, India
    "longitude": 85.8245,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

print(data)
