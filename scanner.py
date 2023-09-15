#!/bin/python3

#this is a python scanner for ip address

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 scanner.py <ip>')
#not best logic, always think how could someone break this

#Add a pretty banner
print('-'*50)
print('Scanning target: ',target)
print('Time started: ',str(datetime.now()))
print('-'*50)

try:
    for port in range(50,85)