import os
import sys
import subprocess
import shutil

BASE_DIR = os.path.dirname(__file__)
COMMAND_DIRS = [
    os.path.join(BASE_DIR, "commands", "user"),
    os.path.join(BASE_DIR, "commands", "shared"),
    os.path.join(BASE_DIR, "commands", "system"),
]

REPO_URL = "https://github.com/nadeeshafdo/HandyCLI"
LOCAL_REPO_DIR = BASE_DIR


def is_git_installed():
    """Check if Git is installed and available."""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False


def update_directory_from_repo():
    """Updates the HandyCLI directory from the remote GitHub repository."""
    if not is_git_installed():
        print("Error: Git is not installed. Please install Git to use the update feature.")
        sys.exit(1)

    try:
        if not os.path.exists(os.path.join(LOCAL_REPO_DIR, ".git")):
            print("Cloning the HandyCLI repository...")
            subprocess.run(["git", "clone", REPO_URL, LOCAL_REPO_DIR], check=True)
            print("HandyCLI repository cloned successfully.")
        else:
            print("Checking for updates to HandyCLI...")
            os.chdir(LOCAL_REPO_DIR)
            subprocess.run(["git", "fetch"], check=True)
            status_result = subprocess.run(
                ["git", "status", "-uno"], capture_output=True, text=True, check=True
            )
            if "Your branch is up to date" in status_result.stdout:
                print("HandyCLI is already up to date.")
            else:
                print("Updates found! Pulling the latest changes...")
                subprocess.run(["git", "pull"], check=True)
                print("HandyCLI has been updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
        sys.exit(1)


def execute_command(command, args):
    """Execute the given command."""
    for directory in COMMAND_DIRS:
        script_path = os.path.join(directory, f"{command}.py")
        if os.path.exists(script_path):
            try:
                subprocess.run(["python", script_path, *args], check=True)
                return
            except subprocess.CalledProcessError as e:
                print(f"Error running command '{command}': {e}")
                sys.exit(1)
    print(f"Command '{command}' not found.")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: $ <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "update":
        update_directory_from_repo()
        return

    args = sys.argv[2:]
    execute_command(command, args)


if __name__ == "__main__":
    main()
