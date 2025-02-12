import time
import requests

def get_monthly_prayer_times(latitude: float, longitude: float) -> list:
    """Get monthly prayer times for a given latitude and longitude."""
    current_date = time.localtime()
    url = f"https://api.aladhan.com/v1/calendar/{current_date[0]}/1?latitude={latitude}&longitude={longitude}&method=3&shafaq=general&tune=5%2C3%2C5%2C7%2C9%2C-1%2C0%2C8%2C-6"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    return None

def get_today_prayer_times(latitude: float, longitude: float) -> dict:
    """Get today's prayer times for a given latitude and longitude."""
    current_date = time.localtime()
    monthly_prayer_times = get_monthly_prayer_times(latitude, longitude)
    if monthly_prayer_times:
        today_prayer_times = monthly_prayer_times[current_date[2] - 1]["timings"]
        return today_prayer_times
    return None

def show_prayer_times(prayer_times: dict):
    """Print prayer times."""
    list_of_prayers = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
    for key in prayer_times:
        if key in list_of_prayers:
            print(f"{key}: {prayer_times[key]}")
