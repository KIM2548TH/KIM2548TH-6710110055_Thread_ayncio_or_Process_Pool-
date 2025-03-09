import requests
import time
import concurrent.futures

CITIES = [
    {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018},
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093}
]

API_URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

def fetch_weather(city):
    """ดึงข้อมูลสภาพอากาศของเมืองโดยใช้ Thread"""
    url = API_URL.format(lat=city["lat"], lon=city["lon"])
    response = requests.get(url)
    data = response.json()
    temp = data["current_weather"]["temperature"]
    print(f"{city['name']}: {temp}°C")

if __name__ == "__main__":
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fetch_weather, CITIES)

    duration = time.time() - start_time
    print(f"Fetched weather for {len(CITIES)} cities in {duration:.2f} seconds")
