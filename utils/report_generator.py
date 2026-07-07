from datetime import datetime
import os


def generate_report(target, results):

    os.makedirs("Reports", exist_ok=True)

    filename = f"Reports/report_{target}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("SNVS v1.0 Scan Report\n")
        file.write("=" * 70 + "\n\n")

        file.write(f"Target      : {target}\n")
        file.write(f"Scan Time   : {datetime.now()}\n\n")

        for item in results:

            file.write("-" * 70 + "\n")
            file.write(f"Port      : {item['port']}\n")
            file.write(f"Service   : {item['service']}\n")
            file.write(f"Version   : {item['version']}\n\n")

            if item["vulnerabilities"]:

                file.write("Vulnerabilities\n\n")

                for cve in item["vulnerabilities"]:

                    file.write(f"CVE         : {cve['id']}\n")
                    file.write(f"Severity    : {cve['severity']}\n")
                    file.write(f"CVSS        : {cve['cvss']}\n")
                    file.write(f"Description : {cve['description']}\n")
                    file.write(f"Fix         : {cve['fix']}\n")
                    file.write("\n")

            else:

                file.write("No Vulnerabilities Found.\n\n")

    return filename