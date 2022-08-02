from pprint import pprint
import pexpect


def send_cfg_cisco(
        host, username, password, enable_passwd, commands, timeout=5
):
    print(f"Подключаюсь к {host}")
    cmd_output = ""
    try:
        with pexpect.spawn(
                f"ssh {username}@{host}", encoding="utf-8", timeout=timeout
        ) as ssh:
            ssh.expect("Password")
            ssh.sendline(password)
            enable_mode = ssh.expect([">", "#"])

            if enable_mode == 0:
                ssh.sendline("enable")
                ssh.expect("Password")
                ssh.sendline(enable_passwd)
                ssh.expect("#")
            ssh.sendline("terminal length 0")
            ssh.expect("#")

            if type(commands) == str:
                commands = ["conf t", commands, "end"]
            else:
                commands = ["conf t", *commands, "end"]

            for cmd in commands:
                ssh.sendline(cmd)
                ssh.expect("#")
                output = ssh.before
                cmd_output += output
                if "%" in output:
                    print(f"При выполнении команды {cmd} возникла ошибка")
                    print(output)
                    break

        return cmd_output.replace("\r\n", "\n")
    except (pexpect.TIMEOUT, pexpect.EOF) as error:
        print(error)


if __name__ == "__main__":
    ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
    cmd_list = ["intrface lo200", "ip address 10.2.2.2 255.255.255.255"]
    for ip in ip_list:
        out = send_cfg_cisco(
            ip, "cisco", "cisco", "cisco", cmd_list, timeout=20
        )
        pprint(out, width=120)
        break
