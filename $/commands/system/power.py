import os
import sys
import time

if len(sys.argv) < 2:
    print("Usage: power [h|r|s]")
    print("	h - Hibernate")
    print("	r - Restart")
    print("	s - Shutdown")
else:
    action = sys.argv[1]
    if action == 'h':
        print("Hibernating...")
        time.sleep(1)
        os.system("shutdown /h")
    elif action == 'r':
        print("Restarting...")
        time.sleep(1)
        os.system("shutdown /r /t 0")
    elif action == 's':
        print("Shutting down...")
        time.sleep(1)
        os.system("shutdown /s /t 0")
