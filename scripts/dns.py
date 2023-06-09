import importlib
import os
import webbrowser
import socket

def install_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name} is already installed.")
    except ImportError:
        print(f"⚠️ {package_name} is not found. Installing {package_name}...")
        try:
            import pip
            pip.main(["install", package_name])
            print(f"✅ {package_name} has been successfully installed.")
        except ImportError:
            print(f"❌ Failed to install {package_name}. Make sure you have pip installed.")

def get_domain_info(domain_name):
    try:
        import whois

        # Gather IP information
        ip_address = socket.gethostbyname(domain_name)

        # Fetch WHOIS information
        domain = whois.whois(domain_name)

        # Create the HTML content with enhanced styling
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
            </table>
        </body>
        </html>
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

# Check if pip is installed
try:
    import pip
    print("✅ pip is already installed.")
except ImportError:
    print("❌ pip is not found. You need to install pip.")
    input("Press Enter to continue after installing pip.")
    print("")

# Install python-whois library
install_package("python-whois")
print("")

# Prompt user for the domain name
domain_name = input("Enter the domain name: ")

# Call the function to fetch the domain information and generate the HTML file
get_domain_info(domain_name)
