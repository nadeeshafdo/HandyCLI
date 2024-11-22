import os
import sys
import subprocess

def run_command(command, *args):
    """
    Executes a script from the 'commands' directory with optional arguments.
    If the script is not found, it prints an error message.

    Parameters:
        command (str): Name of the command to execute.
        *args: Additional arguments for the script.
    """
    # Define the path to the 'commands' directory
    commands_dir = os.path.join(os.path.dirname(__file__), "commands")
    command_file = os.path.join(commands_dir, f"{command}.py")

    # Check if the command exists
    if os.path.isfile(command_file):
        try:
            # Construct the command with arguments
            full_command = ["python", command_file] + list(args)
            # Run the command
            subprocess.run(full_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to execute {command}.py. {e}")
    else:
        # If command doesn't exist, print an error message
        print(f"'{command}' is not recognized as an internal or external command, \noperable program or batch file.~HandyCLI")

def list_commands():
    """Lists all available commands in the 'commands' directory."""
    commands_dir = os.path.join(os.path.dirname(__file__), "commands")
    try:
        # List all .py files in the 'commands' directory (ignores non-Python files)
        command_files = [f[:-3] for f in os.listdir(commands_dir) if f.endswith(".py")]
        if command_files:
            print("Available commands:")
            for cmd in command_files:
                print(f"  - {cmd}")
        else:
            print("No commands found in the 'commands' directory.")
    except FileNotFoundError:
        print("Error: 'commands' directory not found.")

def show_help():
    """Runs the help.py script."""
    commands_dir = os.path.join(os.path.dirname(__file__), "commands")
    help_file = os.path.join(commands_dir, "help.py")
    if os.path.isfile(help_file):
        try:
            subprocess.run(["python", help_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to execute help.py. {e}")
    else:
        print("Error: help.py script not found in the 'commands' directory.")

if __name__ == "__main__":
    # Check if any command is provided
    if len(sys.argv) < 2:
        print("Usage: $ <command> [args...]")
        sys.exit(1)

    # Extract the command and arguments
    command_name = sys.argv[1]

    # Handle specific flags: --list and --help
    if command_name == "--list":
        list_commands()
    elif command_name == "--help":
        show_help()
    else:
        # Run the command with any arguments passed
        command_args = sys.argv[2:]
        run_command(command_name, *command_args)
