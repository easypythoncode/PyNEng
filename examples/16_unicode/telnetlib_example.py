from pprint import pprint
import telnetlib
import time

t = telnetlib.Telnet('192.168.100.1')
cmd = 'sh ip int br\n'

t.read_until(b'Username:')
t.write(b'cisco\n')

t.read_until(b'Password:')
# t.read_until('Password:'.encode("utf-8"))
t.write(b'cisco\n')
t.write(cmd.encode("utf-8"))

time.sleep(5)

b_output = t.read_very_eager()
pprint(b_output)
output = b_output.decode('utf-8')
pprint(output, width=120)
