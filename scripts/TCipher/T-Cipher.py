if __name__ == "__main__":
    ascii_art = """
                             ⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
                             ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
                             ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
                             ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
                             ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
                             ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
                             ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
                             ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
                             ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
                             ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄

'########:::::::::::'######::'####:'########::'##::::'##:'########:'########::
... ##..:::::::::::'##... ##:. ##:: ##.... ##: ##:::: ##: ##.....:: ##.... ##:
::: ##::::::::::::: ##:::..::: ##:: ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:
::: ##::::'#######: ##:::::::: ##:: ########:: #########: ######::: ########::
::: ##::::........: ##:::::::: ##:: ##.....::: ##.... ##: ##...:::: ##.. ##:::
::: ##::::::::::::: ##::: ##:: ##:: ##:::::::: ##:::: ##: ##::::::: ##::. ##::
::: ##:::::::::::::. ######::'####: ##:::::::: ##:::: ##: ########: ##:::. ##:
:::..:::::::::::::::......:::....::..:::::::::..:::::..::........::..:::::..::
                            C.I Toolkit Module
    """
print(ascii_art)
print("T-Cipher: What this module can do:")
print("*************************************")
lines = [
         "1. Encryption: The user can input a message to encrypt. The script then displays the generated AES key and the encrypted message.",
         "2. Decryption: The user can input the AES key and the ciphertext for decryption. The script displays the decrypted result if successful."]

from time import sleep
import sys

for line in lines:          # for each line of text (or each message)
    for c in line:          # for each character in each line
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.01)          # wait a little to make the effect look good.
    print('')               # line break (optional, could also be part of the message)

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
        return "Decryption FAILED!"

def main():
    print("*******************************************************************************")
    print("*                      C.I Toolkit - T-Cipher Module                          *")
    print("*******************************************************************************")

    key = Fernet.generate_key()


    mode = input("Do you want to encrypt or decrypt?: ").lower()

    if mode == 'encrypt':
        print("*" * 80)
        text = input("Enter the message to encrypt: ")
        print("*" * 80)
        print("Encrypting...")
        encrypted_text = encrypt_aes(text, key)
        print("*" * 80)
        print("Encrypted Message:")
        print(">>: " + encrypted_text.decode())
        print("*" * 80)
        print("Generated AES Key:")
        print(">>: " + key.decode())
        print("*" * 80)
        print("*STORE THIS KEY SECURELY: Without it decryption of the Encrypted text is not possible")
        print("*SHARE THIS KEY: ONLY WITH A TRUSTED SOURCE MEANT TO ALSO AT SOME POINT OPEN THIS MESSAGE USING THE KEY")
        print("*MAKE SURE: That transmission of the ENCRYPTED TEXT and KEY is done Securely")
        print("********************************************************************************")
    elif mode == 'decrypt':
        key_input = input("Enter the AES key for decryption: ")
        key = key_input.encode()
        text = input("Enter the ciphertext to decrypt: ")
        print("*" * 80)
        print("Decrypting...")
        decrypted_text = decrypt_aes(text.encode(), key)
        print("Decrypted Result:")
        print(">> " + decrypted_text)
        print("*" * 80)
    else:
        print("Invalid mode selected. Initiating countermeasures...")
        print("*" * 80)
        print("Access denied. Terminating connection!")

if __name__ == "__main__":
    main()
