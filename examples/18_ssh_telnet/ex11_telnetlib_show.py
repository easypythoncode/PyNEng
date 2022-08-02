from pprint import pprint
import re
import telnetlib
import time


def send_show_cisco(host, username, password, enable_passwd, command):
    with telnetlib.Telnet(host) as conn:
        conn.read_until(b"Username")
        conn.write(f"{username}\n".encode("utf-8"))
        conn.read_until(b"Password")
        conn.write(f"{password}\n".encode("utf-8"))
        conn.read_until(b">")
        conn.write(b"enable\n")
        conn.read_until(b"Password")
        conn.write(f"{enable_passwd}\n".encode("utf-8"))
        conn.read_until(b"#")
        # time.sleep(1)
        # conn.read_very_eager()

        conn.write(f"{command}\n".encode("utf-8"))
        output = conn.read_until(b"#").decode("utf-8")
        return output.replace("\r\n", "\n")


if __name__ == "__main__":
    out = send_show_cisco(
        "192.168.100.1", "cisco", "cisco", "cisco", "sh int desc"
    )
    pprint(out, width=120)
    # with open("result.txt", "w") as f:
    #    f.write(out)
