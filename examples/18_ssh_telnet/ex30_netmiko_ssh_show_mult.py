from pprint import pprint
import yaml
import netmiko
import socket
from netmiko import (
    Netmiko,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_show(device, commands):
    try:
        with Netmiko(**device) as ssh:
            ssh.enable()
            result = {}
            if type(commands) == str:
                commands = [commands]
            for cmd in commands:
                output = ssh.send_command(cmd)
                result[cmd] = output
        return result
    except socket.timeout as error:
        print(f"Не удалось подключиться к {device['host']}")
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        for device in devices:
            out = send_show(device, "sh ip int br")
            pprint(out)
