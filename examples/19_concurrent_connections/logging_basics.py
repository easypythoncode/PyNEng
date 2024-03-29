from datetime import datetime
import logging
import netmiko
import yaml

# эта строка указывает ,что лог-сообщения paramiko юудут выводиться
# только если они уровня WARNING и выше
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
    format="%(threadName)s %(name)s %(levelname)s: %(message)s", level=logging.INFO
)


def send_show(device, show):
    start_msg = "===> {} Connection: {}"
    received_msg = "<=== {} Received:   {}"
    host = device["host"]
    logging.info(start_msg.format(datetime.now().time(), host))

    with netmiko.ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(show)
        logging.info(received_msg.format(datetime.now().time(), host))
    return result


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_show(dev, "sh clock"))
