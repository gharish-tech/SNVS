import sys
from utils.ip_validator import validate_ip

if len(sys.argv) < 2:
    print("[-] Error: Target IP address is required.")
    print("Usage: python main.py <IP Address>")
    sys.exit()

target = sys.argv[1]

if not validate_ip(target):
    print("[-] Invalid IP Address")
    sys.exit()

print("[+] Valid Target:", target)

    
    