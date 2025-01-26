import time
import requests
import json

prev_time_sec = 0

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



# while True:
#     local_time = time.localtime()
#     if local_time[4] != prev_time_sec:
#         print(f"Current time: {local_time[3]:02d}:{local_time[4]:02d}")
#         prev_time_sec = local_time[4]
#         get_location()
