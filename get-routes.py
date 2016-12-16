#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable

routelist = open('bgproutes_current','w')
dev = Device(user="username",password="mypassword",host='192.168.0.1')
dev.open()
routes = RouteTable(dev)
routes.get(protocol="bgp",community="65001:666")
for route in routes.keys():
  print "Offending route found-->"+route
  routelist.write(route+'\n')
dev.close()
