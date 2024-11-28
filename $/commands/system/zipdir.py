import os
import sys
import zipfile

def zipdir(directory, output):
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))
    print(f"Directory '{directory}' has been zipped into '{output}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zipdir.py <directory> <output.zip>")
    else:
        zipdir(sys.argv[1], sys.argv[2])
