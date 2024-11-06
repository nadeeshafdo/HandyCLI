import os
import sys
import shutil
import time

def backup(source, destination=None):
    if not destination:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        destination = f"{source}_backup_{timestamp}"
    
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
        print(f"Backup created at '{destination}'")
    except Exception as e:
        print(f"Error creating backup: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python backup.py <source> [destination]")
    else:
        source = sys.argv[1]
        destination = sys.argv[2] if len(sys.argv) > 2 else None
        backup(source, destination)
