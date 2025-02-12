from location import get_location
from prayer_times import get_today_prayer_times, show_prayer_times
from notifications import prayer_notification

def main():
    location = get_location()
    if location:
        latitude, longitude = location
        today_prayer_times = get_today_prayer_times(latitude, longitude)
        if today_prayer_times:
            show_prayer_times(today_prayer_times)
            prayer_notification(today_prayer_times)
        else:
            print("Failed to retrieve prayer times.")
    else:
        print("Failed to retrieve location.")

if __name__ == "__main__":
    main()
