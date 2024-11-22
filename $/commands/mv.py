import os
import sys
import shutil

def move(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved '{src}' to '{dest}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mv.py <source> <destination>")
    else:
        move(sys.argv[1], sys.argv[2])
