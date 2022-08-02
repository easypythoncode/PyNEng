from pprint import pprint
import re
import telnetlib
import time


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


def send_show_cisco(host, username, password, enable_passwd, command):
    with telnetlib.Telnet(host) as conn:
        conn.read_until(b"Username")
        conn.write(to_bytes(username))
        conn.read_until(b"Password")
        conn.write(to_bytes(password))
        conn.read_until(b">")
        conn.write(b"enable\n")
        conn.read_until(b"Password")
        conn.write(to_bytes(enable_passwd))
        conn.read_until(b"#")
        # time.sleep(1)
        # conn.read_very_eager()

        conn.write(to_bytes(command))
        output = conn.read_until(b"#", timeout=5).decode("utf-8")
        return output.replace("\r\n", "\n")


if __name__ == "__main__":
    out = send_show_cisco(
        "192.168.100.1", "cisco", "cisco", "cisco", "sh int desc"
    )
    pprint(out, width=120)
    # with open("result.txt", "w") as f:
    #    f.write(out)
