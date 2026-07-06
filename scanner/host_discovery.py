import platform
import subprocess


def is_host_alive(ip):
    """
    Returns True if host responds to ping.
    """

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", ip]
    else:
        command = ["ping", "-c", "1", ip]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return result.returncode == 0