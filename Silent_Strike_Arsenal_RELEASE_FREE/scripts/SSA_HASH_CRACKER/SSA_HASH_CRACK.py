import hashlib
import itertools
import os
import subprocess
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_online_wordlist(url):
    try:
        response = subprocess.run(['wget', url, '-O', 'online_wordlist.txt'], capture_output=True, text=True)
        if response.returncode == 0:
            # Read the downloaded file and filter out non-password content
            with open('online_wordlist.txt', 'r') as f:
                lines = f.read().splitlines()
                # Filter lines containing valid passwords
                wordlist = [line for line in lines if is_valid_password(line)]
            return wordlist
        else:
            print("\033[1;31mFailed to download the online leaked password wordlist. Continuing with the local wordlist...\033[0m")
            return None
    except subprocess.CalledProcessError as e:
        print(f"\033[1;31mFailed to download the online leaked password wordlist: {e}. Continuing with the local wordlist...\033[0m")
        return None

def is_valid_password(line):
    # You can define your criteria for valid passwords here
    # For example, you can filter out lines that are too long or contain special characters
    # Modify this function according to your specific requirements
    return len(line) <= 30 and line.isalnum()  # Example: passwords must be alphanumeric and no longer than 30 characters


def crack_hash(cipher, algorithm, charset, password_length, start=0, end=None):
    if end is None:
        end = len(charset) ** password_length + start

    for i, password in enumerate(itertools.product(charset, repeat=password_length), start=start):
        password = "".join(password)
        hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()
        if hashed_password == cipher:
            return password

    return None

def print_progress(progress, total_attempts, password, is_local=True):
    bar_length = 30
    progress_percent = min(100, int(progress / total_attempts * 100))
    progress_bar = "#" * int(progress_percent / 100 * bar_length)

    source = "LOCAL" if is_local else "DOWNLOADED"
    sys.stdout.write(
        f"\r{source} Password Wordlist Progress: [{progress_bar.ljust(bar_length)}] {progress_percent}% | Current password being Checked: {password}")
    sys.stdout.flush()

def crack_with_wordlist(cipher, algorithm, wordlist, is_local=True):
    total_attempts = len(wordlist)

    source = "LOCAL" if is_local else "DOWNLOADED"
    print(f"\nAttempting To Crack Source of Passwords: {source} | Total attempts: {total_attempts}\n")
    print("****************************************************************************************************")
    print("""    
      ⠀⠀⠀⠀⠀⠀⠀⠀⠀                 ⢀⣀⣀⣀⣀⣀⣠⣼⠂⠀⠀⠀⠀⠙⣦⢀⠀⠀⠀⠀⠀⢶⣤⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⠷⢦⠀⣹⣶⣿⣦⣿⡘⣇⠀⠀⠀⢰⠾⣿⣿⣿⣟⣻⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢟⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⡏⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣝⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣿⣿⣿⡇⠀⠀⠀⠀⠛⣿⣿⣷⡀⠘⢿⣧⣻⡷⠀⠀⠀⠀⠀⠀⣿⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣝⢧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⠟⣡⣾⣿⣿⣧⣿⡿⣋⣴⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢻⣿⣿⣿⣶⡄⠙⠛⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⣝⢻⣿⣟⣿⣿⣷⣮⡙⢿⣽⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡿⢋⣴⣿⣿⣿⣿⣿⣼⣯⣾⣿⣿⡿⣻⣿⣿⣿⣦⠀⠀⠀⠀⢀⣹⣿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠻⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣦⡙⢿⣇⠀⠀⠀⠀
⠀⠀⠀⣠⡏⣰⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡿⢋⣼⣿⣿⣿⣿⣿⣷⡤⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢠⣾⣿⣿⣿⣿⣿⣷⡜⢿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣦⡙⣦⠀⠀⠀
⠀⠀⣰⢿⣿⣿⠟⠋⣠⣾⣿⣿⣿⣿⣿⠛⢡⣾⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠻⣿⡟⣿⣿⣿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣟⠻⣿⣆⠙⢿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣟⣧⠀⠀
⠀⣰⢣⣿⡿⠃⣠⡾⠟⠁⠀⣸⣿⡟⠁⢀⣿⠋⢠⣿⡏⣿⣿⣿⣿⣿⢿⠁⢀⣠⣴⢿⣷⣿⣿⣿⠀⠀⠽⢻⣿⣿⣿⣿⡼⣿⡇⠈⢿⡆⠀⠻⣿⣧⠀⠈⠙⢿⣆⠈⠻⣿⣎⢧⠀
⠀⢣⣿⠟⢀⡼⠋⠀⠀⢀⣴⠿⠋⠀⠀⣾⡟⠀⢸⣿⠙⣿⠃⠘⢿⡟⠀⣰⢻⠟⠻⣿⣿⣿⣿⣿⣀⠀⠀⠘⣿⠋⠀⣿⡇⣿⡇⠀⠸⣿⡄⠀⠈⠻⣷⣄⠀⠀⠙⢷⡀⠙⣿⣆⠁
⢀⣿⡏⠀⡞⠁⢀⡠⠞⠋⠁⠀⠀⠀⠈⠉⠀⠀⠀⠿⠀⠈⠀⠀⠀⠀⠀⣿⣿⣰⣾⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⠀⠉⠀⠸⠃⠀⠀⠈⠋⠀⠀⠀⠀⠙⠳⢤⣀⠀⠹⡄⠘⣿⡄
⣸⡟⠀⣰⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠟⠁⠀⠹⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣧⠀⢹⣷
⣿⠃⢠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣤⣀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⣿
⣿⠀⢸⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠉⢻⣧⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸
⡇⠀⠈⠀⠀⠀⠀⠀⠀#Cracking⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢿⣧⡀⠀⠀⣿⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢸
⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾
⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⢀  ⣾⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣀⡼⣿⣿⣾⣤⣀⡼⣿⣿⣾⣤⣠⡼⣿⣿⣾⣀⡼⣿⣿⣾⣤⣠⡼⣤⣠⡼⠀⠀⠀

        """)
    for progress, password in enumerate(wordlist, start=1):
        hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()
        if hashed_password == cipher:
            print("""
                             ⣀⣴⠶⢶⣖⡒⠒⠲⢤⣀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠟⠋⠉⢿⣷⣶⣾⣿⣿⢷⣯⣝⣧⣀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠴⣆⠀⠙⠻⠿⠿⠋⠀⠻⠿⠿⢿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠙⠲⣤⣀⠀⠀⠀⠀⣠⡶⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠒⠶⠯⠭⠍⠉⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣱⣦⣴⣖⣻⣄⡀⠀⠀⣀⣠⠶⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⠄⠒⠉⠁⠀⠀⠀⠀⠹⡛⡅⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡤⣤⣮⡤⣀⣴⣀⡄⠀⢠⢠⢠⣤⣧⢴⣤⣤⠀⡄⠀⡤⢤⡤⠀⠀⠀⠀
⠀⠀⢸⣠⡿⣟⣛⣿⠛⣿⣇⣀⠘⡞⡞⢻⢳⢸⠈⣿⡛⡇⠀⡇⢸⠀⠀⠀⠀⠀
⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠈⠳⠤⣀⡀⠀⠀⠀⠀⠀
⢀⣾⡗⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠉⠙⠒⢦⣄⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈  Intercuba.Net
                                       #CRACKING                                    
                """)
            print("\nPassword found in the password wordlist!!! PASSWORD FOUND:", password)
            print("**********************************************************************")
            return password  # Stop further processing if password found

        print_progress(progress, total_attempts, password, is_local=is_local)
    
    print(f"\nNO Password or Message found in the {source} password wordlist")
    print("****************************************************************************************************")

def crack_with_brute_force(cipher, algorithm):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_password_length = 10
    brute_force_start = 0
    max_attempts = sum(len(charset) ** i for i in range(1, max_password_length + 1))
    print("""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⡒⠤⡀⠀⠀⠀⠀⠀⢠⠃⠀⡞⠆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢢⠀⠀⠀⠀⢅⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⠛⡶⣄⠁⠢⢄⣀⠠⠀⢰⠀⡷⠐⠇⠀⠀⠀⠀⠀⡀⠀⠀⠀⣀⣠⢛⡿⢤⣔⢠⠀⣿⠂⠂⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠢⢤⢸⠍⢂⠄⡀⠁⡇⡄⠀⠀⢀⠆⠀⣇⢀⡄⡽⣿⢩⡇⣯⣿⣿⢥⡠⣮⡁⡇⠀⠀⠀⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠀⠀⢰⠙⡢⢜⣵⣬⣐⠤⢀⠀⠀⢸⠀⠀⣹⡼⠷⠊⠻⠏⠞⢛⠤⣿⠻⣿⣟⣤⠅⠀⢀⠀⡇⠇⠀⠀⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠈⡀⠀⢸⠀⡾⠀⡎⠹⠻⢿⣷⡏⠒⠌⣀⠬⣔⣡⠨⠠⠠⢀⣶⣹⣿⢽⣤⣿⣷⣟⣤⠀⠀⠀⠁⠀⠘⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠀⠘⠈⠃⠈⠁⠀⠀⢀⠩⢒⡄⡀⠀⠈⠪⡀⠄⠠⠢⠄⠟⠈⠉⠏⠉⢟⠛⢯⣯⣹⣿⣿⠀⠀#FREE_CUBA!⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢧⣤⣝⢆⡤⡠⠃⢄⡀⠀⠁⡈⢣⢀⣸⣠⣀⣆⠈⢶⣾⣿⡏⠉⠉⠀⢴⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠠⣠⣄⣒⡮⣭⣯⣷⣺⣅⣄⣀⡠⠤⠾⠒⣾⣿⣿⣿⣿⣿⣿⠿⣄⡠⣠⡊⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣿⠖⣤⣖⠦⠀⣀⣤⣴⡾⠋⠀⠀⠀⠀⠁⠒⠲⠀⠈⠉⠉⣉⣭⣭⡿⠛⠛⢿⣟⣛⣛⣭⠈⠉⣈⣉⣹⣿⣛⣪⣥⡄⠀
⠀⠀⠐⠥⢀⡀⣄⣤⣼⣍⢺⣿⣿⢷⢷⣷⣦⠤⠤⠤⠀⢠⣤⡼⠷⠚⠁⠀⠈⢲⡌⢢⠐⠙⡓⡭⣾⢵⠦⠒⠒⠘⢳⣿⣿⡄⠉⠠
⠀⠀⠀⠀⢰⣋⣻⢿⣿⣿⣻⡯⠋⠀⠁⠠⠀⠐⠀⣀⡠⠞⠉⣵⠆⣠⣶⣺⢻⣿⣿⣷⣥⣤⣨⡐⡀⠀⠈⠀⠀⠀⢰⡎⢣⣰⠀⠠
⠀⠀⠀⠀⢸⢀⣀⣀⣿⡉⣹⡇⡤⣴⢲⡒⣶⠴⡤⢤⣂⣀⡿⣡⠾⠯⠅⢠⣿⣷⣿⣿⣿⣿⣿⣿⣷⣦⣄⡂⠀⠀⢸⣷⣿⣿⡆⠀
⠀⠀⠀⠀⢘⡤⠄⠤⢼⣿⣿⣿⡈⠈⠁⣗⠙⠛⠛⠛⠓⠛⠻⢿⠤⢄⠤⠤⣿⡟⣝⡇⣸⣿⣝⣮⣿⣿⣽⡟⢟⡟⣿⣿⣷⣿⠃⠀
⠀⠀⠀⠀⠀⢿⣿⣣⣚⣿⣿⣿⣯⣶⣮⣽⣤⣄⠀⣰⣳⣤⣤⣻⣒⠛⡂⠐⢻⡱⢸⣧⣿⡟⡿⣿⠙⠁⣿⠈⠸⣿⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣷⣳⣚⣿⣟⡝⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣧⠀⢡⣈⠭⡆⢨⣿⣿⣇⢿⣿⣴⠄⣿⡦⢰⣿⣿⣿⡝⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣦⣆⢘⣿⣿⣿⣯⢿⣿⣜⣿⣧⠼⢿⣟⣹⠀⠄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠀⠀⠀⠉⠉⠁⠉⠉⠉⠋⠛⠛⠿⠿⠽⠛⠟⠙⠛⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
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
                   ⢀⣀⣀⣀⣀⣀⣠⣼⠂⠀⠀⠀⠀⠙⣦⢀⠀⠀⠀⠀⠀⢶⣤⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⠷⢦⠀⣹⣶⣿⣦⣿⡘⣇⠀⠀⠀⢰⠾⣿⣿⣿⣟⣻⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢟⣥⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⡏⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣝⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣿⣿⣿⡇⠀⠀⠀⠀⠛⣿⣿⣷⡀⠘⢿⣧⣻⡷⠀⠀⠀⠀⠀⠀⣿⣿⣿⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣝⢧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⠟⣡⣾⣿⣿⣧⣿⡿⣋⣴⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢻⣿⣿⣿⣶⡄⠙⠛⠁⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⣝⢻⣿⣟⣿⣿⣷⣮⡙⢿⣽⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡿⢋⣴⣿⣿⣿⣿⣿⣼⣯⣾⣿⣿⡿⣻⣿⣿⣿⣦⠀⠀⠀⠀⢀⣹⣿⣿⣿⣿⣶⣤⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⠻⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣦⡙⢿⣇⠀⠀⠀⠀
⠀⠀⠀⣠⡏⣰⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⡿⢋⣼⣿⣿⣿⣿⣿⣷⡤⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢠⣾⣿⣿⣿⣿⣿⣷⡜⢿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣦⡙⣦⠀⠀⠀
⠀⠀⣰⢿⣿⣿⠟⠋⣠⣾⣿⣿⣿⣿⣿⠛⢡⣾⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠻⣿⡟⣿⣿⣿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣟⠻⣿⣆⠙⢿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⣟⣧⠀⠀
⠀⣰⢣⣿⡿⠃⣠⡾⠟⠁⠀⣸⣿⡟⠁⢀⣿⠋⢠⣿⡏⣿⣿⣿⣿⣿⢿⠁⢀⣠⣴⢿⣷⣿⣿⣿⠀⠀⠽⢻⣿⣿⣿⣿⡼⣿⡇⠈⢿⡆⠀⠻⣿⣧⠀⠈⠙⢿⣆⠈⠻⣿⣎⢧⠀
⠀⢣⣿⠟⢀⡼⠋⠀⠀⢀⣴⠿⠋⠀⠀⣾⡟⠀⢸⣿⠙⣿⠃⠘⢿⡟⠀⣰⢻⠟⠻⣿⣿⣿⣿⣿⣀⠀⠀⠘⣿⠋⠀⣿⡇⣿⡇⠀⠸⣿⡄⠀⠈⠻⣷⣄⠀⠀⠙⢷⡀⠙⣿⣆⠁
⢀⣿⡏⠀⡞⠁⢀⡠⠞⠋⠁⠀⠀⠀⠈⠉⠀⠀⠀⠿⠀⠈⠀⠀⠀⠀⠀⣿⣿⣰⣾⣿⣿⣿⣿⣿⣿⣤⠀⠀⠀⠀⠀⠉⠀⠸⠃⠀⠀⠈⠋⠀⠀⠀⠀⠙⠳⢤⣀⠀⠹⡄⠘⣿⡄
⣸⡟⠀⣰⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠟⠁⠀⠹⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣧⠀⢹⣷
⣿⠃⢠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣤⣀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⣿
⣿⠀⢸⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠉⢻⣧⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸
⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⡀⠀⠀⣿⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢸
⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾
⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⢀  ⣾⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⣀⡼⣿⣿⣾⣤⣀⡼⣿⣿⣾⣤⣠⡼⣿⣿⣾⣀⡼⣿⣿⣾⣤⣠⡼⣤⣠⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         
     InterCuba.Net                           
     S.S.A_Hash_Cracker                   
                             
    """
    print("\033[1;32m" + banner + "\033[0m")

def main():
    algorithms = list(hashlib.algorithms_guaranteed)
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_password_length = 10

    try:
        clear_screen()
        print_banner()
        print("**************************************************************")
        print("\033[1;34mWhat hashing algorithm do you want to crack?:\033[0m")
        print("**************************************************************")
        print("Algorithms:", algorithms)

        while True:
            print("*************************************************************")
            algorithm = input("Please enter the algorithm type: ").lower()
            if algorithm in algorithms:
                break
            else:
                print("\033[1;31mInvalid algorithm.\033[0m")

        print("\033[1;34mEnter the hash to crack:\033[0m")
        cipher = input().strip()

        if not cipher:
            print("\033[1;31mInvalid hash. Please enter a valid hash.\033[0m")
            return

        online_wordlist_url = "https://raw.githubusercontent.com/josuamarcelc/common-password-list/main/rockyou.txt/rockyou_1.txt"
        online_wordlist = download_online_wordlist(online_wordlist_url)
        found_password = None  # Initialize found_password here

        # Check downloaded online wordlist
        if online_wordlist:
            found_password = crack_with_wordlist(cipher, algorithm, online_wordlist, is_local=False)

        # Check the local password list
        if not found_password:
            with open("Passwords.txt", "r", encoding="latin-1", errors="replace") as f:
                local_wordlist = f.read().splitlines()
            found_password = crack_with_wordlist(cipher, algorithm, local_wordlist, is_local=True)

        # If not found in both wordlists, attempt brute force
        if not found_password:
            crack_with_brute_force(cipher, algorithm)

    except KeyboardInterrupt:
        print("\n\033[1;31mCracking process interrupted.\033[0m")

if __name__ == "__main__":
    main()
