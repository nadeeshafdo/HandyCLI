import sys
import re

def grep(pattern, file):
    try:
        with open(file, 'r') as f:
            for i, line in enumerate(f, start=1):
                if re.search(pattern, line):
                    print(f"{i}: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <file>")
    else:
        grep(sys.argv[1], sys.argv[2])
