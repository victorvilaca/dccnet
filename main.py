#!/usr/bin/python

import sys
import socket

for arg in sys.argv[1:]:
  #print arg
  if arg == '-c':
    print 'Cliente'
    for aux in sys.argv[2:3]:
      ip,port=aux.split(":")
      print ip
      print port
    for auxInput in sys.argv[3:4]:
      print auxInput
    for auxOutput in sys.argv[4:]:
      print auxOutput
    HOST = ip
    PORT = port

  if arg == '-s':
    print 'Servidor'
    for port in sys.argv[2:3]:
      print port
    for auxInput in sys.argv[3:4]:
      print auxInput
    for auxOutput in sys.argv[4:]:
      print auxOutput
    HOST = ''
    PORT = port
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)