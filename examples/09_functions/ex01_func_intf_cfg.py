db_name = "dhcp.db"


def gen_intf_cfg(intf, ip_mask):
    template = f"interface {intf}\n ip address {ip_mask}"
    return template


intf1 = gen_intf_cfg("Gi0/1", "10.1.1.1 255.255.255.255")
intf2 = gen_intf_cfg("Gi0/2", "10.2.2.1 255.255.255.255")
intf3 = gen_intf_cfg("Gi0/3", "10.3.3.1 255.255.255.255")

print(intf1)
print(intf2)
print(intf3)
print("outside func", db_name)
