import os
import platform
import subprocess
import sys


def install_requirements():
    requirements = ["scapy","psutil","netifaces","colorama","bcrypt","argon2","tqdm"]

    try:
        for requirement in requirements:
            subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install requirements. Make sure you have pip installed.")
        exit(1)


def main():
    print("Firewall Monitoring Tool - Requirements Installation")
    print("---------------------------------------------------")
    print("This script will install the necessary libraries required .")
    print("Ensure you have administrative privileges to install packages.")

    os_choice = platform.system().lower()

    if os_choice not in ['linux', 'darwin', 'windows']:
        print("Unsupported operating system.")
        exit(1)

    if os_choice == 'windows':
        print("Windows OS detected. Ensure you have Npcap installed for packet capturing.")

    print("Installing required libraries...")
    install_requirements()

    print("Installation completed successfully.")
    print("Remember to run it with administrative privileges for proper network packet capturing.")

if __name__ == "__main__":
    main()
