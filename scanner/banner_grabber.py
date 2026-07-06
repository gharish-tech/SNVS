import socket


def grab_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        sock.connect((ip, port))

        # Send a simple HTTP request only for web servers
        if port in [80, 8080, 443]:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        return banner if banner else "No Banner"

    except Exception:
        return "Banner Not Available"