import requests

def get_location() -> tuple:
    """Returns the latitude and longitude of the user's location using the IP address"""
    url = "https://api.ip2location.io/?"
    respons = requests.get(url)
    if respons.status_code == 200:
        data = respons.json()
        latitude=data["latitude"]
        longitude=data["longitude"]
        return (latitude,longitude)
    return (None,None)
