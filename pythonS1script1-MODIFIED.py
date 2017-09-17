import getpass
import sys
import telnetlib

router_list = [
{'ip':'192.168.111.1','login':'admin','password':'cisco'},
{'ip':'192.168.111.2','login':'admin','password':'cisco'}
]


for r in router_list:
  HOST = r['ip']
  user = r['login']
  password = r['password']

  tn = telnetlib.Telnet(HOST)
  tn.read_until("Username: ")
  tn.write(user + "\n")
  tn.write(password + "\n")

  tn.write("enable\n")
  #tn.write("cisco\n")
  tn.write("conf t\n")
  tn.write("hostname MODIFIED_FTOM_TELNET\n")
  tn.write("interface loopback 0\n")
  tn.write("description FROM_TELNET_SCRIPT\n")
  tn.write("ip address 1.1.1.1 255.255.255.255\n")
  tn.write("exit\n")
  tn.write("end\n")
  tn.write("exit\n")

  print tn.read_all()
