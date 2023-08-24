import os
import platform
import datetime
import socket
import struct
import fcntl
import argparse
from threading import Thread
from scapy.all import sniff, IP, TCP, Raw
from tabulate import tabulate
import time
import netifaces as ni
from colorama import Fore, Style

BLOCKLIST = ["example.com", "maliciousdomain.org","93.184.216.34"]  # Add blocklisted domains here
KEYWORDS = ["porn", "hacker", "virus", ".exe"]  # Add keywords to check in domain names

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_interface():
    print("Available interfaces:")
    interfaces_info = []
    for iface in ni.interfaces():
        addrs = ni.ifaddresses(iface)
        if ni.AF_INET in addrs:
            ip = addrs[ni.AF_INET][0]['addr']
            try:
                is_up = ni.ifaddresses(iface)[ni.AF_INET][0]['broadcast']
            except KeyError:
                is_up = False

            if ip != "127.0.0.1" and is_up:
                interfaces_info.append((iface, ip))

    if not interfaces_info:
        print("No interfaces with IP address other than 127.0.0.1 found.")
        return None

    headers = ["Index", "Interface", "IP"]
    print(tabulate(enumerate(interfaces_info), headers=headers, tablefmt="grid"))

    selected_idx = int(input("Enter the index of the interface to monitor: "))
    interface = interfaces_info[selected_idx][0]
    return interface

def get_os():
    parser = argparse.ArgumentParser(description="Firewall Monitoring Tool")
    parser.add_argument(
        "os_choice",
        choices=["linux", "macos", "windows"],
        help="Select the operating system (Linux/MacOS/Windows)",
    )
    args = parser.parse_args()
    return args.os_choice

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def resolve_ip_to_domain(ip):
    try:
        domain_name = socket.gethostbyaddr(ip)[0]
        return domain_name
    except socket.herror:
        return ip

def check_keywords(domain):
    for keyword in KEYWORDS:
        if keyword in domain.lower():
            return True
    return False

def parse_http_request(payload):
    try:
        payload = payload.decode()
        request_line, headers = payload.split("\r\n", 1)
        method, path, version = request_line.split(" ")
        return method, path
    except Exception:
        return None, None

def read_packet(packet_data):
    eth_length = 14  # Ethernet header length

    if packet_data.haslayer(IP):
        ip_header = packet_data[IP]

        src_ip = ip_header.src
        dst_ip = ip_header.dst
        protocol = ip_header.proto
        packet_length = len(packet_data)

        src_domain = resolve_ip_to_domain(src_ip)
        dst_domain = resolve_ip_to_domain(dst_ip)

        transport_layer = packet_data.payload
        src_port = "N/A"
        dst_port = "N/A"
        traffic_type = "N/A"
        website = "N/A"

        if isinstance(transport_layer, TCP):
            src_port = transport_layer.sport
            dst_port = transport_layer.dport

            if isinstance(transport_layer.payload, Raw):
                http_method, http_path = parse_http_request(transport_layer.payload.load)
                if http_method and http_path:
                    traffic_type = "HTTP"
                    website = http_path.split("/", 1)[0]

                    if website != "N/A" and check_keywords(website):
                        print(Fore.RED + f"ALERT: Blocked connection to {website} (IP: {dst_ip})" + Style.RESET_ALL)
                        blocked_connections.append([get_timestamp(), src_domain, src_ip, dst_domain, dst_ip, protocol, packet_length, src_port, dst_port, traffic_type])

        if is_ip_in_blocklist(src_ip) or is_ip_in_blocklist(dst_ip):
            print(Fore.RED + f"ALERT: Blocked connection to {dst_ip}" + Style.RESET_ALL)
            blocked_connections.append([get_timestamp(), src_domain, src_ip, dst_domain, dst_ip, protocol, packet_length, src_port, dst_port, traffic_type])

        network_log.append([get_timestamp(), src_domain, src_ip, dst_domain, dst_ip, protocol, packet_length, src_port, dst_port, traffic_type])

def is_ip_in_blocklist(ip):
    for domain in BLOCKLIST:
        try:
            resolved_ip = socket.gethostbyname(domain)
            if resolved_ip == ip:
                return True
        except socket.gaierror:
            pass
    return False

def monitor_network_traffic(interface):
    sniff(iface=interface, prn=read_packet, lfilter=lambda pkt: IP in pkt)

def display_live_logs():
    headers = ["Timestamp", "Source Domain", "Source IP", "Destination Domain", "Destination IP", "Protocol", "Length", "Source Port", "Destination Port", "Traffic Type"]
    while True:
        clear_screen()
        print(Fore.CYAN + "Latest Connections" + Style.RESET_ALL)
        print(tabulate(network_log[-10:], headers=headers, tablefmt="fancy_grid"))

        print(Fore.RED + "\nLatest Blocked Connections" + Style.RESET_ALL)
        print(tabulate(blocked_connections[-10:], headers=headers, tablefmt="fancy_grid"))

        time.sleep(1)

if __name__ == "__main__":
    network_log = []
    blocked_connections = []

    os_choice = get_os()
    interface = get_interface()

    clear_screen()
    if not interface:
        print("Exiting the firewall monitoring tool.")
    else:
        print(f"Starting Firewall monitoring tool for {os_choice} on interface {interface}")

        network_thread = Thread(target=monitor_network_traffic, args=(interface,))
        display_thread = Thread(target=display_live_logs)

        network_thread.daemon = True
        display_thread.daemon = True

        network_thread.start()
        display_thread.start()

        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("\nFirewall monitoring tool terminated.")
