import hashlib
from platform import system
import os, sys

if system() == 'Linux':
    os.system('clear')
elif system() == 'Windows':
    os.system('cls')
print('''
[*] InterCuba.Net
\033[1;31;40m Krintoxi  \n
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣶⣶⣶⣾⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⠿⠿⠛⠛⠛⠋⠉⠉⠁⠀⠀⠈⠛⠿⢿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⡄⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇ 75 ⣿⡇⠀⠀⠈⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀x⢀⣿⠇⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣶⠿⠋⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠃⠀⠀⠀⠀⢀⣴⣿⣥⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢀⣴⣿⣋⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣽⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣶⣤⣶⠿⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀o⠀⠀⠀⠀⢀⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀o⠀⠀⠀⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠀#SOSCUBA⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣾⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⠿⣿⡏⠉⠀⠈⠛⢿⣶⣤⣄⣀⣀⣤⣴⣶⠟⠋⠀⠉⠙⢻⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⠿⠟⠛⣿⡆⠀⠘⣿⡄⠀⠀⠀⣠⣾⠟⢉⣿⣯⠙⢿⣦⣄⠀⠀⠀⢀⣾⠏⠀⢨⣿⠛⠻⢿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣴⣾⣿⣿⠿⠟⠋⠉⠀⠀⠀⣀⣼⣿⠄⠀⠙⣿⡀⢀⣼⡟⠁⠀⣸⡟⢻⣆⠀⠈⢿⣇⠀⢀⣾⠏⠀⢠⣾⣇⡀⠀⠀⠀⠉⠙⠻⠿⣿⣿⣶⣦⣄⡀⠀⠀⠀
⠀⠀⢠⣿⣿⠟⠋⢻⣧⠀⣀⣠⣴⡾⠟⠛⠉⠀⠀⠀⠀⠹⣿⣸⡿⣷⡄⣰⡿⠀⠘⣿⡆⢀⣾⢿⣄⣾⠏⠀⠀⠀⠈⠛⠻⠿⣦⣤⣀⡀⠀⠀⣼⡟⠛⠻⣿⣷⠀⠀⠀
⠀⠀⣼⣿⡇⠀⠀⠈⢿⡷⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠃⠘⢿⣿⠃⠀⠀⠘⣿⡿⠃⠘⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⢶⣶⡿⠁⠀⠀⢻⣿⣧⠀⠀
⠀⢀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⡀⢀⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⣿⣿⠀⠀
⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡿⠋⠀⠀⢀⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀
⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢸⡟⠛k⢻r⠛i⠛n⠛t⣿ox⢻i⣯⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀
⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀xxxxx⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠸⠿⠾⠷⠾⠿⠾⠿⠷⠿⠿⠿⠿⠾⠟⠿⠿⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀
⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀xxxxxxxxxxx⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀
⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
''')

hash_lengths = {
    7: "[*] created by >> Leo Edge Intercuba.net",
    16: "[*] hash >> MySQL323, LM Hash (16-character Unicode password), FCS-16",
    19: "[*] hash >> Cisco-ASA MD5",
    20: "[*] hash >> FCS-64, FCS-32",
    21: "[*] hash >> SAP CODVN B (BCODE)",
    24: "[*] hash >> Tiger",
    27: "[*] hash >> Oracle H: Type (Oracle 7+), DES(Oracle)",
    32: "[*] hash >> MD5, MD4, MD2, RAdmin v2.x, Cisco-IOS type 5 (MD5-based)",
    34: "[*] hash >> bcrypt (Blowfish-based)",
    40: "[*] hash >> SHA1, ecdsa-with-SHA1, DSA-SHA, ripemd160, HAVAL-160, Redmine Project Management Web App",
    41: "[*] hash >> MySQL5",
    43: "[*] hash >> Cisco-IOS type 4 (SHA256-based), Cisco-IOS type 7",
    47: "[*] hash >> FortiGate (FortiOS)",
    48: "[*] hash >> HAVAL-192, CRC16, CRC24",
    55: "[*] hash >> Drupal7",
    56: "[*] hash >> SHA224, HAVAL-224, CRC32",
    57: "[*] hash >> Samsung Android Password/PIN",
    60: "[*] hash >> BCRYPT",
    64: "[*] hash >> SHA256, RIPEMD-256, HAVAL-256, SHA-256 (HMAC), Cisco IOS SHA-256",
    68: "[*] hash >> HAVAL-256",
    80: "[*] hash >> RIPEMD-320",
    96: "[*] hash >> SHA384 HASH, sha384, SHA-384 (HMAC)",
    1024: "[*] hash >> SHA-512 (HMAC) truncated to 1024 bits",
    110: "[*] hash >> Juniper IVE",
    128: "[*] hash >> SHA512, sha512, Whirlpool, RIPEMD-320, CRC64, SHA-512 (HMAC)",
    136: "[*] hash >> BLAKE2b-512",
    144: "[*] hash >> SHA-512 (HMAC) truncated to 144 bits",
    152: "[*] hash >> BLAKE2s-256",
    160: "[*] hash >> SHA-1 (Cisco PIX), RIPEMD-160, SHA-1 (HMAC)",
    168: "[*] hash >> BLAKE2s-224",
    174: "[*] hash >> NetNTLMv2",
    180: "[*] hash >> SHA-1 (HMAC) truncated to 180 bits",
    192: "[*] hash >> Tiger192,4",
    224: "[*] hash >> SHA-3 (224 bits), SHA-224 (HMAC), SHA-3 (224 bits), SHA-224 (HMAC)",
    256: "[*] hash >> SHA-3 (256 bits), SHA-256 (HMAC), Tiger192,4 (HMAC)",
    280: "[*] hash >> SHA-224 (HMAC) truncated to 280 bits",
    288: "[*] hash >> Whirlpool",
    320: "[*] hash >> SHA-384 (HMAC) truncated to 320 bits",
    321: "[*] hash >> Windows Phone 8+ PIN/password",
    384: "[*] hash >> SHA-3 (384 bits), SHA-384 (HMAC)",
    512: "[*] hash >> SHA-3 (512 bits), SHA-512 (HMAC), Whirlpool (HMAC)",
    1024: "[*] hash >> SHA-512 (HMAC) truncated to 1024 bits",
    150: "[*] hash >> Example hash type",
    200: "[*] hash >> Another hash type",
}

while True:
    the_hash = input('[*] Enter your hash (or "q" to quit): ')
    if the_hash.lower() == 'q':
        print('Goodbye!')
        break

    hash_length = len(the_hash)

    if hash_length in hash_lengths:
        print('[+] hash >>> ' + hash_lengths[hash_length])
    else:
        print('[#] Error >> 404 not found')
    print()
