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


ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "10.2.2.2"]
for ip in ip_list:
    status = ping_ip(ip)
    print(f"{ip=} {status=}")
