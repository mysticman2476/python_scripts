#/usr/bin/python

from __future__ import print_function

name_var1 = "john"
name_var2 = "robert"
name_var3 = "doe"

my_list = (name_var1, name_var2, name_var3)

print ("{:>30}{:>30}{:>30}".format(*my_list))

name4=raw_input("Enter new name: ")

print(name4)
