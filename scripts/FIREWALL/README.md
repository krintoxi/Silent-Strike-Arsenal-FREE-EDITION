# Firewall Monitoring Tool

The Firewall Monitoring Tool is a script that monitors network traffic on a specified interface, identifies potential threats, and displays live logs of network connections. It can detect blocked connections based on a blocklist of domains and specific keywords present in domain names.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [Features](#features)
- [Security Considerations](#security-considerations)
- [Dependencies](#dependencies)

## Overview
The Firewall Monitoring Tool is designed to provide network administrators with an insight into the network traffic on a given interface. It identifies suspicious connections based on a predefined blocklist of domains and keywords. The tool displays live logs of network connections and blocked connections, allowing administrators to monitor potential threats in real time.

## Usage
1. Run the script: `python firewall_monitor.py`.
2. Select the operating system (`linux`, `macos`, or `windows`).
3. The script will list available interfaces with IP addresses other than `127.0.0.1`.
4. Choose the index of the interface you want to monitor.
5. The tool will start monitoring network traffic and displaying live logs.
6. The tool will detect and display blocked connections based on the blocklist and keywords.

## Features
- Monitors network traffic on a specified interface.
- Identifies suspicious connections based on a blocklist of domains.
- Detects specific keywords in domain names for potential threats.
- Displays live logs of network connections and blocked connections.
- Supports Linux, MacOS, and Windows operating systems.

## Security Considerations
- This tool provides basic network monitoring and detection capabilities. 
- Use this tool as part of a broader security strategy .
- Ensure that the blocklist and keywords are updated regularly to reflect current threats.

## Dependencies
- Python 3.x
- `scapy`: A powerful packet manipulation library for network protocols.
- `tabulate`: A Python library for tabular data visualization.
- `netifaces`: A Python library for querying network interface information.
- `colorama`: A Python library for adding colored text output to the terminal.
