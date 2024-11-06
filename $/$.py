import os

print("Custom Command List")
print("-------------------")
files = [f for f in os.listdir(os.path.dirname(__file__)) if f != '$.bat']
for file in files:
    print(file)
