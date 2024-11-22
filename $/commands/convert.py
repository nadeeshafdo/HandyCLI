import sys
from PIL import Image

def convert(input_file, output_format):
    try:
        img = Image.open(input_file)
        output_file = f"{input_file.rsplit('.', 1)[0]}.{output_format}"
        img.save(output_file)
        print(f"Converted '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file> <output_format>")
    else:
        convert(sys.argv[1], sys.argv[2])
