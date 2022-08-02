from pprint import pprint
import yaml
import netmiko
import socket
from netmiko import (
    Netmiko,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


def send_cfg(device, commands):
    try:
        with Netmiko(**device) as ssh:
            ssh.enable()
            result = ssh.send_config_set(commands, error_pattern="%")
            return result.replace("\r\n", "\n")
    except socket.timeout as error:
        print(f"Не удалось подключиться к {device['host']}")
    except NetmikoAuthenticationException:
        print(f"Ошибка аутентификации с {device['host']}")


if __name__ == "__main__":
    commands = {
        "192.168.100.1": ["int lo9", "ipaddress 10.90.90.1 255.255.255.255"],
        "192.168.100.2": ["int lo9"],
        "192.168.100.3": ["int lo9"],
    }
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        for device in devices:
            try:
                out = send_cfg(
                    device, commands[device['host']]
                )
                pprint(out)
            except ValueError as error:
                print(error)
