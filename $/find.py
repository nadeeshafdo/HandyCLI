import os
import sys
import fnmatch

def find(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            if fnmatch.fnmatch(name, pattern):
                print(os.path.join(root, name))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: find <directory> <pattern>")
    else:
        find(sys.argv[1], sys.argv[2])
