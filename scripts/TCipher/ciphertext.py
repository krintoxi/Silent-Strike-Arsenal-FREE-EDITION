#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys, traceback
import argparse
import time
import subprocess
if __name__ == "__main__":
    ascii_art = """
    ⠀⢀⣤⣤⣤⣤⣤⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠻⢿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣼⣿⡏⠀⠀⠀⢀⣀⣀⣀⣀⠀⢸⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
    ⠀⣿⣿⠁⠀⠀⢰⣿⣿⣿⣿⣿⡆⠘⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
    ⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣀⣈⣿⣿⣿⣿⣿⣦⡀⠀⠀
    ⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
    ⠀⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
    ⠀⢿⣿⡆⠀⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⡇⠀
    ⠀⠸⣿⣧⡀⠀  ALPHA#66⠈⠙⢿⣿⡇⠀
    ⠀⠀⠛⢿⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣿⡇⠀⠀
    ⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠿⠛⠉
    """

    print(ascii_art)

lines = ["C.I_TOOLKIT: What this module can do: ",
         "1. Encryption: The user can input a message to encrypt. The script then displays the generated AES key and the encrypted message.",
         "2. Decryption: The user can input the AES key and the ciphertext for decryption. The script displays the decrypted result if successful."]
print('-------------------------------------------------------------')
         

from time import sleep
import sys

for line in lines:          # for each line of text (or each message)
    for c in line:          # for each character in each line
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.01)          # wait a little to make the effect look good.
    print('')               # line break (optional, could also be part of the message)
print('-------------------------------------------------------------')

from cryptography.fernet import Fernet
import random
import string

def encrypt_aes(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_aes(ciphertext, key):
    try:
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(ciphertext).decode()
        return decrypted_message
    except:
        return "Decryption failed"

def main():
    print("************************************************************")
    print("*                   C.I Toolkit - AES Cipher              *")
    print("************************************************************")

    key = Fernet.generate_key()
    print("Generated AES Key:")
    print(">> " + key.decode())
    print("=" * 60)

    mode = input("Do you want to encrypt or decrypt? ").lower()

    if mode == 'encrypt':
        text = input("Enter the message to encrypt: ")
        print("=" * 60)
        print("Encrypting...")
        encrypted_text = encrypt_aes(text, key)
        print("Encrypted Message:")
        print(">> " + encrypted_text.decode())
        print("=" * 60)
    elif mode == 'decrypt':
        key_input = input("Enter the AES key for decryption: ")
        key = key_input.encode()
        text = input("Enter the ciphertext to decrypt: ")
        print("=" * 60)
        print("Decrypting...")
        decrypted_text = decrypt_aes(text.encode(), key)
        print("Decrypted Result:")
        print(">> " + decrypted_text)
        print("=" * 60)
    else:
        print("Invalid mode selected. Initiating countermeasures...")
        print("=" * 60)
        print("Access denied. Terminating connection...")

if __name__ == "__main__":
    main()
