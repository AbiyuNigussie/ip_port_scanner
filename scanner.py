#!/bin/python3

import sys
import socket 

from datetime import datetime as dt

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else: 
	print("Invalid amount of arguements. ")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()

print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+ str(dt.now()))
print("-" * 50)

try:
	common_ports = [ 20, 21, 22, 53, 80, 443, 4444, 5431, 8080]
	print("Checking All ports")
	for port in common_ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))
		else:
			print("port {} is filtered or closed".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program. ")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resloved. ")
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()
		

