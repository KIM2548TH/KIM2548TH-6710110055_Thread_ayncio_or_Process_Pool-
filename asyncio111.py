import asyncio
import aiohttp
import time

CITIES = [
    {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018},
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093}
]

API_URL = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

async def fetch_weather(session, city):
    """ดึงข้อมูลสภาพอากาศของเมืองโดยใช้ asyncio + aiohttp"""
    url = API_URL.format(lat=city["lat"], lon=city["lon"])
    async with session.get(url) as response:
        data = await response.json()
        temp = data["current_weather"]["temperature"]
        print(f"{city['name']}: {temp}°C")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city) for city in CITIES]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    duration = time.time() - start_time
    print(f"Fetched weather for {len(CITIES)} cities in {duration:.2f} seconds")
