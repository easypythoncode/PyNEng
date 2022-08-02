from pprint import pprint
import subprocess as sub


def ping_ip(ip):
    print(f"Пингую адрес {ip}...")
    ping = sub.run(
        ["ping", "-c", "3", "-n", ip],
        stdout=sub.DEVNULL,
        stderr=sub.DEVNULL,
        encoding="utf-8",
    )
    # output = ping.stdout + ping.stderr
    # pprint(output)
    if ping.returncode == 0:
        return True
    else:
        return False


print(ping_ip("8.8.8.8"))
print(ping_ip("10.1.1.1"))
