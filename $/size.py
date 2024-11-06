import os
import sys

def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            total_size += os.path.getsize(os.path.join(dirpath, filename))
    return total_size

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python size.py <file_or_directory>")
    else:
        path = sys.argv[1]
        size = get_size(path)
        print(f"Size of '{path}': {size} bytes")
