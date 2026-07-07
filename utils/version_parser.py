import re

PATTERNS = [

    ("Apache", r"Apache/([\d.]+)"),

    ("OpenSSH", r"OpenSSH[_/]([\d.]+)"),

    ("nginx", r"nginx/([\d.]+)"),

    ("Microsoft-IIS", r"Microsoft-IIS/([\d.]+)"),

    ("FileZilla", r"FileZilla(?: Server)?[/ ]([\d.]+)"),

    ("MySQL", r"MySQL[/ -]?([\d.]+)"),

    ("PostgreSQL", r"PostgreSQL[/ ]([\d.]+)"),

    ("Redis", r"Redis[_/ ]([\d.]+)"),

    ("Tomcat", r"Apache Tomcat/([\d.]+)"),

    ("ProFTPD", r"ProFTPD[\s/]([\d.]+)"),

    ("vsFTPd", r"vsFTPd[\s/]([\d.]+)")
]


def parse_banner(banner):

    if not banner:
        return None, None

    for service, pattern in PATTERNS:

        match = re.search(pattern, banner, re.IGNORECASE)

        if match:
            return service, match.group(1)

    return None, None