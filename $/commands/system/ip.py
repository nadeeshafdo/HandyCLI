import subprocess

result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True)
output = result.stdout
for line in output.splitlines():
    if "IPv4" in line or "IPv6" in line:
        print(line)
