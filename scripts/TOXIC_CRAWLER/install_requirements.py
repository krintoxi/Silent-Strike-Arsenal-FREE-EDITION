import os
import platform
import subprocess
import sys


def install_requirements():
    requirements = ["requests","beautifulsoup4","jinja2","googlesearch-python","reportlab","fpdf","duckduckgo-search"]

    try:
        for requirement in requirements:
            subprocess.check_call([sys.executable, "-m", "pip", "install", requirement])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install requirements. Make sure you have pip installed.")
        exit(1)


def main():
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
    print("You can now run the main monitoring script 'firewall_monitor.py'.")
    print("Remember to run it with administrative privileges for proper network packet capturing.")
    print("Enjoy monitoring your network traffic and system resources with Firewall Monitoring Tool!")


if __name__ == "__main__":
    main()
