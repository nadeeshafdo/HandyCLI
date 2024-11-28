import sys
import os

BASE_DIR = os.path.dirname(__file__)
COMMAND_DIRS = [
    os.path.join(BASE_DIR, "commands", "user"),
    os.path.join(BASE_DIR, "commands", "shared"),
    os.path.join(BASE_DIR, "commands", "system"),
    os.path.join(BASE_DIR, "commands", "test")
]

def main():
    if len(sys.argv) < 2:
        print("Usage: $ <command> [args]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]
    
    # Search for the command in the directories
    for directory in COMMAND_DIRS:
        script_path = os.path.join(directory, f"{command}.py")
        if os.path.exists(script_path):
            os.system(f"python {script_path} {' '.join(args)}")
            return
    
    print(f"Command '{command}' not found.")
    sys.exit(1)

if __name__ == "__main__":
    main()
