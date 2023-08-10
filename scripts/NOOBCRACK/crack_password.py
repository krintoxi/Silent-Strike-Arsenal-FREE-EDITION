import hashlib
import itertools
import time
import sys
import os
import requests
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def download_online_wordlist(url):
    response = requests.get(url)
    if response.status_code == 200:
        wordlist = response.text.splitlines()
        return wordlist
    else:
        print("\033[1;31mFailed to download the online leaked password wordlist. Continuing with the local wordlist...\033[0m")
        return None


def crack_hash(cipher, algorithm, charset, password_length, start=0, end=None):
    if end is None:
        end = len(charset) ** password_length + start

    for i, password in enumerate(itertools.product(charset, repeat=password_length), start=start):
        password = "".join(password)
        hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()
        if hashed_password == cipher:
            return password

    return None

def print_wordlist_progress(progress, total_attempts_wordlist, password, is_local=True):
    bar_length = 30
    progress_percent = min(100, int(progress / total_attempts_wordlist * 100))
    progress_bar = "#" * int(progress_percent / 100 * bar_length)

    source = "LOCAL" if is_local else "DOWNLOADED"
    sys.stdout.write(
        f"\r{source} Password Wordlist Progress: [{progress_bar.ljust(bar_length)}] {progress_percent}% | Current password being Checked: {password}")
    sys.stdout.flush()

def crack_with_wordlist(cipher, algorithm, wordlist, is_local=True):
    total_attempts_wordlist = len(wordlist)

    source = "LOCAL" if is_local else "DOWNLOADED"
    print(f"\nAttempting To Crack Source of Passwords: {source} | Total attempts: {total_attempts_wordlist}\n")
    print("****************************************************************************************************")

    for progress, password in enumerate(wordlist, start=1):
        hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()
        if hashed_password == cipher:
            print("\nPassword found in the password wordlist!!! PASSWORD FOUND:", password)
            print("**********************************************************************")
            return password  # Stop further processing if password found

        print_wordlist_progress(progress, total_attempts_wordlist, password, is_local=is_local)
    print(f"\nNO Password or Message found in the {source} password wordlist")
    print("****************************************************************************************************")
def crack_with_brute_force(cipher, algorithm):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_password_length = 10
    brute_force_start = 0
    max_attempts = sum(len(charset) ** i for i in range(1, max_password_length + 1))

    print("The Time this process takes is based on the hardware you are running and length of the key to crack.")
    print(f"Starting brute-force... Total attempts: {max_attempts}\n")
    print("****************************************************************************************************")
    for password_length in range(1, max_password_length + 1):
        for attempt, password in enumerate(itertools.product(charset, repeat=password_length), start=1):
            password = "".join(password)
            hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()
            brute_force_start += 1
            if hashed_password == cipher:
                print("\nPassword found by brute force:", password)
                return password  # Stop further processing if password found

            if brute_force_start % 100000 == 0:
                print_brute_force_progress(attempt, max_attempts, password_length, password)


def print_brute_force_progress(attempt, total_attempts, password_length, password):
    bar_length = 30
    progress_percent = min(100, int(attempt / total_attempts * 100))
    progress_bar = "#" * int(progress_percent / 100 * bar_length)
    sys.stdout.write(
        f"\rBrute Force Progress: [{progress_bar.ljust(bar_length)}] {progress_percent}% | Current password length: {password_length} | Current password: {password}")
    sys.stdout.flush()

def print_banner():
    banner = """
><<<     ><<                    ><<                ><<                           ><<     
>< ><<   ><<                    ><<             ><<   ><<                        ><<     
><< ><<  ><<   ><<       ><<    ><<            ><<       >< ><<<   ><<       ><<<><<  ><<
><<  ><< ><< ><<  ><<  ><<  ><< ><< ><<        ><<        ><<    ><<  ><<  ><<   ><< ><< 
><<   >< ><<><<    ><<><<    ><<><<   ><<      ><<        ><<   ><<   ><< ><<    ><><<   
><<    >< << ><<  ><<  ><<  ><< ><<   ><<       ><<   ><< ><<   ><<   ><<  ><<   ><< ><< 
><<      ><<   ><<       ><<    ><< ><<           ><<<<  ><<<     ><< ><<<   ><<<><<  ><<
                                         ><<<<<                                          
***********************************************************************************************
"""
    print("\033[1;32m" + banner + "\033[0m")


def main():
    algorithms = ["md5", "sha1", "sha256", "sha384", "sha512"]
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_password_length = 10

    try:
        clear_screen()
        print_banner()
        print("**************************************************************")
        print("\033[1;34mWhat hashing algorithm do you want to crack?:\033[0m")
        print("**************************************************************")
        print("(md5, sha1, sha256, sha384, sha512):")

        while True:
            algorithm = input("Please enter the algorithm name: ").lower()
            if algorithm in algorithms:
                break
            else:
                print("\033[1;31mInvalid algorithm. Please choose from md5, sha1, sha256, sha384, or sha512.\033[0m")

        print("\033[1;34mEnter the hash to crack:\033[0m")
        cipher = input().strip()

        if not cipher:
            print("\033[1;31mInvalid hash. Please enter a valid hash.\033[0m")
            return

        with open("passwords.txt", "r") as f:
            local_wordlist = f.read().splitlines()

        found_password = crack_with_wordlist(cipher, algorithm, local_wordlist, is_local=True)

        if not found_password:
            online_wordlist_url = "https://raw.githubusercontent.com/josuamarcelc/common-password-list/main/rockyou.txt/rockyou_1.txt"
            online_wordlist = download_online_wordlist(online_wordlist_url)
            if online_wordlist:
                found_password = crack_with_wordlist(cipher, algorithm, online_wordlist, is_local=False)

        if not found_password:
            crack_with_brute_force(cipher, algorithm)

    except KeyboardInterrupt:
        print("\n\033[1;31mCracking process interrupted.\033[0m")


if __name__ == "__main__":
    main()
