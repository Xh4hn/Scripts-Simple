import sys
import socket

target = socket.gethostbyname(input("Target: "))

print("Scanning target > " + target)

try:
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        output = s.connect_ex((target, port))
        if output == 0:
            print("[+] Open Port > {}".format(port))
        s.close()
except:
    print("\n Exit...")
    sys.exit(0)
