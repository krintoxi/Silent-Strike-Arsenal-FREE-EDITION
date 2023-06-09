import importlib
import sys


def check_module(module_name):
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(f"Required module '{module_name}' is not installed.")
        choice = input(f"Do you want to install '{module_name}' now? (y/n): ")
        if choice.lower() == "y":
            try:
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
                print(f"'{module_name}' has been successfully installed.")
            except Exception as e:
                print(f"Failed to install '{module_name}': {str(e)}")
        else:
            print(f"Please install '{module_name}' before running the script.")
        sys.exit(1)


# Check for required modules
check_module("requests")
check_module("urllib3")
check_module("socks")
check_module("stem")

# Rest of the script goes here...


import requests
import webbrowser
import logging
import urllib3
from urllib.parse import urljoin
from TsqliPAYLOADS import payloads

# Disable insecure request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(filename="tsqli.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to get user input URL
def get_target_url():
    while True:
        target_url = input("🔍 Enter the full vulnerable URL (e.g., https://example.com/?id=1): ")
        if target_url.startswith(("http://", "https://")):
            return target_url
        else:
            print("❌ Invalid URL! Please make sure to include http:// or https://")

# Function to perform injection and analyze response
def perform_injection(target_url):
    print("\n🚀 Performing SQL injection detection...")
    print("-----------------------------------------")

    positive_results = []

    for payload in payloads:
        complete_url = target_url.replace("1", payload)
        print(f"\n🔸 Testing payload: {payload}")

        try:
            response = requests.get(complete_url, verify=False)

            # Check for successful injection
            if response.status_code == 200 and "error" in response.text:
                positive_results.append(payload)
                print("✅ Injection successful!")
            else:
                print("❌ No injection detected.")

            # Additional response analysis
            content_type = response.headers.get("Content-Type")
            content_length = len(response.text)
            server_header = response.headers.get("Server")

            # Content-Type analysis
            if content_type and "text/html" not in content_type:
                print(f"⚠️ Unexpected Content-Type: {content_type}")

            # Content-Length analysis
            if content_length != len(requests.get(target_url, verify=False).text):
                print("⚠️ Different response size")

            # Server header analysis
            if server_header and "Apache" in server_header:
                print("⚠️ Server header indicates Apache")

            # Add more analysis techniques as needed

            print("-----------------------------------------")

        except requests.RequestException as e:
            print(f"❌ Error occurred: {str(e)}")
            print("-----------------------------------------")

        # Log the result
        logging.info(f"Payload: {payload} - Injection successful" if payload in positive_results else f"Payload: {payload} - No injection detected")

    # Save positive findings to an HTML file
    save_positive_findings(positive_results)

# Function to save positive findings to an HTML file
def save_positive_findings(positive_results):
    if not positive_results:
        print("\n📌 No positive findings.")
        return

    print("\n📌 Saving positive findings to HTML file...")

    html = """
    <html>
    <head>
        <title>Positive Findings</title>
        <style>
            body {
                background-color: #000;
                color: #0F0;
                font-family: monospace;
                font-size: 16px;
                padding: 20px;
            }
            h1 {
                text-align: center;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                margin-bottom: 10px;
            }
        </style>
    </head>
    <body>
        <h1>Positive Findings</h1>
        <ul>
    """

    for result in positive_results:
        html += f"            <li>{result}</li>\n"

    html += """
        </ul>
    </body>
    </html>
    """

    with open("positive_findings.html", "w") as file:
        file.write(html)

    print("✨ Positive findings saved to positive_findings.html")
    webbrowser.open("positive_findings.html")

# Main function
def main():
    print("✨ SQL Injection Detection Tool ✨")
    print("---------------------------------")
    print("")

    target_url = get_target_url()
    perform_injection(target_url)

if __name__ == "__main__":
    main()
