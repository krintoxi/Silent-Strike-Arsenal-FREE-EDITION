**ᴹ‧ᴬ‧ᶜ ᔆᵖᵒᵒᶠ - MAC Address Spoofer**

MAC SPOOF is a Python script that enables users to spoof MAC addresses for network interfaces on Linux, Windows, and macOS operating systems. The script provides a user-friendly command-line interface to list available network interfaces, change the MAC address for any desired interface, and offers the option to revert the MAC address back to its original value.


## Features

- Random MAC address generation: The script generates a random 6-byte MAC address in the format "XX:XX:XX:XX:XX:XX".
- Get original MAC address: Retrieve the original MAC address of a given network interface on Windows or non-Windows systems.
- Get network interfaces: List all available network interfaces along with their current MAC addresses, status (UP or DOWN), and associated IP addresses.
- Spoof MAC address: Change the MAC address of a specific network interface using platform-specific commands for Windows and non-Windows systems.
- Revert MAC address: Revert a specific network interface's MAC address back to its original value.
- User-friendly interface: The script offers an interactive command-line interface with options for selecting the operating system, interface to spoof, and MAC address reversion.
- Graceful Exit: Provides an option to quit the program at any point during the interface selection.

## Prerequisites

- Python 3.x
- Administrator (root) privileges are required to change the MAC address on non-Windows systems.

## How to Use

1. Clone the repository or download the `macspoof.py` script.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the script using the following command:
   ```bash
   python3 macspoof.py
   ```
4. The script will prompt you to select your operating system (Linux, Windows, or macOS).
5. After selecting the operating system, the available network interfaces will be listed with their respective MAC addresses, status, and IP addresses.
6. Choose an interface to spoof its MAC address.
7. The script will generate a new random MAC address and apply it to the selected interface.
8. You will be prompted to decide whether to revert to the original MAC address immediately or later.
9. To exit the script gracefully, choose the appropriate option during the interface selection.

## Example Usage

```bash
$ python3 macspoof.py
Welcome to MACSPOOF!

Enter your operating system (Linux, Windows, or MacOS): linux

╔════════════════════════════════════════╗
       Available network interfaces!:
╚════════════════════════════════════════╝

1. eth0 (MAC: 00:11:22:33:44:55, Status: UP, IP Addresses: 192.168.1.100, fe80::1)
2. wlan0 (MAC: aa:bb:cc:dd:ee:ff, Status: UP, IP Addresses: 192.168.0.101, fe80::2)

Enter the number of the interface you want to spoof (or press Enter to quit): 1
Changing MAC address for eth0 to 12:34:56:78:90:ab...
MAC address for eth0 has been changed to 12:34:56:78:90:ab.

Do you want to revert to the original MAC address later? (y/n): y
MAC address for eth0 has been reverted to its original value: 00:11:22:33:44:55.

Enter the number of the interface you want to spoof (or press Enter to quit): 2
Changing MAC address for wlan0 to 98:76:54:32:10:fe...
MAC address for wlan0 has been changed to 98:76:54:32:10:fe.

Do you want to revert to the original MAC address later? (y/n): n

Enter the number of the interface you want to spoof (or press Enter to quit): 
```

## Disclaimer

MAC address spoofing should only be performed with the necessary permissions and for legitimate purposes. The authors of this script are not responsible for any misuse or illegal activities. Use at your own risk.

## Credits

This script was created by [InterCuba.Net] ([@krintoxi](https://github.com/username)).

---
