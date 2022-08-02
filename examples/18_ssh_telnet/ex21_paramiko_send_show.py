import time
from pprint import pprint
import paramiko


def send_show_cisco(
        host,
        username,
        password,
        enable_passwd,
        command,
        max_read=1000000,
        timeout=5,
        pause=0.5,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=host,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with cl.invoke_shell() as ssh:
        ssh.settimeout(timeout)
        ssh.send("enable\n")
        time.sleep(pause)
        ssh.send(f"{enable_passwd}\n")
        ssh.send("terminal length 0\n")
        time.sleep(pause)
        ssh.recv(max_read)

        ssh.send(f"{command}\n")
        time.sleep(pause)
        output = ssh.recv(max_read).decode("utf-8").replace("\r\n", "\n")
        return output


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.1"]
    for ip in ip_list:
        out = send_show_cisco(ip, "cisco", "cisco", "cisco", "sh ip int br")
        pprint(out, width=120)
