import platform
import psutil

def sysinfo():
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

if __name__ == "__main__":
    sysinfo()
