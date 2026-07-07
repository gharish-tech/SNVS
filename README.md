# 🛡️ SNVS v2.0

## Service & Version Vulnerability Scanner

SNVS (Service & Version Vulnerability Scanner) is a Python-based cybersecurity tool that scans a target host, detects running services and software versions, and matches them against a local CVE database to identify known vulnerabilities.

---

## Features

- ✅ Host Discovery
- ✅ Port Scanning
- ✅ Banner Grabbing
- ✅ Service Detection
- ✅ Version Detection
- ✅ Local CVE Database
- ✅ Vulnerability Matching
- ✅ Flask Web Dashboard
- ✅ Download Scan Reports
- ✅ NVD CVE Links

---

## Technologies Used

- Python 3
- Flask
- Socket Programming
- JSON
- HTML
- CSS
- JavaScript

---

## Project Structure

```
SNVS/
│
├── app.py
├── main.py
├── database/
├── scanner/
├── updater/
├── utils/
├── vulnerability/
├── templates/
├── static/
├── Reports/
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SNVS.git
```

Go into the project

```bash
cd SNVS
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## Workflow

```
Target IP
     │
     ▼
Host Discovery
     │
     ▼
Port Scanner
     │
     ▼
Banner Grabber
     │
     ▼
Version Detection
     │
     ▼
CVE Matching
     │
     ▼
Risk Report
```

---

## Example

Target

```
192.168.85.128
```

Detected

```
Apache 2.2.8
```

Result

```
CVE-2007-6420
Severity : High
CVSS : 7.5
```

---

## Future Improvements

- PDF Reports
- HTML Reports
- Scan Progress Bar
- Top 1000 Ports
- Custom Port Range
- OS Detection
- Multi-threaded Scanning
- Search & Filter
- Docker Support

---

## Author

Harish

Cybersecurity | Python | Networking

---