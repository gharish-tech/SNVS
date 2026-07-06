import re


def parse_banner(banner):

    if not banner:
        return None, None

    # Apache
    apache = re.search(r"Apache/([\d.]+)", banner, re.IGNORECASE)
    if apache:
        return "Apache", apache.group(1)

    # OpenSSH
    openssh = re.search(r"OpenSSH[_/]([\d.]+)", banner, re.IGNORECASE)
    if openssh:
        return "OpenSSH", openssh.group(1)

    # nginx
    nginx = re.search(r"nginx/([\d.]+)", banner, re.IGNORECASE)
    if nginx:
        return "nginx", nginx.group(1)

    return None, None