import os
import sys
import subprocess

if len(sys.argv) < 2:
    print("Please provide a command to run with elevated privileges.")
else:
    command = ' '.join(sys.argv[1:])
    subprocess.run(["powershell", "-Command", f"Start-Process cmd -ArgumentList '/c {command}' -Verb RunAs"])
