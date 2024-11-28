import os
import shutil

print("Cleaning temporary files...")
temp = os.getenv('TEMP')
for root, dirs, files in os.walk(temp):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        shutil.rmtree(os.path.join(root, name))
os.makedirs(temp, exist_ok=True)
print("Temporary files cleaned.")
input("Press Enter to continue...")
