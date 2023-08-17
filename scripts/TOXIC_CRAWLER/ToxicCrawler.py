import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import signal
import random
import time
import sys
from contextlib import redirect_stdout
# Create a custom stream to capture terminal output
class TerminalCapture:
    def __init__(self):
        self.terminal = sys.stdout
        self.content = []

    def write(self, message):
        self.content.append(message)
        self.terminal.write(message)

    def flush(self):
        pass  # No need to flush in this case

# Use the custom stream to capture terminal output
capture_stream = TerminalCapture()
sys.stdout = capture_stream
# Global variable to store all links
all_links = set()
# Function to check if a URL exists
def url_exists(url):
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:
            return "Exists"
        elif response.status_code == 404:
            return "404 Error"
        else:
            return f"Status {response.status_code}"
    except requests.RequestException as e:
        return f"Request Exception: {str(e)}"

def search_for_interesting_files(base_url):
    interesting_files = [".pdf", ".txt", ".mp3", ".bin", ".zip", ".rar", ".tar.gz", ".tgz", ".gz", ".sql.gz", ".bak.gz", ".sql", ".mp4", ".jpeg", ".png"]
    found_files = set()

    for file_type in interesting_files:
        search_url = urljoin(base_url, file_type)  # Form complete URL
        if url_exists(search_url):
            response = requests.get(search_url)
            if response.status_code == 200 and response.content:  # Check status and non-empty content
                found_files.add(search_url)

    return found_files

# Function to check if a link is internal to the base URL
def is_internal_link(link, base_url):
    absolute_link = urljoin(base_url, link)
    return absolute_link.startswith(base_url)
# Function to scrape links from a page using a random user agent
def scrape_links(url):
    links = set()
    try:
        headers = {'User-Agent': get_random_user_agent()}
        response = requests.get(url, headers=headers)
        print("Using Random User Agent:", headers['User-Agent'])  # Print the chosen user agent
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a", href=True):
                links.add(link.get("href"))
        return links
    except requests.RequestException:
        return links

# Function to search Google for URLs related to the target
def search_google(target_url, num_results=1000):
    query = f'site:{target_url}'
    search_url = f'https://www.google.com/search?q={query}'
    try:
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = []
            for link in soup.find_all("a", href=True):
                url = link.get("href")
                match = re.match(r'^/url\?q=(.*?)&', url)
                if match:
                    decoded_url = match.group(1)
                    if decoded_url.startswith("http"):
                        results.append(decoded_url)
                if len(results) >= num_results:
                    break
            return results
        else:
            return []
    except requests.RequestException:
        return []
# Function to process a URL and return the result
def process_url(url):
    result = "Not Found"
    if url_exists(url):
        result = "Found Active"
    return result, url
# Function to get a random user agent
def get_random_user_agent():
    return random.choice(USER_AGENTS)
# Function to handle Ctrl+C and save results before exiting
def handle_interrupt(signum, frame):
    print("\nCtrl+C detected. results   NOT SAVED  exiting...")

def search_for_ports(base_url):
    ports = [80, 443, 8080, 8000, 8081]  # Add more ports if needed
    port_links = set()

    for port in ports:
        port_url = urljoin(base_url, f":{port}")
        result, _ = process_url(port_url)
        port_links.add((port_url, result))
        print(f"Port: {port_url} - Result: {result}")

def search_for_subdomains(base_url):
    subdomains = ["www", "blog", "shop", "admin"]  # Add more subdomains if needed
    subdomain_links = set()

    for subdomain in subdomains:
        subdomain_url = urljoin(base_url, f"http://{subdomain}.{base_url}")
        result, _ = process_url(subdomain_url)
        subdomain_links.add((subdomain_url, result))
        print(f"Subdomain: {subdomain_url} - Result: {result}")

    return subdomain_links
# Function to search DuckDuckGo for URLs related to the target
def search_duckduckgo(target_url, num_results=10):
    query = f'site:{target_url}'
    api_url = f'https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1'
    response = requests.get(api_url)
    data = response.json()
    results = data.get('Results', [])[:num_results]
    return [result['FirstURL'] for result in results]


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1234.567 Safari",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.12345.678",
]

# Main Execution
def main():
    global all_links  # Declare all_links as a global variable
    # Set up the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)
    print("******************************************************************")
    print("Press Ctrl+C at any time to terminate the script and save results.")
    print("******************************************************************")
    base_url_input = input("Enter the base URL of the target website (e.g., example.com): ").strip()

    # Add "http://" or "https://" if missing
    if not base_url_input.startswith("http://") and not base_url_input.startswith("https://"):
        base_url = "http://" + base_url_input
    else:
        base_url = base_url_input
    internal_links = set()
    external_links = set()
    google_links = set()
    duckduckgo_links = set()
    subdomain_links = set()
    port_links = set()

    print("*******************************************************")
    print("[*] Phase 1: Attempting to access common directories...")
    print("*******************************************************")
    # Phase 1: Attempting to access common directories
    common_directories = ["/files", "/data", "/uploads"]  # Add more if needed
    for directory in common_directories:
        directory_url = urljoin(base_url, directory)
        result, _ = process_url(directory_url)
        internal_links.add((directory_url, result))
        print(f"Directory: {directory_url} - Result: {result}")

    print("************************************")
    print("[*] Phase 2: Browsing Directories...")
    print("************************************")
    phase_2_start_time = time.time()  # Record the start time of Phase 2
    phase_2_timeout = 15  # 10 minutes in seconds (10 * 60)

    while internal_links and time.time() - phase_2_start_time < phase_2_timeout:
        link, _ = internal_links.pop()
        page_links = scrape_links(link)
        for page_link in page_links:
            full_link = urljoin(base_url, page_link)
            if is_internal_link(full_link, base_url):
                if full_link not in internal_links and full_link not in external_links:
                    result, _ = process_url(full_link)
                    internal_links.add((full_link, result))
                    print(f"Link: {full_link} - Result: {result}")
            else:
                if full_link not in external_links:
                    external_links.add((full_link, "External"))
                    print(f"Possibly External Link of Interest: {full_link}")
    else:
        print("Phase 2 timed out. Proceeding to Phase 3.")

    print("******************************************")
    print("[*] Phase 3: Using Google Search Engine...")
    print("******************************************")
    google_results = search_google(base_url, num_results=1000)
    for link in google_results:
        print(f"Google Link: {link}")  # Print the link being processed
        match = re.match(r'^https?://(.*?)/', link)
        if match:
            domain = match.group(1)
            if domain == base_url:
                if link not in internal_links:
                    result, _ = process_url(link)
                    internal_links.add((link, result))
                    print(f"Google Link: {link} - Result: {result}")
                google_links.add(link)

    print("******************************************")
    print("[*] Phase 4: Checking DuckDuckGo...")
    print("******************************************")

    def search_duckduckgo(query, num_results=10):
        results = []
        search_url = f"https://duckduckgo.com/html/?q={query}&t=h_&iar=web"
        try:
            response = requests.get(search_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                links = soup.find_all("a", class_="result__url")
                for link in links:
                    url = link.get("href")
                    results.append(url)
                    if len(results) >= num_results:
                        break
            return results
        except requests.RequestException:
            return []

    # Combine all the links into a single set
    all_links = internal_links | external_links | google_links | set(duckduckgo_links)

    domain = base_url_input
    print("***********************************************")
    print("[*] Phase 4: Searching for Interesting Files...")
    print("***********************************************")
    print("This Will Take a Maximum of 5 minutes BE PATIENT.")
    interesting_files = search_for_interesting_files(base_url)
    for file_url in interesting_files:
        print(f"Interesting File Found!: {file_url}")
        all_links.add((file_url, "Interesting File"))
        all_links = internal_links | external_links | google_links | set(duckduckgo_links)

    print("******************************************")
    print("[*] Phase 5: Checking Subdomains...")
    print("******************************************")
    subdomain_links = search_for_subdomains(base_url)

    print("******************************************")
    print("[*] Phase 5: Checking Ports...")
    print("******************************************")
    port_links = search_for_ports(base_url)

    print("**************************************")
    print("[*] Phase 5: Saving Results to HTML...")
    print("**************************************")
    with open('terminal_output.txt', 'w') as f:
        f.writelines(capture_stream.content)
    # Combine all the links into a single set
    all_links = internal_links | external_links | google_links | set(duckduckgo_links)
if __name__ == "__main__":
    main()