import sys
import psutil
import time

def monitor(interval=2):
    try:
        print("Monitoring system performance. Press Ctrl+C to stop.")
        while True:
            cpu = psutil.cpu_percent(interval=interval)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
    except KeyboardInterrupt:
        print("Stopped monitoring.")

if __name__ == "__main__":
    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    monitor(interval)
