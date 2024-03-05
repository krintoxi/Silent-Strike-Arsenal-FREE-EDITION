import subprocess
import sys

def run_shell_command(command):
    """Executes a shell command and returns its output."""
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing: {command}")
        sys.exit(1)

def install_system_dependencies():
    """Installs system-wide dependencies."""
    dependencies = "gnome-terminal python3-pip python3-pil python3-pil.imagetk python3-tk"
    print("Installing system dependencies...")
    run_shell_command(f"sudo apt update && sudo apt install -y {dependencies}")

def install_python_packages(packages):
    """Installs Python packages using pip."""
    try:
        subprocess.run(["pip3", "install"] + packages, check=True)
    except subprocess.CalledProcessError:
        print("Error installing Python packages. Ensure pip is installed and try again.")
        sys.exit(1)

def check_required_packages(packages):
    """Checks if the required Python packages are installed."""
    missing_packages = []
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    return missing_packages

def main():
    print("Welcome to the S.S.A Installer and Updater!")
    print("\033[32m" + "\033[0m")
    print("""
                          LIBERTAD!         \☻/\☻/
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▌░ ▌
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ / \░ / \
███████ ]▄▄▄▄▄▄▄▄▄-----------●
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▂▄▅█████████▅▄▃▂
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░I███████████████████].
""")
    print("\033[36m╔════════════════════════════════════════════════╗")
    print("║    \033[31mWelcome to the S.S.A Installer and Updater!\033[36m║")
    print("╚════════════════════════════════════════════════╝\033[0m")
    print("Loading.....please be patient..")
    required_packages = ["questionary", "matplotlib", "tabulate", "sqlite3", "Pillow", "requests", "tk", "pybnb"]
    missing_packages = check_required_packages(required_packages)

    if missing_packages:
        response = input("Required packages are missing. Do you want to install them? (y/n): ").strip().lower()
        if response == "y":
            install_system_dependencies()
            install_python_packages(missing_packages)
            print("Required packages installed and updated successfully.")
            if input("Launch S.S.A? (y/n): ").strip().lower() == "y":
                run_shell_command("python3 SSA.pyc")
        else:
            print("Please install the required packages manually before running the Control Panel script.")
            sys.exit(1)
    else:
        print("Required packages are already installed. You can go ahead and run S.S.A.")

if __name__ == "__main__":
    main()
