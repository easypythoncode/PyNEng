from pprint import pprint
import socket
import yaml
from netmiko import Netmiko, NetmikoAuthenticationException, NetmikoBaseException


def send_show(device_dict, command):
    try:
        with Netmiko(**device_dict) as conn:
            conn.enable()
            output = conn.send_command(command)
            return output
    except (NetmikoAuthenticationException, socket.timeout) as error:
        print(f"Ошибка {error} при подключении к {device_dict['host']}")
    except NetmikoBaseException as error:
        print(f"Ошибка netmiko {error} при подключении к {device_dict['host']}")


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        for device in devices:
            out = send_show(device, "sh int desc")
            pprint(out)
