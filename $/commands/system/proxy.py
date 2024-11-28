import re
import subprocess
import sys

# Utility function to execute a command
def exec(cmd):
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Show command related functions
def getSysProxies():
    """Retrieve system proxy settings."""
    print("[System Proxy Settings]")
    output = exec(["netsh", "winhttp", "show", "proxy"])
    print(output)
    return output

def getGitProxies():
    """Retrieve Git proxy settings."""
    print("[Git Proxy Settings]")
    http_proxy = exec(["git", "config", "--global", "http.proxy"])
    https_proxy = exec(["git", "config", "--global", "https.proxy"])
    socks_proxy = exec(["git", "config", "--global", "socks.proxy"])
    print(f"http.proxy: {http_proxy}")
    print(f"https.proxy: {https_proxy}")
    print(f"socks.proxy: {socks_proxy}")
    return {"http.proxy": http_proxy, "https.proxy": https_proxy, "socks.proxy": socks_proxy}

def getAllProxies():
    """Retrieve both system and Git proxy settings."""
    getSysProxies()
    getGitProxies()

# Import command related functions
def setSysProxies():
    """Import system proxy settings from Internet Explorer."""
    print("[Importing System Proxy Settings]")
    output = exec(["netsh", "winhttp", "import", "proxy", "source=ie"])
    print(output)
    return output

def setGitProxies():
    """Set Git proxy settings based on system proxy."""
    print("[Importing Git Proxy Settings]")
    sys_proxy = exec(["netsh", "winhttp", "show", "proxy"])
    match = re.search(r"Proxy Server\(s\)\s*:\s*(.*)", sys_proxy)
    if match:
        proxies = match.group(1).strip().split(";")
        for proxy in proxies:
            if proxy.startswith("http="):
                exec(["git", "config", "--global", "http.proxy", proxy.split("=")[1]])
            elif proxy.startswith("https="):
                exec(["git", "config", "--global", "https.proxy", proxy.split("=")[1]])
            elif proxy.startswith("socks="):
                exec(["git", "config", "--global", "socks.proxy", proxy.split("=")[1]])
        print("Git proxies imported successfully.")
    else:
        print("No system proxy found to import for Git.")

def setAllProxies():
    """Set both system and Git proxy settings."""
    setSysProxies()
    setGitProxies()

# Reset command related functions
def unsetSysProxies():
    """Reset system proxy settings."""
    print("[Resetting System Proxy Settings]")
    output = exec(["netsh", "winhttp", "reset", "proxy"])
    print(output)
    return output

def unsetGitProxies():
    """Reset Git proxy settings."""
    print("[Resetting Git Proxy Settings]")
    exec(["git", "config", "--global", "--unset", "http.proxy"])
    exec(["git", "config", "--global", "--unset", "https.proxy"])
    exec(["git", "config", "--global", "--unset", "socks.proxy"])
    print("Git proxies reset successfully.")

def unsetAllProxies():
    """Reset both system and Git proxy settings."""
    unsetSysProxies()
    unsetGitProxies()

# Main body of the program
def main():
    if len(sys.argv) < 3:
        print("Usage: proxy [show|import|reset] sys|git|all")
        sys.exit(1)

    command = sys.argv[1].lower()
    scope = sys.argv[2].lower()

    if command == "show":
        if scope == "sys":
            getSysProxies()
        elif scope == "git":
            getGitProxies()
        elif scope == "all":
            getAllProxies()
        else:
            print("Invalid scope. Usage: proxy show sys|git|all")

    elif command == "import":
        if scope == "sys":
            setSysProxies()
        elif scope == "git":
            setGitProxies()
        elif scope == "all":
            setAllProxies()
        else:
            print("Invalid scope. Usage: proxy import sys|git|all")

    elif command == "reset":
        if scope == "sys":
            unsetSysProxies()
        elif scope == "git":
            unsetGitProxies()
        elif scope == "all":
            unsetAllProxies()
        else:
            print("Invalid scope. Usage: proxy reset sys|git|all")

    else:
        print("Invalid command. Usage: proxy [show|import|reset] sys|git|all")

if __name__ == "__main__":
    main()
