import platform, psutil

def getPCSpec():
    print("  OS:",platform.system())
    print("  Processor:",platform.processor())
    print("  CPU Core:",psutil.cpu_count(logical=True))
    print("  Memory:",round(psutil.virtual_memory().total / (1024*1024*1024), ndigits=2), "GB")