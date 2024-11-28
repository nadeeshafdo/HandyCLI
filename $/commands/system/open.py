import os
import sys

if len(sys.argv) < 2:
    print("Usage: open.py path")
else:
    path = sys.argv[1]
    os.startfile(path)
