import re
import time
from pprint import pprint
import socket
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
        auth_out = ssh.recv(max_read).decode("utf-8")
        match_prompt = re.search(r"\n(\S+#)", auth_out)
        if match_prompt:
            prompt = match_prompt.group(1)
            prompt = ">"
        else:
            prompt = "#"

        ssh.send(f"{command}\n")
        output = ""
        ssh.settimeout(5)
        while True:
            time.sleep(pause)
            try:
                part = ssh.recv(100).decode("utf-8")
            except socket.timeout:
                print("ERROR")
                break
            print("part".center(40, "="))
            pprint(part)
            output += part
            if prompt in output:
                break

        return output.replace("\r\n", "\n")


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    for ip in ip_list:
        out = send_show_cisco(ip, "cisco", "cisco", "cisco", "sh int desc")
        pprint(out, width=120)
