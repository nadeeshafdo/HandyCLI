import os
import sys
import subprocess

def check_7z_installed():
    result = subprocess.run(["where", "7z"], capture_output=True)
    return result.returncode == 0

if not check_7z_installed():
    print("7-Zip not found in PATH. Please install 7-Zip or add it to the PATH.")
else:
    if len(sys.argv) < 2:
        print("Usage: unzip.py [zipfile] [destination]")
    else:
        zipfile = sys.argv[1]
        destination = os.path.dirname(zipfile)
        if len(sys.argv) > 2:
            destination = sys.argv[2]
        subprocess.run(["7z", "x", zipfile, f"-o{destination}", "-y"])
        print("Unzipping completed.")
