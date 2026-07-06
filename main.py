import sys
from utils.version_parser import parse_banner
from vulnerability.cve_checker import check_vulnerability
from scanner.banner_grabber import grab_banner
from utils.services import get_service_name
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
    
ports = [21,22,23,25,53,80,110,143,443,3306,3389,8080]

print("\n[*] Scanning Common Ports...\n")

for port in ports:

    if scan_port(target, port):

        service = get_service_name(port)

        banner = grab_banner(target, port)

        print(f"[+] {port:<6} OPEN     {service}")
        print(f"    Banner: {banner}\n")

        service_name, version = parse_banner(banner)

        if service_name and version:

            result = check_vulnerability(service_name, version)

            if result:

                print("[!] Vulnerability Found")
                print(f"CVE         : {result['cve']}")
                print(f"Severity    : {result['severity']}")
                print(f"CVSS        : {result['cvss']}")
                print(f"Description : {result['description']}")
                print(f"Fix         : {result['fix']}")
                print()

    else:

        print(f"[-] {port:<6} CLOSED")
        
        