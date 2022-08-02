from pprint import pprint
import re
import pexpect


def send_show_cisco(host, username, password, enable_passwd, command):
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
            ssh.sendline("terminal length 10")
            ssh.expect("#")

            ssh.sendline(command)
            output = ""
            while True:
                print("page".center(40, "="))
                match_prompt = ssh.expect(
                    ["#", "--More--", pexpect.TIMEOUT], timeout=5
                )
                page = ssh.before
                page = re.sub(r" +\x08+ +\x08+", "\n", page)
                # print(page)
                output += page  # output = output + page
                if match_prompt == 0:
                    break
                elif match_prompt == 1:
                    ssh.send(" ")
                else:
                    print(">>>>> Error timeout")
                    break

            return output.replace("\r\n", "\n")
    except (pexpect.TIMEOUT, pexpect.EOF) as error:
        print(error)


if __name__ == "__main__":
    out = send_show_cisco(
        "192.168.100.1", "cisco", "cisco", "cisco", "sh run"
    )
    pprint(out, width=120)
    # with open("result.txt", "w") as f:
    #    f.write(out)
