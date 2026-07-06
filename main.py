import sys
import ipaddress

if len(sys.argv) < 2:
    print("[-] Error: Target IP address is required.")
    print("Usage: py main.py <IP Address>")
    sys.exit()

target = sys.argv[1]

try:
    ipaddress.ip_address(target)
    print(f"[+] Valid Target: {target}")

except ValueError:
    print(f"[-] Invalid IP Address: {target}")
    sys.exit()
    
    