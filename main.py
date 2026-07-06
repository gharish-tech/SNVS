import sys
from scanner.port_scanner import scan_port
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
    
print("\n[*] Scanning Common Ports...\n")

ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]

for port in ports:
    if scan_port(target, port):
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")