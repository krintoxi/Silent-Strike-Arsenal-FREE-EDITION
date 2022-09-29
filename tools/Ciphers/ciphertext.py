#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
import argparse
import time
import subprocess

lines = ["C.I_TOOLKIT",
         "(Text Cipher)"]
print('-------------------------------------------------------------')
         

from time import sleep
import sys

for line in lines:          # for each line of text (or each message)
    for c in line:          # for each character in each line
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.1)          # wait a little to make the effect look good.
    print('')               # line break (optional, could also be part of the message)
print('-------------------------------------------------------------')

choice = input('Would you like to Cipher(c) or De-Cipher(d) text: ')
if choice == "c":
	print("Ok..")
	cmd1 = os.system("python scripts/Ciphers/KeyCipher.py")
if choice == "d":
	cmd1 = os.system("python scripts/Ciphers/ReverseKeyCipher.py")
