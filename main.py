import time

prev_time_sec = 0

while True:
    local_time = time.localtime()
    if local_time[4] != prev_time_sec:
        print(f"Current time: {local_time[3]:02d}:{local_time[4]:02d}")
        prev_time_sec = local_time[4]
