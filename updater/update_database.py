import json

from updater.nvd_downloader import download_cves
from updater.nvd_parser import parse_cves


print("[*] Downloading CVEs...")

data = download_cves()

print("[+] Download Complete")

parsed = parse_cves(data)

with open("database/cve.json", "w") as file:
    json.dump(parsed, file, indent=4)

print(f"[+] Saved {len(parsed)} CVEs")
