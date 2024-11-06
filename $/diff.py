import sys

def diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()
        
    for line in f1_lines:
        if line not in f2_lines:
            print(f"- {line.strip()}")
    for line in f2_lines:
        if line not in f1_lines:
            print(f"+ {line.strip()}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
    else:
        diff(sys.argv[1], sys.argv[2])
