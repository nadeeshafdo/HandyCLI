import subprocess
import sys

def show_proxy():
    return subprocess.run(["netsh", "winhttp", "show", "proxy"], capture_output=True, text=True)

def reset_proxy():
    return subprocess.run(["netsh", "winhttp", "reset", "proxy"], capture_output=True, text=True)

def import_proxy():
    return subprocess.run(["netsh", "winhttp", "import", "proxy", "source=ie"], capture_output=True, text=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: proxy.py [show|reset|import]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "show":
        print(show_proxy().stdout)
    elif command == "reset":
        print(reset_proxy().stdout)
    elif command == "import":
        print(import_proxy().stdout)
    else:
        print("Invalid command. Usage: proxy.py [show|reset|import]")
        sys.exit(1)

if __name__ == "__main__":
    main()
