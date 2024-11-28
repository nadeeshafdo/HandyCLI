import sys
import time
import os

def watch(path, interval=2):
    last_modified = os.path.getmtime(path)
    print(f"Watching '{path}' for changes...")

    while True:
        try:
            current_modified = os.path.getmtime(path)
            if current_modified != last_modified:
                print(f"'{path}' has been modified.")
                last_modified = current_modified
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopped watching.")
            break
        except FileNotFoundError:
            print(f"File '{path}' not found.")
            break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python watch.py <file_or_directory>")
    else:
        path = sys.argv[1]
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 2
        watch(path, interval)
