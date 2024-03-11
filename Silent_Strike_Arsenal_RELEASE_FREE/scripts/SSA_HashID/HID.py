import os
from platform import system

# Function to clear the console screen
def clear_screen():
    if system() == 'Linux':
        os.system('clear')
    elif system() == 'Windows':
        os.system('cls')

# Hash lengths and their corresponding types
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
    "1Password(Agile Keychain)": 64,
    "1Password(Cloud Keychain)": 64,
    "Adler-32": 8,
    "AIX(smd5)": 13,
    "AIX(ssha1)": 46,
    "AIX(ssha256)": 46,
    "AIX(ssha512)": 86,
    "Android FDE ≤ 4.3": 32,
    "Android PIN": 4,
    "Apache MD5": 32,
    "bcrypt(SHA-256)": 60,
    "BigCrypt": 23,
    "Blowfish(OpenBSD)": 60,
    "BSDi Crypt": 128,
    "Cisco Type 4": 43,
    "Cisco Type 8": 43,
    "Cisco Type 9": 43,
    "Cisco VPN Client(PCF-File)": 72,
    "Cisco-ASA(MD5)": 43,
    "Cisco-IOS(MD5)": 43,
    "Cisco-IOS(SHA-256)": 64,
    "Cisco-PIX(MD5)": 43,
    "Citrix Netscaler": 128,
    "Clavister Secure Gateway": 64,
    "CRAM-MD5": 32,
    "CRC-16": 4,
    "CRC-16-CCITT": 4,
    "CRC-24": 6,
    "CRC-32": 8,
    "CRC-32B": 8,
    "CRC-64": 16,
    "CRC-96(ZIP)": 24,
    "Crypt16": 128,
    "CryptoCurrency(Adress)": None,  # Replace with appropriate length
    "CryptoCurrency(PrivateKey)": None,  # Replace with appropriate length
    "Dahua": 32,
    "DES(Oracle)": 16,
    "DES(Unix)": 13,
    "Django(bcrypt-SHA256)": 60,
    "Django(bcrypt)": 60,
    "Django(DES Crypt Wrapper)": 13,
    "Django(MD5)": 32,
    "Django(PBKDF2-HMAC-SHA1)": 56,
    "Django(PBKDF2-HMAC-SHA256)": 64,
    "Django(SHA-1)": 40,
    "Django(SHA-256)": 64,
    "Django(SHA-384)": 96,
    "DNSSEC(NSEC3)": None,  # Replace with appropriate length
    "Domain Cached Credentials": 48,
    "Domain Cached Credentials v2": 64,
    "Double MD5": 32,
    "Double SHA1": 40,
    "Drupal > v7.x": 55,
    "Eggdrop IRC Bot": 32,
    "ELF-32": 8,
    "EPi": 32,
    "EPiServer 6.x < v4": 64,
    "EPiServer 6.x ≥ v4": 64,
    "Fairly Secure Hashed Password": None,  # Replace with appropriate length
    "FCS-16": 4,
    "FCS-32": 8,
    "Fletcher-32": 8,
    "FNV-132": 32,
    "FNV-164": 64,
    "Fortigate(FortiOS)": 47,
    "FreeBSD MD5": 32,
    "GHash-32-3": 8,
    "GHash-32-5": 8,
    "GOST CryptoPro S-Box": 64,
    "GOST R 34.11-94": 64,
    "GRUB 2": 32,
    "Half MD5": 16,
    "HAS-160": 40,
    "Haval-128": 32,
    "Haval-160": 40,
    "Haval-192": 48,
    "Haval-224": 56,
    "Haval-256": 64,
    "hMailServer": None,  # Replace with appropriate length
    "IKE-PSK MD5": 16,
    "IKE-PSK SHA1": 20,
    "IP.Board ≥ v2": 32,
    "IPMI2 RAKP HMAC-SHA1": 20,
    "iSCSI CHAP Authentication": None,  # Replace with appropriate length
    "Joaat": 8,
    "Joomla < v2.5.18": 32,
    "Joomla ≥ v2.5.18": 32,
    "Juniper Netscreen/SSG(ScreenOS)": 32,
    "Kerberos 5 AS-REQ Pre-Auth": None,  # Replace with appropriate length
    "Lastpass": None,  # Replace with appropriate length
    "LDAP(SSHA-512)": None,  # Replace with appropriate length
    "Lineage II C4": 32,
    "LinkedIn": 32,
    "LM": 32,
    "Lotus Notes/Domino 5": 16,
    "Lotus Notes/Domino 6": 32,
    "Lotus Notes/Domino 8": 32,
    "MangosWeb Enhanced CMS": 32,
    "MD2": 32,
    "MD4": 32,
    "MD5": 32,
    "MD5 Crypt": 128,
    "MD5(APR)": 32,
    "MD5(Chap)": 32,
    "MediaWiki": 32,
    "Microsoft MSTSC(RDP-File)": 32,
    "Microsoft Office ≤ 2003 (MD5+RC4)": 32,
    "Microsoft Office ≤ 2003 (SHA1+RC4)": 40,
    "Microsoft Office 2007": 64,
    "Microsoft Office 2010": 64,
    "Microsoft Office 2013": 64,
    "Microsoft Outlook PST": None,  # Replace with appropriate length
    "Minecraft(AuthMe Reloaded)": 32,
    "Minecraft(xAuth)": 32,
    "MSSQL(2000)": 32,
    "MSSQL(2005)": 32,
    "MSSQL(2008)": 32,
    "MSSQL(2012)": 32,
    "MSSQL(2014)": 32,
    "MyBB ≥ v1.2+": 32,
    "MySQL Challenge-Response Auth (SHA1)": 40,
    "MySQL323": 32,
    "MySQL4.1": 41,
    "MySQL5.x": 64,
    "NetNTLMv1-VANILLA / NetNTLMv1+ESS": 32,
    "NetNTLMv2": 64,
    "Netscape LDAP SHA": 32,
    "Netscape LDAP SSHA": 48,
    "NTHash(FreeBSD Variant)": 32,
    "NTLM": 32,
    "Oracle 11g/12c": None,  # Replace with appropriate length
    "Oracle 7-10g": None,  # Replace with appropriate length
    "osCommerce": 32,
    "OSX v10.4-10.6": 32,
    "OSX v10.7": 32,
    "OSX v10.8-10.9": 32,
    "Palshop CMS": 32,
    "PBKDF2-HMAC-SHA256(PHP)": 64,
    "PBKDF2-SHA1(Generic)": None,  # Replace with appropriate length
    "PBKDF2-SHA256(Generic)": None,  # Replace with appropriate length
    "PBKDF2-SHA512(Generic)": None,  # Replace with appropriate length
    "PBKDF2(Atlassian)": None,  # Replace with appropriate length
    "PBKDF2(Cryptacular)": None,  # Replace with appropriate length
    "PBKDF2(Dwayne Litzenberger)": None,  # Replace with appropriate length
    "PDF 1.4 - 1.6 (Acrobat 5 - 8)": None,  # Replace with appropriate length
    "PeopleSoft": 32,
    "PHPass' Portable Hash": 34,
    "phpBB 3.x": 40,
    "PHPS": 34,
    "PostgreSQL Challenge-Response Auth (MD5)": 32,
    "PostgreSQL MD5": 32,
    "RACF": None,  # Replace with appropriate length
    "RAdmin v2.x": None,  # Replace with appropriate length
    "Redmine Project Management Web App": 40,
    "RIPEMD-128": 32,
    "RIPEMD-160": 40,
    "RIPEMD-256": 64,
    "RIPEMD-320": 80,
    "Salsa10": 64,
    "Salsa20": 64,
    "SAM(LM_Hash:NT_Hash)": 32,
    "SAP CODVN B (BCODE)": None,  # Replace with appropriate length
    "SAP CODVN F/G (PASSCODE)": None,  # Replace with appropriate length
    "SAP CODVN H (PWDSALTEDHASH) iSSHA-1": None,  # Replace with appropriate length
    "SCRAM Hash": None,  # Replace with appropriate length
    "scrypt": None,  # Replace with appropriate length
    "SHA-1": 40,
    "SHA-1 Crypt": 34,
    "SHA-1(Base64)": 28,
    "SHA-1(Oracle)": 48,
    "SHA-224": 56,
    "SHA-256": 64,
    "SHA-256 Crypt": 64,
    "SHA-384": 96,
    "SHA-512": 128,
    "SHA-512 Crypt": 106,
    "SHA3-224": 56,
    "SHA3-256": 64,
    "SHA3-384": 96,
    "SHA3-512": 128,
    "Siemens-S7": 32,
    "SipHash": 16,
    "Skein-1024": 128,
    "Skein-1024(384)": 48,
    "Skein-1024(512)": 64,
    "Skein-256": 64,
    "Skein-512": 128,
    "Skein-512(256)": 32,
    "Skein-512(384)": 48,
    "Snefru-128": 32,
    "Snefru-256": 64,
    "SonicWALL (SHA1/DES)": 44,
    "SonicWALL (SHA256/AES)": 64,
    "SSHA-1(Base64)": None,  # Replace with appropriate length
    "SSHA-256(Base64)": None,  # Replace with appropriate length
    "SSHA-384(Base64)": None,  # Replace with appropriate length
    "SSHA-512(Base64)": None,  # Replace with appropriate length
    "Thrip": 32,
    "TIGER-128": 32,
    "TIGER-160": 40,
    "TIGER-192": 48,
    "Truncate-4": 4,
    "Truncate-8": 8,
    "UnicodePwd": None,  # Replace with appropriate length
    "Ventrilo": None,  # Replace with appropriate length
    "vBulletin < v3.8.5": 32,
    "vBulletin ≥ v3.8.5": 40,
    "VNC": None,  # Replace with appropriate length
    "VMware Authentication Daemon": None,  # Replace with appropriate length
    "WBB3": 32,
    "Woltlab Burning Board 3.x": 40,
    "Wordpress ≥ v2.6.0": 34,
    "Wordpress ≤ v2.5.1": 34,
    "X11": 11,
    "XMF1": None,  # Replace with appropriate length
    "xmpp-scram": None,  # Replace with appropriate length
    "XOR-32": 8,
    "ZIP": None,  # Replace with appropriate length
}

# Function to display supported algorithms
def display_algorithms():
    for length, description in hash_lengths.items():
        print(f"{length}: {description}")

# Clear the screen on start
clear_screen()

print('''
[*] InterCuba.Net
\033[1;31;40m Hash Identifier  \n

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠛⠛⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠿⠟⣿⠉⠛⠻⠶⠶⠶⠶⠟⠛⠉⣿⠻⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠉⠁⠀⠀⠀⠀⠙⠻⠶⠦⠤⠤⠤⠤⠴⠶⠟⠋⠀⠀⠀⠀⠈⠉⣿⣿⣿
⣿⣿⣿⣿⣷⣶⣶⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⣤⣶⣶⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠹⣿⣿⣿⡟⢻⣿⣿⣿⠏⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠉⠁⠀⢹⣇⠀⠉⠉⠁⠀⠀⠈⠉⠉⠀⣸⡏⠀⠈⠉⠻⢿⣿⣿⣿
⣿⣿⣅⣀⠀⠀⠀⠀⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀⠀⣀⣨⣿⣿
⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠈⢻⣷⣦⣤⣤⣴⣾⡟⠁⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠛⠓⠀⠀⠀⠸⣯⠀⠀⠀⠀⣽⠇⠀⠀⠀⠚⠛⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⣄⣀⣀⡀⠀⠀⠀⠘⣷⣀⣀⣾⠃⠀⠀⠀⢀⣀⣀⣠⣼⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⣿⠉⠙⣿⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⢛⡙⢻⠛⣉⢻⣉⢈⣹⣿⣿⠟⣉⢻⡏⢛⠙⣉⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⠻⠃⣾⠸⠟⣸⣿⠈⣿⣿⣿⡀⠴⠞⡇⣾⡄⣿⠘..⣿⣿⣿⣿⣿⣿
⣿⣿⣟⠛⣃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

.---.    .---.        ,.     ,-_/,.     ,.   .---. ,-_/,.   ,-_/   .         .                 
\___     \___        / |     ' |_|/    / |   \___  ' |_|/   '  | ,-| ,-. ,-. |- . ," . ,-. ,-. 
    \        \      /~~|-.    /| |    /~~|-.     \  /| |    .^ | | | |-' | | |  | |- | |-' |   
`---' :; `---' :; ,'   `-'    `' `' ,'   `-' `---'  `' `'   `--' `-^ `-' ' ' `' ' |  ' `-' '   
                                                                                  '            
                                                                                               

''')

while True:
    the_hash = input('[*] Enter your hash (or "q" to quit, "algo" for a list of supported algorithms): ')

    if the_hash.lower() == 'q':
        print('Goodbye!')
        break

    if the_hash.lower() == 'algo':
        display_algorithms()
    else:
        hash_length = len(the_hash)
        if hash_length in hash_lengths:
            print('[+] hash >>> ' + hash_lengths[hash_length])
        else:
            print('[#] Error >> Hash Type NOT found')
    
    print()

