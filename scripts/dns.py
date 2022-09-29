#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
cmd1 = os.system ("sudo apt install dnsutils")
print "**************************************************************"
print "Enter the domain below to gather basic DNS information."
print "Example: website.com"
print"***************************************************************"
target = raw_input("Input Target: ")  
print""
print "*****************************************"
cmd1 = os.system ("nslookup -type=ns -query=all "+target)

print"-----------"
print "Finished!"
print "----------"
