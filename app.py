from flask import Flask, render_template, request

from flask import send_file
from scanner.host_discovery import is_host_alive
from scanner.port_scanner import scan_port
from scanner.banner_grabber import grab_banner

from utils.ip_validator import validate_ip
from utils.services import get_service_name
from utils.version_parser import parse_banner
from utils.report_generator import generate_report

from vulnerability.cve_checker import check_vulnerability

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    results = []

    if request.method == "POST":

        target = request.form["ip"]

        if not validate_ip(target):
            return render_template(
                "index.html",
                error="Invalid IP Address"
            )

        if not is_host_alive(target):
            return render_template(
                "index.html",
                error="Host is Down"
            )

        ports = [21,22,23,25,53,80,110,143,443,3306,3389,8080]

        for port in ports:

            if scan_port(target, port):

                service = get_service_name(port)

                banner = grab_banner(target, port)

                service_name, version = parse_banner(banner)

                vulns = []

                if service_name and version:
                    vulns = check_vulnerability(service_name, version)

                results.append({

                    "port": port,
                    "service": service,
                    "banner": banner,
                    "detected": service_name,
                    "version": version,
                    "vulnerabilities": vulns

                })

        # Generate Report
        report_file = generate_report(target, results)

        return render_template(
            "index.html",
            target=target,
            results=results,
            report=report_file.split("/")[-1]
        )

    return render_template("index.html")



from flask import send_from_directory
import os


@app.route("/Reports/<filename>")
def download_report(filename):

    reports_folder = os.path.join(app.root_path, "Reports")

    return send_from_directory(
        reports_folder,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    