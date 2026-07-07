import sys

from scanner.banner_grabber import grab_banner
from scanner.host_discovery import is_host_alive
from scanner.port_scanner import scan_port

from utils.ip_validator import validate_ip
from utils.services import get_service_name
from utils.version_parser import parse_banner

from vulnerability.cve_checker import check_vulnerability


# ==========================================================
# Banner
# ==========================================================

print("=" * 70)
print("        SNVS v1.0 - Service & Version Vulnerability Scanner")
print("=" * 70)
print("Author      : Harish")
print("Language    : Python")
print("Version     : 1.0")
print("=" * 70)
print()


# ==========================================================
# Counters
# ==========================================================

open_ports = 0
services_found = 0
vulnerabilities_found = 0


# ==========================================================
# Input Validation
# ==========================================================

if len(sys.argv) < 2:
    print("Usage: py main.py <IP Address>")
    sys.exit()

target = sys.argv[1]

if not validate_ip(target):
    print("[-] Invalid IP Address")
    sys.exit()


# ==========================================================
# Host Discovery
# ==========================================================

print(f"Target IP   : {target}")
print()

print("[*] Checking Host Status...")

if is_host_alive(target):
    print("[+] Host Status : Alive")
else:
    print("[-] Host Status : Down")
    sys.exit()

print()


# ==========================================================
# Port Scan
# ==========================================================

ports = [
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    143,
    443,
    3306,
    3389,
    8080,
]

print("[*] Scanning Common Ports...\n")

for port in ports:

    if scan_port(target, port):

        open_ports += 1

        service = get_service_name(port)

        banner = grab_banner(target, port)

        service_name, version = parse_banner(banner)

        if service_name and version:
            services_found += 1

        print("=" * 70)
        print(f"PORT        : {port}")
        print(f"STATE       : OPEN")
        print(f"SERVICE     : {service}")
        print(f"BANNER      : {banner}")
        print(f"DETECTED    : {service_name}")
        print(f"VERSION     : {version}")

        if service_name and version:

            results = check_vulnerability(service_name, version)

            if results:

                vulnerabilities_found += len(results)

                print("\nVULNERABILITIES FOUND")
                print("-" * 70)

                for cve in results:

                    print(f"CVE ID         : {cve['id']}")
                    print(f"Severity       : {cve['severity']}")
                    print(f"CVSS Score     : {cve['cvss']}")
                    print(f"Description    : {cve['description']}")
                    print(f"Recommendation : {cve['fix']}")
                    print("-" * 70)

            else:
                print("\nNo Known Vulnerabilities Found")

        else:
            print("\nService Version Not Identified")

    else:

        print(f"[-] Port {port:<5} CLOSED")


# ==========================================================
# Scan Summary
# ==========================================================

print("\n")
print("=" * 70)
print("                        SCAN SUMMARY")
print("=" * 70)

print(f"Target IP               : {target}")
print(f"Open Ports              : {open_ports}")
print(f"Services Detected       : {services_found}")
print(f"Vulnerabilities Found   : {vulnerabilities_found}")

print("=" * 70)
print("Scan Completed Successfully!")
print("=" * 70)
