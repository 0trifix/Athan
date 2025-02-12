import time
import subprocess
import requests

#prev_time_sec = 0

# Function to get longitude and latitude using IP address
def get_location():
    url = "https://api.ip2location.io/?"
    respons = requests.get(url)

    #Check if the response is succesfull
    if respons.status_code == 200:
        data = respons.json()
        latitude=data["latitude"]
        longitude=data["longitude"]
        return (latitude,longitude)
    return None

def get_monthly_prayer_times(latitude,longitude):
    current_date = time.localtime()
    url = f"https://api.aladhan.com/v1/calendar/{current_date[0]}/1?latitude={latitude}&longitude={longitude}&method=3&shafaq=general&tune=5%2C3%2C5%2C7%2C9%2C-1%2C0%2C8%2C-6"
    respons = requests.get(url)
    if respons.status_code == 200:
        data = respons.json()
        return (data["data"]) # Returns the prayer times of the month in list of dictionary's 
    return None

def get_today_prayer_times():
    location = get_location()
    current_date = time.localtime()
    today_prayer_times = get_monthly_prayer_times(location[0],location[1])[current_date[2]-1]["timings"]
    return today_prayer_times

def show_prayer_times():
    list_of_prayers = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"]
    today_prayer_times = get_today_prayer_times()
    for key in today_prayer_times:
        if key in list_of_prayers:
            print(f"{key}: {today_prayer_times[key]}")
    return None

def prayer_notification():
    list_of_prayers = ["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha"]
    today_prayer_times = get_today_prayer_times()
    current_time = time.localtime()
    current_time_sec = current_time[3]*3600 + current_time[4]*60 + current_time[5]
    for key in today_prayer_times:
        if key in list_of_prayers:
            prayer_time = today_prayer_times[key]
            prayer_time_sec = int(prayer_time.split(":")[0])*3600 + int(prayer_time.split(":")[1])*60
            if current_time_sec == prayer_time_sec:
                subprocess.run(["notify-send",f"{key} prayer time"])
    return None

