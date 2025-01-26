import time
import requests
import json

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

def get_prayer_times(latitude,longitude):
    current_date = time.localtime()
    url = f"https://api.aladhan.com/v1/calendar/{current_date[0]}/1?latitude={latitude}&longitude={longitude}&method=3&shafaq=general&tune=5%2C3%2C5%2C7%2C9%2C-1%2C0%2C8%2C-6"
    respons = requests.get(url)
    if respons.status_code == 200:
        data = respons.json()
        return (data["data"])


latitude = get_location()[0]
longitude = get_location()[1] 
print(get_prayer_times(latitude,longitude))

# while True:
#     local_time = time.localtime()
#     if local_time[4] != prev_time_sec:
#         print(f"Current time: {local_time[3]:02d}:{local_time[4]:02d}")
#         prev_time_sec = local_time[4]
#         get_location()
