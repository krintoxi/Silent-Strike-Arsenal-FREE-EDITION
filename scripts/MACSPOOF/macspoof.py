import subprocess
import random
import platform
import sys
#INTERCUBA.NET
def random_mac_address():
    return ':'.join([f"{random.randint(0x00, 0xFF):02x}" for _ in range(6)])

def get_original_mac(interface):
    if platform.system() == "Windows":
        reg_query_cmd = ['reg', 'query', r'HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\{interface}\Ndi', '/v', 'NetworkAddress']
        reg_query_result = subprocess.check_output(reg_query_cmd, shell=True).decode('utf-8')
        original_mac = reg_query_result.split()[-1]
        return original_mac
    else:
        ifconfig_cmd = ['ifconfig', interface]
        ifconfig_result = subprocess.check_output(ifconfig_cmd).decode('utf-8')
        for line in ifconfig_result.split('\n'):
            if 'ether ' in line:
                original_mac = line.split('ether ')[-1].strip()
                return original_mac
        return None

def get_network_interfaces():
    try:
        if platform.system() == "Windows":
            ifconfig_result = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
        else:
            ifconfig_result = subprocess.check_output(['ifconfig']).decode('utf-8')

        interfaces = []

        for line in ifconfig_result.split('\n'):
            if line.strip() != '':
                if platform.system() == "Windows":
                    if "Ethernet adapter" in line or "Wireless LAN adapter" in line:
                        interface = line.split(':')[1].strip()
                    elif "Physical Address" in line:
                        mac_address = line.split(':')[1].strip()
                        interfaces.append((interface, mac_address))
                else:
                    if line[0].isalnum():
                        interface = line.split(':')[0]
                        mac_address = None
                    elif line.strip().startswith('ether'):
                        mac_address = line.strip().split()[1]
                    else:
                        continue

                    if mac_address:
                        interfaces.append((interface, mac_address))

        return interfaces

    except Exception as e:
        print("Error occurred while listing network interfaces:")
        print(e)
        return []

def spoof_mac_address(interface, new_mac):
    try:
        if platform.system() == "Windows":
            subprocess.call(['netsh', 'interface', 'set', 'interface', interface, 'admin=disable'])
            subprocess.call(['reg', 'add', r'HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\{interface}\Ndi', '/v', 'NetworkAddress', '/d', new_mac, '/f'])
            subprocess.call(['netsh', 'interface', 'set', 'interface', interface, 'admin=enable'])
        else:
            subprocess.call(['sudo', 'ifconfig', interface, 'down'])
            subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
            subprocess.call(['sudo', 'ifconfig', interface, 'up'])

    except Exception as e:
        print("Error occurred while spoofing MAC address:")
        print(e)

def revert_mac_address(interface, original_mac):
    try:
        spoof_mac_address(interface, original_mac)
        print(f"MAC address for {interface} has been reverted to its original value: {original_mac}.")
    except Exception as e:
        print("Error occurred while reverting MAC address:")
        print(e)

def print_menu(interfaces):
    print("\033[36m╔════════════════════════════════════════╗")
    print("       \033[31mAvailable network interfaces!:\033[36m      ")
    print("╚════════════════════════════════════════╝\033[0m")

    for i, (interface, mac) in enumerate(interfaces, 1):
        status = "UP" if "UP" in subprocess.check_output(['ifconfig', interface]).decode() else "DOWN"
        ip_addresses = [line.split()[1] for line in subprocess.check_output(['ifconfig', interface]).decode().splitlines() if "inet " in line]
        print(f"\033[36m{i}. \033[0m{interface} (\033[32mMAC:\033[0m \033[35m{mac}\033[0m, \033[32mStatus:\033[0m \033[35m{status}\033[0m, \033[32mIP Addresses:\033[0m \033[35m{', '.join(ip_addresses)}\033[0m)")
    print(f"\033[36m{i + 1}. \033[0mRevert all interfaces to original MAC addresses")
    print(f"\033[36m{i + 2}. \033[0mQuit")

def main():
    print("\033[36m╔════════════════════════════════════════╗")
    print("           \033[31mWelcome to MACSPOOF!\033[36m      ")

    # Ask for the operating system
    os_choice = input("\033[36mEnter your operating system (\033[32mLinux\033[0m, \033[32mWindows\033[0m, or \033[32mMacOS\033[0m): \033[0m").strip().lower()

    if os_choice not in ["linux", "windows", "macos"]:
        print("Invalid operating system choice. Exiting.")
        sys.exit(1)

    # Get the available network interfaces and their MAC addresses
    interfaces = get_network_interfaces()

    if len(interfaces) == 0:
        print("No network interfaces found.")
        sys.exit(1)

    while True:
        print_menu(interfaces)
        choice = input("\033[36mEnter the number of the interface you want to spoof (or press Enter to quit): \033[0m").strip()

        if not choice:
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > len(interfaces) + 2:
                print("Invalid choice. Please enter a valid number.")
                continue

            if choice == len(interfaces) + 1:
                print("\033[36mReverting all interfaces to original MAC addresses...\033[0m")
                for interface, original_mac in interfaces:
                    revert_mac_address(interface, original_mac)
                break

            if choice == len(interfaces) + 2:
                print("Exiting MACSPOOF.")
                break

            interface, original_mac = interfaces[choice - 1]
            new_mac = random_mac_address()

            print(f"\033[36mChanging MAC address for {interface} to {new_mac}...\033[0m")
            spoof_mac_address(interface, new_mac)

            print(f"\033[36mMAC address for {interface} has been changed to {new_mac}.\033[0m")

            revert = input("\033[36mDo you want to revert to the original MAC address later? (\033[32my\033[36m/\033[32mn\033[36m): \033[0m").strip().lower()
            if revert == 'n':
                revert_mac_address(interface, original_mac)

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
