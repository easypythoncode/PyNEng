from pprint import pprint
import pexpect


def send_show_cisco(host, username, password, enable_passwd, command):
    print(f"Подключаюсь к {host}")
    cmd_output_dict = {}
    try:
        with pexpect.spawn(
                f"ssh {username}@{host}", encoding="utf-8", timeout=10
        ) as ssh:
            ssh.expect("Password")
            ssh.sendline(password)
            ssh.expect(">")
            ssh.sendline("enable")
            ssh.expect("Password")
            ssh.sendline(enable_passwd)
            ssh.expect("#")
            ssh.sendline("terminal length 0")
            ssh.expect("#")

            if type(command) == str:
                command = [command]

            for cmd in command:
                ssh.sendline(cmd)
                ssh.expect("#")
                output = ssh.before
                cmd_output_dict[cmd] = output.replace("\r\n", "\n")

        return cmd_output_dict
    except (pexpect.TIMEOUT, pexpect.EOF) as error:
        print(error)


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.1"]
    for ip in ip_list:
        out = send_show_cisco(
            ip, "cisco", "cisco", "cisco", ["sh clock", "sh int desc"]
        )
        pprint(out, width=120)
