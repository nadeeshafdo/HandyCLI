import sys

if len(sys.argv) < 2:
    print("Usage: cat.py filename")
else:
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        print(file.read())
