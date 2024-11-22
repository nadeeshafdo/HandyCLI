import os
import sys
import time

def touch(file_path):
    """
    Simulates the `touch` command: Creates the file if it doesn't exist, or updates its modification time if it does.
    """
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Update the modification and access times to the current time
            os.utime(file_path, None)
        else:
            # Create an empty file
            with open(file_path, 'w') as f:
                pass
        print(f"'{file_path}' has been touched.")
    except Exception as e:
        print(f"Error touching file '{file_path}': {e}")

# Get the file path(s) from the command line arguments
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: touch <file1> <file2> ...")
    else:
        for file_path in sys.argv[1:]:
            touch(file_path)
