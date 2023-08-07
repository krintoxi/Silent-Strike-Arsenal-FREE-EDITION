import hashlib
import bcrypt
import scrypt
import argon2
import time
import os
import multiprocessing
import importlib.util
import sys
import subprocess
import re
import wordlist  # Import the wordlist from wordlist.py

filename = 'schedule'  # File to store current cracking progress
resultname = 'result'  # File to store the final cracking result
order = 0
print("----------------------------------------")
algorithm = input("What hashing algorithm do you want to crack? (md5, sha1, sha256, sha384, sha512, bcrypt, scrypt, argon2): ")
algorithm = algorithm.lower()
print("----------------------------------------")

# Character set for plaintext generation
default_charset = '0123456789abcdefghijklmnopqrstuvwxyz'  # All alphanumeric characters (lowercase)

# Wordlist of common passwords
wordlist = wordlist.wordlist

def generate_text(order, charset):
    # Generate plaintext from the given order and charset
    if order == 0:
        return charset[0]
    text = ''
    while order != 0:
        text = charset[order % len(charset)] + text
        order //= len(charset)
    return text

def is_valid_hash(input_str, algorithm):
    # Check if the input is a valid hash for the selected algorithm
    if algorithm in ['md5', 'sha1', 'sha256', 'sha384', 'sha512']:
        return bool(re.match(r"^[a-fA-F0-9]{64}$", input_str))
    elif algorithm == 'bcrypt':
        return True
    elif algorithm == 'scrypt':
        return bool(re.match(r"^[a-fA-F0-9]{128}$", input_str))
    elif algorithm == 'argon2':
        return True
    else:
        return False

def check_wordlist(cipher, algorithm):
    # Check if the password is in the wordlist
    for password in wordlist:
        hashed_password = hash_password(password, algorithm)
        if hashed_password == cipher:
            return password
    return None

def hash_password(password, algorithm):
    if algorithm == 'md5':
        return hashlib.md5(password.encode('utf-8')).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode('utf-8')).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode('utf-8')).hexdigest()
    elif algorithm == 'sha384':
        return hashlib.sha384(password.encode('utf-8')).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(password.encode('utf-8')).hexdigest()
    elif algorithm == 'bcrypt':
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    elif algorithm == 'scrypt':
        return scrypt.hash(password, salt=scrypt.getsalt()).decode('utf-8')
    elif algorithm == 'argon2':
        return argon2.PasswordHasher().hash(password.encode('utf-8')).decode('utf-8')
    else:
        raise ValueError("Invalid hashing algorithm specified.")

def install_tqdm():
    try:
        importlib.util.find_spec('tqdm')
    except ImportError:
        print("Installing 'tqdm' library...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'tqdm'])

def crack_hash(chunk, charset, total_attempts):
    global order
    found = False
    chunk_order = order  # Start cracking from the current order position
    while not found:
        text = generate_text(chunk_order, charset)
        chunk_order += 1
        total_attempts[0] += 1

        if hashlib.new(algorithm, text.encode('utf-8')).hexdigest() == cipher:
            found = True
            return text

def main():
    global order
    install_tqdm()

    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            order = int(fp.readline().strip())

    try:
        if not is_valid_hash(cipher, algorithm):
            raise ValueError("Invalid hash or unsupported hashing algorithm. Please provide a valid hash.")

        print("A character set is a collection of characters that the script will use to generate")
        print("plaintexts for the brute force attack. It can be any combination of characters")
        print("that you think the password may contain.")
        print("For example, if you think the password contains the word 'hello' along with")
        print("digits and lowercase letters, you can enter '0123456789abcdefghijklmnopqrstuvwxyzhello'.")
        print("If you are not sure, you can press Enter to use the default character set, which is:")
        print("'0123456789abcdefghijklmnopqrstuvwxyz' (all lowercase alphanumeric characters).")

        charset = input("Enter the character set (or press Enter to use default): ")
        charset = charset or default_charset

        use_wordlist = input("Do you want to use the wordlist? (y/n): ").lower() == 'y'

        if use_wordlist:
            print("Using wordlist for cracking...")
            password = check_wordlist(cipher, algorithm)
            if password:
                print(f"\nPlaintext (found in wordlist): {password}")
                return

        print(f"\nStarting from position {order} in the character set.")
        print("Cracking in progress...")
        print("You can interrupt the process any time by pressing 'Ctrl + C'.\n")

        max_attempts_per_chunk = 100000  # Limit attempts per chunk before pausing

        total_attempts = [0]
        chunks = [charset[i:i + max_attempts_per_chunk] for i in range(0, len(charset), max_attempts_per_chunk)]
        with multiprocessing.Pool() as pool:
            while True:
                futures = [pool.apply_async(crack_hash, args=(chunk, charset, total_attempts)) for chunk in chunks]
                pool.close()
                pool.join()
                for future in futures:
                    plaintext = future.get()
                    if plaintext:
                        print(f"\nPlaintext: {plaintext}")
                        print("Cracking successful!")
                        with open(resultname, 'w') as fp:
                            fp.write(plaintext)
                        return

                print(f"Current progress: {order}/{len(charset)}")
                print("Performance Metrics:")
                print(f"Average Speed: {total_attempts[0] / (time.time() - start_time):.2f} attempts per second")
                print(f"Total Attempts: {total_attempts[0]}")

                order += max_attempts_per_chunk  # Move to the next chunk
                if order >= len(charset):
                    break

    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print("\nCracking interrupted by the user.")
    finally:  # Save the current progress when the program terminates
        with open(filename, 'w') as fp:
            fp.write(str(order))

if __name__ == '__main__':
    start_time = time.time()
    main()
