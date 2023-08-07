import importlib.util
import subprocess
import sys

required_packages = [
    'hashlib',
    'bcrypt',
    'scrypt',
    'argon2',
    'tqdm',
]

def check_and_install(package):
    try:
        importlib.util.find_spec(package)
    except ImportError:
        print(f"Installing '{package}' library...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', package])

def install_required_packages():
    for package in required_packages:
        check_and_install(package)

def main():
    print("Checking and installing required packages...")
    install_required_packages()
    print("All required packages installed successfully!")

if __name__ == '__main__':
    main()
