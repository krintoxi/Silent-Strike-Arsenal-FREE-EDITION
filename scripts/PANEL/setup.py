import subprocess
import sys

def install_required_packages(packages):
    try:
        subprocess.run(["pip", "install"] + packages, check=True)
    except subprocess.CalledProcessError as e:
        print("Error installing required packages. Make sure you have pip installed.")
        sys.exit(1)

def check_required_packages(packages):
    missing_packages = []
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    return missing_packages

if __name__ == "__main__":


    print("\033[32m" + "\033[0m")
    print("\033[36m╔════════════════════════════════════════════════╗")
    print("║      \033[31mWelcome to the Control Panel Setup!\033[36m       ║")
    print("╚════════════════════════════════════════════════╝\033[0m")

    required_packages = ["questionary", "matplotlib", "tabulate", "hashlib", "sqlite3"]
    missing_packages = check_required_packages(required_packages)

    if not missing_packages:
        print("Required packages are already installed.")
        print("You can go ahead and run Panel.py")
    else:
        response = input("\033[31mRequired packages are missing. Do you want to install them? (y/n): \033[0m").lower()
        if response == "y":
            install_required_packages(missing_packages)
            print("\033[32mRequired packages installed successfully.\033[0m")
        else:
            print("\033[33mPlease install the required packages manually before running the Control Panel script.\033[0m")
            sys.exit(1)
