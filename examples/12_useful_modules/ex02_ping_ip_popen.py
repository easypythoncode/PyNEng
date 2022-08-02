from pprint import pprint
import subprocess as sub


def ping_ip_list(ip_list):
    pingable = []
    unpingable = []
    process_list = []
    for ip in ip_list:
        ping_process = sub.Popen(
            ["ping", "-c", "3", "-n", ip],
            stdout=sub.DEVNULL,
            stderr=sub.DEVNULL,
            encoding="utf-8",
        )
        process_list.append(ping_process)
    for ip, pr in zip(ip_list, process_list):
        returncode = pr.wait()
        print(ip, returncode)
        if returncode == 0:
            pingable.append(ip)
        else:
            unpingable.append(ip)
    return (pingable, unpingable)


ip_list = ["8.8.8.8", "8.8.4.4", "10.1.1.1", "10.2.2.2", "10.3.3.3", "10.4.4.4"]
ok, not_ok = ping_ip_list(ip_list)
pprint(ok)
pprint(not_ok)
