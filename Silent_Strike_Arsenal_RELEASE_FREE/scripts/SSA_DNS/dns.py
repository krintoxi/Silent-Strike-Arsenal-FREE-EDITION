import importlib
import os
import webbrowser
import socket
import whois
import ssl
import requests
import json
import subprocess
import threading
import time
from tqdm import tqdm

# Initialize port_scan_result as an empty dictionary
port_scan_result = {"result": ""}

def get_domain_info(domain_name):

    def scan_ports(ip_address):
        try:
            nmap_command = f"nmap -v -n -p- --host-timeout 120s {ip_address}"
            print("""
░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
░░░░░░▐▌░░░░▀▀███████▀
▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒""")
            print("Scanning ports using NMAP... This Will TIMEOUT at 120 Seconds. ")
            print("Be Patient...")
            proc = subprocess.Popen(nmap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            for line in iter(proc.stdout.readline, ""):
                port_scan_result["result"] += line

        except Exception as e:
            print("Port scanning failed. Make sure nmap is installed.")

    try:
        print("Getting domain information for:", domain_name)
        
        # Gather IP information
        ip_address = socket.gethostbyname(domain_name)
        print("IP Address:", ip_address)

        # Fetch WHOIS information
        domain = whois.whois(domain_name)

        # Retrieve SSL Certificate Information
        try:
            cert = ssl.get_server_certificate((domain_name, 443))
            certificate_info = ssl.PEM_cert_to_DER_cert(cert)
            certificate_issuer = certificate_info.get('issuer', 'Not Found')
            certificate_expiration_date = certificate_info.get('notAfter', 'Not Found')
        except Exception as e:
            certificate_issuer = 'Not Found'
            certificate_expiration_date = 'Not Found'

        # Retrieve HTTP Response Headers
        try:
            response = requests.get(f"https://{domain_name}")
            headers = response.headers
            security_headers = {
                "Content-Security-Policy": headers.get("Content-Security-Policy", "Not Found"),
                "Strict-Transport-Security": headers.get("Strict-Transport-Security", "Not Found"),
                "X-Frame-Options": headers.get("X-Frame-Options", "Not Found"),
            }
        except Exception as e:
            security_headers = {
                "Content-Security-Policy": "Not Found",
                "Strict-Transport-Security": "Not Found",
                "X-Frame-Options": "Not Found",
            }

        # Retrieve geolocation information (requires API key)
        try:
            geolocation_url = f"https://ip-api.com/json/{ip_address}?fields=country,regionName,city,lat,lon"
            response = requests.get(geolocation_url)
            geolocation_data = response.json()
        except Exception as e:
            geolocation_data = {
                "country": "Not Found",
                "regionName": "Not Found",
                "city": "Not Found",
                "lat": "Not Found",
                "lon": "Not Found",
            }

        # Subdomain Scanning
        try:
            subdomains = []
            subdomain_results = socket.gethostbyaddr(ip_address)
            subdomains.append(subdomain_results[0])
        except Exception as e:
            subdomains = ["Not Found"]
        print("Subdomains:", ', '.join(subdomains))

        # Start a separate thread for port scanning
        port_scan_thread = threading.Thread(target=scan_ports, args=(ip_address,))
        port_scan_thread.start()

        # Create the HTML content with enhanced styling, including the actual data
        html_content = f'''
        <html>
        <head>
            <title>Domain Information: {domain_name}</title>
            <style>
                body {{
                    font-family: Courier, monospace;
                    background-color: black;
                    color: #0f0;
                    padding: 30px;
                }}
                h1 {{
                    font-size: 24px;
                    color: #f00;
                    text-decoration: underline;
                }}
                table {{
                    margin-top: 20px;
                }}
                th {{
                    padding: 5px;
                    background-color: #0f0;
                    color: black;
                    font-weight: bold;
                    text-align: left;
                }}
                td {{
                    padding: 5px;
                    color: #0f0;
                }}
            </style>
        </head>
        <body>
            <h1>Domain Information: {domain_name}</h1>
            <pre>                      
              .   *        .       .
         *      -0-
            .                .  *       - )-
         .      *       o       .       * S.S.A
   o                |                     Domain Information Scout
             .     -O-
  .                 |        *      .     -0-
         *  o     .    '       *      .        o
                .         .        |      *
     *             *              -O-          .
           .             *         |     ,
 Intercuba.net                 .           o
          .---.
    =   _/__~0_\_     .  *            o       '
   = = (_________)             .
                   .                        *
         *               - ) -       *
                .               .</pre>
            <table>
                <tr>
                    <th>IP Address</th>
                    <td>{ip_address}</td>
                </tr>
                <tr>
                    <th>Domain Name</th>
                    <td>{domain.name}</td>
                </tr>
                <tr>
                    <th>Registrar</th>
                    <td>{domain.registrar}</td>
                </tr>
                <!-- Other domain information -->
                <!-- ... -->
                <tr>
                    <th>Subdomains</th>
                    <td>{', '.join(subdomains)}</td>
                </tr>
                <tr>
                    <th>Creation Date</th>
                    <td>{domain.creation_date}</td>
                </tr>
                <tr>
                    <th>Expiration Date</th>
                    <td>{domain.expiration_date}</td>
                </tr>
                <tr>
                    <th>Updated Date</th>
                    <td>{domain.updated_date}</td>
                </tr>
                <tr>
                    <th>Name Servers</th>
                    <td>{domain.name_servers}</td>
                </tr>
                <tr>
                    <th>Status</th>
                    <td>{domain.status}</td>
                </tr>
                <tr>
                    <th>Emails</th>
                    <td>{domain.emails}</td>
                </tr>
                <tr>
                    <th>DNSSEC</th>
                    <td>{domain.dnssec}</td>
                </tr>
                <tr>
                    <th>WHOIS Server</th>
                    <td>{domain.whois_server}</td>
                </tr>
                <tr>
                    <th>Referral URL</th>
                    <td>{domain.referral_url}</td>
                </tr>
                <tr>
                    <th>SSL Certificate Issuer</th>
                    <td>{certificate_issuer}</td>
                </tr>
                <tr>
                    <th>SSL Certificate Expiration Date</th>
                    <td>{certificate_expiration_date}</td>
                </tr>
                <tr>
                    <th>HTTP Headers</th>
                    <td>{json.dumps(security_headers)}</td>
                </tr>
                <tr>
                    <th>Geolocation</th>
                    <td>{json.dumps(geolocation_data)}</td>
                </tr>
            </table>
        </body>
        </html>
        '''

        # Wait for the port scanning thread to finish
        port_scan_thread.join()

        # Add port scan result to the HTML content
        html_content += f'''
        <table>
            <tr>
                <th>Port/NMAP Scan Result</th>
                <td>{port_scan_result["result"]}</td>
            </tr>
        </table>
        '''

        # Create a new folder for the output files
        folder_name = "Whois Results"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Save the HTML content to a file inside the folder
        file_name = f"{domain_name}_whois_info.html"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write(html_content)

        # Open the file with the default web browser
        webbrowser.open(file_path)

        # Get the absolute path of the file
        abs_file_path = os.path.abspath(file_path)
        print(f"✅ HTML file generated and opened in the default web browser.")
        print(f"ℹ️ Output file: {abs_file_path}")

    except Exception as e:
        print("❌ An error occurred:", str(e))


# Prompt user for the domain name
print("""              .   *        .       .
         *      -0-
            .                .  *       - )-
         .      *       o       .       * S.S.A
   o                |                     Domain Information Scout
             .     -O-
  .                 |        *      .     -0-
         *  o     .    '       *      .        o
                .         .        |      *
     *             *              -O-          .
           .             *         |     ,
 Intercuba.net                 .           o
          .---.
    =   _/__~0_\_     .  *            o       '
   = = (_________)             .
                   .                        *
         *               - ) -       *""")
print("*************************************")
domain_name = input("❌ Enter the domain name: ")

# Call the function to fetch the domain information and generate the HTML file
get_domain_info(domain_name)
