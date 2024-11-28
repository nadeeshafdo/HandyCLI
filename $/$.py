import os
import sys
import subprocess

BASE_DIR = os.path.dirname(__file__)
COMMAND_DIRS = [
    os.path.join(BASE_DIR, "commands", "user"),
    os.path.join(BASE_DIR, "commands", "shared"),
    os.path.join(BASE_DIR, "commands", "system")
]

REPO_URL = "https://github.com/nadeeshafdo/HandyCLI"
LOCAL_REPO_DIR = BASE_DIR

def update_directory_from_repo():
    """
    Checks if the local repository is up to date with the remote one.
    Clones or pulls changes only if updates are available.
    """
    if not os.path.exists(os.path.join(LOCAL_REPO_DIR, ".git")):
        # Clone the repository if it's not already present
        print("Cloning the repository...")
        subprocess.run(["git", "clone", REPO_URL, LOCAL_REPO_DIR], check=True)
    else:
        # Check if there are updates in the remote repository
        print("Checking for updates...")
        os.chdir(LOCAL_REPO_DIR)
        subprocess.run(["git", "fetch"], check=True)
        result = subprocess.run(
            ["git", "status", "-uno"],
            capture_output=True, text=True, check=True
        )
        if "Your branch is up to date" not in result.stdout:
            print("Updates found! Pulling changes...")
            subprocess.run(["git", "pull"], check=True)
        else:
            print("The directory is already up to date.")

def main():
    if len(sys.argv) < 2:
        print("Usage: $ <command> [args]")
        sys.exit(1)

    # Ensure the repository is up to date
    update_directory_from_repo()

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
