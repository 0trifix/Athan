import time
import subprocess

def prayer_notification(prayer_times: dict):
    """Send a notification for each prayer time."""
    list_of_prayers = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
    current_time = time.localtime()
    current_time_sec = current_time[3] * 3600 + current_time[4] * 60 + current_time[5]
    for key in prayer_times:
        if key in list_of_prayers:
            prayer_time = prayer_times[key].split(" ")[0]
            prayer_time_sec = int(prayer_time.split(":")[0]) * 3600 + int(prayer_time.split(":")[1]) * 60
            if current_time_sec == prayer_time_sec:
                subprocess.run(["notify-send", f"Time for {key} prayer!"])
