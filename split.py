#!/usr/bin/python

from __future__ import print_function

ip_addr = raw_input("Enter an ip addr: ")

print(ip_addr)

ip_addr=ip_addr.split(".")

print ("{:<12} {:<12} {:<12} {:<12}".format(*ip_addr))
