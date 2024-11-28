import subprocess
import sys


def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"


def get_winhttp_proxy():
    command = ["netsh", "winhttp", "show", "proxy"]
    output = run_command(command)
    return output


def import_ie_proxy():
    command = ["netsh", "winhttp", "import", "proxy", "source=ie"]
    output = run_command(command)
    return output


def reset_winhttp_proxy():
    command = ["netsh", "winhttp", "reset", "proxy"]
    output = run_command(command)
    return output


def set_git_proxy(http_proxy=None, https_proxy=None, socks_proxy=None):
    if http_proxy:
        run_command(["git", "config", "--global", "http.proxy", http_proxy])
    if https_proxy:
        run_command(["git", "config", "--global", "https.proxy", https_proxy])
    if socks_proxy:
        run_command(["git", "config", "--global", "socks.proxy", socks_proxy])


def get_git_proxy():
    http_proxy = run_command(["git", "config", "--global", "http.proxy"])
    https_proxy = run_command(["git", "config", "--global", "https.proxy"])
    socks_proxy = run_command(["git", "config", "--global", "socks.proxy"])
    return {
        "http": http_proxy if http_proxy else "Not Set",
        "https": https_proxy if https_proxy else "Not Set",
        "socks": socks_proxy if socks_proxy else "Not Set",
    }


def reset_git_proxy():
    run_command(["git", "config", "--global", "--unset", "http.proxy"])
    run_command(["git", "config", "--global", "--unset", "https.proxy"])
    run_command(["git", "config", "--global", "--unset", "socks.proxy"])
    return "Git proxy settings reset."


def main():
    if len(sys.argv) < 2:
        print("Usage: proxy.py [show|reset|import|set] [sys|git] [proxy URLs]")
        sys.exit(1)

    command = sys.argv[1].lower()
    scope = sys.argv[2].lower() if len(sys.argv) > 2 else None

    if command == "show":
        if scope == "sys":
            print("[System Proxy Settings]")
            print(get_winhttp_proxy())
        elif scope == "git":
            print("[Git Proxy Settings]")
            proxies = get_git_proxy()
            print(f"  HTTP Proxy: {proxies['http']}")
            print(f"  HTTPS Proxy: {proxies['https']}")
            print(f"  SOCKS Proxy: {proxies['socks']}")
        else:
            print("[System Proxy Settings]")
            print(get_winhttp_proxy())
            print("\n[Git Proxy Settings]")
            proxies = get_git_proxy()
            print(f"  HTTP Proxy: {proxies['http']}")
            print(f"  HTTPS Proxy: {proxies['https']}")
            print(f"  SOCKS Proxy: {proxies['socks']}")

    elif command == "import":
        if scope == "sys":
            print(import_ie_proxy())
        elif scope == "git":
            print("Import functionality not supported for Git proxy.")
        else:
            print(import_ie_proxy())

    elif command == "reset":
        if scope == "sys":
            print(reset_winhttp_proxy())
        elif scope == "git":
            print(reset_git_proxy())
        else:
            print(reset_winhttp_proxy())
            print(reset_git_proxy())

    elif command == "set":
        if scope == "git":
            http_proxy = sys.argv[3] if len(sys.argv) > 3 else None
            https_proxy = sys.argv[4] if len(sys.argv) > 4 else None
            socks_proxy = sys.argv[5] if len(sys.argv) > 5 else None
            set_git_proxy(http_proxy, https_proxy, socks_proxy)
            print("Git proxy settings updated.")
        else:
            print("Setting system proxy is not supported through this script.")

    else:
        print("Invalid command. Usage: proxy.py [show|reset|import|set] [sys|git] [proxy URLs]")
        sys.exit(1)


if __name__ == "__main__":
    main()
