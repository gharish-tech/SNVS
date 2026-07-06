import sys
from utils.ip_validator import validate_ip
from scanner.host_discovery import is_host_alive

if len(sys.argv) < 2:
    print("Usage: python main.py <IP>")
    sys.exit()

target = sys.argv[1]

if not validate_ip(target):
    print("[-] Invalid IP Address")
    sys.exit()

print("[+] Valid Target:", target)

print("[*] Checking if host is alive...")

if is_host_alive(target):
    print("[+] Host is Alive")
else:
    print("[-] Host is Down or Blocking Ping")
    