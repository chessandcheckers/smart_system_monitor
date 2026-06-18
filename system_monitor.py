import psutil 
import time

print("Monitoring started. Press Ctrl+C to stop.")
try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu}%")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
