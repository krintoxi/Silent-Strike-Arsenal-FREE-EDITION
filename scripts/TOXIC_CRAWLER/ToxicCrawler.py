import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import signal
import random
import time
import sys
from urllib.parse import unquote
import threading
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


def switch_user_agents():
    global current_user_agent
    while True:
        time.sleep(120)  # Wait for 2 minutes
        current_user_agent = get_random_user_agent()
        print("Switched to new user agent:", current_user_agent)

def read_word_list(file_path):
    with open(file_path, "r") as file:
        word_list = [line.strip() for line in file]
    return word_list

def search_for_interesting_files(base_url, word_list_path, interesting_files):
    word_list = read_word_list(word_list_path)
    found_files = set()

    print("Searching for interesting files on:", base_url)
    for filename in word_list:
        for extension in interesting_files:
            file_url = urljoin(base_url, f"{filename}{extension}")
            print("Checking for:", file_url)
            if url_exists(file_url):
                response = requests.get(file_url)
                if response.status_code == 200 and response.content:
                    found_files.add(file_url)
                    print("Found:", file_url)
                else:
                    print("File not found:", file_url)
            else:
                print("URL does not exist:", file_url)

    return found_files

def execute_phase(phase_function, *args):
    start_time = time.time()
    phase_timeout = 5 * 60  # 5 minutes in seconds

    phase_function(*args)  # Execute the phase function

    elapsed_time = time.time() - start_time
    if elapsed_time >= phase_timeout:
        print(f"Phase timed out after {elapsed_time:.2f} seconds. Moving to the next phase.")


# Function to check if a link is internal to the base URL
def is_internal_link(link, base_url):
    absolute_link = urljoin(base_url, link)
    return absolute_link.startswith(base_url)
# Function to scrape links from a page using a random user agent
def scrape_links(url):
    links = set()

    try:
        print("Scraping links from:", url)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a", href=True):
                links.add(link.get("href"))
            print("Found", len(links), "links on the page.")
        else:
            print("Failed to retrieve page with status code:", response.status_code)

    except requests.RequestException as e:
        print("An error occurred:", e)

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

def search_for_subdomains(base_url, sub_domain_wordlist_path):
    sub_domain_word_list = read_word_list(sub_domain_wordlist_path)
    subdomain_links = set()

    for subdomain in sub_domain_word_list:
        subdomain_url = urljoin(base_url, f"http://{subdomain}.{base_url}")
        result, _ = process_url(subdomain_url)
        subdomain_links.add((subdomain_url, result))
        print(f"Subdomain: {subdomain_url} - Result: {result}")

    return subdomain_links

# Function to search DuckDuckGo for URLs related to the targe
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
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

    return results

# Global variable to control script execution
pause_execution = False
cancel_execution = False

# Function to pause and resume execution
def toggle_execution():
    global pause_execution
    pause_execution = not pause_execution

# Function to cancel execution
def cancel_execution_handler():
    global cancel_execution
    cancel_execution = True

def user_interaction_thread():
    while True:
        print("\nPress 'p' to pause/resume, 'c' to cancel, or any other key to continue...")
        user_input = input().strip().lower()

        if user_input == 'p':
            toggle_execution()
        elif user_input == 'c':
            cancel_execution_handler()

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1234.567 Safari",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/100.0.12345.678",
]
current_user_agent = random.choice(USER_AGENTS)
# Main Execution
user_agent_thread = threading.Thread(target=switch_user_agents)
user_agent_thread.daemon = True  # The thread will exit when the main thread exits
user_agent_thread.start()

common_wordlist_path = "common_wordlist.txt"  # Path to your common_wordlist.txt file
sub_domain_wordlist_path ="sub_domain_wordlist.txt"
wordlist = "wordlist.txt"
def main():
    global common_wordlist_path
    global wordlist
    global all_links  # Declare all_links as a global variable
    # Set up the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, handle_interrupt)
    ascii_art = """
                                                               / /
                                                        | | |  /
                                                         \|_|_/
                                                       ,--/.__/--'
                       _.-/   _   \-._                    .'|
                     .'::(_,-' `-._)::`.                  |:|
                    (:::::::::::::::::::)                .':|
                     \_:::;;;::::;;;:::/    /            |::|
             \        ,---'..\::/..`-.'    /             |::|
              \       \_;:....|'...:_ )   /             .'=||
               \.       )---. )_.--&lt; (   /'             ||=||
                \\     //|:: /--\:::\\\ //             _||= |
                 \\   ||::\:|----|:/:||/--.______,--==' \ - /
          -._     \`.  \\:|:|-- -|:\:/-.,,\\  .----'//'_.`-'
      \.     `-.   \ \ _|:|:|-- -|::||::\,,||-'////---' |/'
       \\       `._)\ / |\/:|-/|--\:/|. :\_,'---'       /
        \\_      /,,\/:.'\\/-.'`-.-//  \ |
        /`\-    //,,,' |-.\-'\--/|-/ ./| |             /
         /||-   ||, /| |\. |.-==-.| . /| |            | /
 __  |    /||-  ||,,\- | .  \;;;;/ .  .':/         _,-=/-'
/  \//    /||-  ' `,-|::\ . \,..,/   /: /         /.-'
,--||      /||-/.-.'  \  `._ `--' _.' .'|        //
.--||`.    /||//\ '   |-'.___`___' _,'|//       /;
  /\| \     ///\ /     \\_`-.`--`-'_==|'       /;'
 / |'\ \.   //\ /       \_\__)\`==-_'_|       / /
  .'  \.=`./|\ /          \`-- \--._/_/------( /
       \.=| `_/|-          |\`-| -/| `--------'
        \\` ./|-/-         |\`-| |-|     ________
         `--\ |=|'        _|\`-| |-|----'.-._ ..\`-.
             -|-|-     .-':`-;-| |./.-.-( | ||..|=-\\
             `'= /'   / ,--.:|-| ||_|_|_|_|-'__ .`-._)
              /|-|- .' /\ \ \|-` \\ ____,---'  `-. ..|
               /\=\/..'\ \_&gt;-'`-\ \'              \ .|
               `,-':/\`.&gt;' |\/ \/\ \              `- |
               //::/\ \/_/|-' \/| \ `.            / ||
              / (:|\ \/) \ \|.'-'  `-\\          |;:|\_
             || |:`-/:.'-|-' \|       \\          `;_\-`-._
             \\=/:_/::/\| \|          |\\            `-._ =`-._
              \_)' |:|                | //               `--.__`-.
                   |:|                                         )\|
                   /;/                                         / (\_
                  / /                                         |\\;;_`-.
                _/ /                                          ' `---\.-\
               /::||
              /:::/
             //;;'             
             `-'

  **********  ****  **     **  **    ******      ******  *******    ****  **       ** **        ****  *******  
/////**///  *///**//**   **  ***   **////**    **////**/**////**  */// */**      /**/**       */// */**////** 
    /**    /*  */* //** **  //**  **    //    **    // /**   /** /* **/*/**   *  /**/**      /    /*/**   /** 
    /**    /* * /*  //***    /** /**         /**       /*******  /*/* /*/**  *** /**/**         *** /*******  
    /**    /**  /*   **/**   /** /**         /**       /**///**  /*/ ** /** **/**/**/**        /// */**///**  
    /**    /*   /*  ** //**  /** //**    **  //**    **/**  //** /* //  /**** //****/**       *   /*/**  //** 
    /**    / ****  **   //** **** //******    //****** /**   //**/ *****/**/   ///**/********/ **** /**   //**
    //      ////  //     // ////   //////      //////  //     //  ///// //       // ////////  ////  //     // 

                                C.I Toolkit Module
        """


    print(ascii_art)
    print("******************************************************************")
    print("Press Ctrl+C at any time to terminate the script and save results.")
    print("******************************************************************")
    headers = {'User-Agent': get_random_user_agent()}
    print("Using Random User Agent:", headers['User-Agent'])
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
    # Execute each phase with a time limit of 5 minutes

    print("*******************************************************")
    print("[*] Phase 1: Attempting to access common directories...")
    print("*******************************************************")
    user_agent_thread = threading.Thread(target=switch_user_agents)
    user_agent_thread.daemon = True  # The thread will exit when the main thread exits
    user_agent_thread.start()
    common_wordlist_path = "common_wordlist.txt"  # Path to your common_wordlist.txt file
    common_directories = read_word_list(common_wordlist_path)
    for directory in common_directories:
        directory_url = urljoin(base_url, directory)
        result, _ = process_url(directory_url)
        internal_links.add((directory_url, result))
        print(f"Directory: {directory_url} - Result: {result}")

    print("******************************************")
    print("[*] Phase 2: Using Google Search Engine...")
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
    print("[*] Phase 3: Checking DuckDuckGo...")
    print("******************************************")
    duckduckgo_results = search_duckduckgo(base_url, num_results=1000)
    for link in duckduckgo_results:
        decoded_link = unquote(link.replace('//duckduckgo.com/l/?uddg=', ''))
        print(f"DuckDuckGo Decoded Link: {decoded_link}")  # Print the decoded link being processed
        match = re.match(r'^https?://(.*?)/', decoded_link)
        if match:
            domain = match.group(1)
            if domain == base_url:
                if decoded_link not in internal_links:
                    result, _ = process_url(decoded_link)
                    internal_links.add((decoded_link, result))
                    print(f"DuckDuckGo Link: {decoded_link} - Result: {result}")
                duckduckgo_links.add(decoded_link)

    print("**********************************************************")
    print("[*] Phase 3: Browsing Directories For interesting LINKS...")
    print("**********************************************************")
    phase_2_start_time = time.time()  # Record the start time of Phase 2
    phase_2_timeout = 15  # 15 minutes in seconds

    while internal_links and time.time() - phase_2_start_time < phase_2_timeout:
        link, _ = internal_links.pop()
        page_links = scrape_links(link)  # Only pass the link as an argument
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
        print("Phase 3 timed out. Proceeding to Phase 4.")

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
        print("Phase 3 timed out. Proceeding to Phase 4.")

    print("***********************************************")
    print("[*] Phase 4: Searching for Interesting Files...")
    print("***********************************************")
    print("This Will Take a Maximum of 5 minutes BE PATIENT.")
    word_list_path = "wordlist.txt"  # Path to your wordlist.txt file
    interesting_files = [".pdf", ".txt", ".mp3", ".bin", ".zip", ".rar", ".tar.gz", ".tgz", ".gz", ".sql.gz", ".bak.gz",
                         ".sql", ".mp4", ".jpeg", ".png"]
    interesting_files_result = search_for_interesting_files(base_url, word_list_path, interesting_files)
    all_links |= interesting_files_result

    print("******************************************")
    print("[*] Phase 5: Checking Subdomains...")
    print("******************************************")
    sub_domain_wordlist_path = "sub_domain_wordlist.txt"  # Path to your sub_domain_wordlist.txt file
    subdomain_links_result = search_for_subdomains(base_url, sub_domain_wordlist_path)
    all_links |= subdomain_links_result

    print("******************************************")
    print("[*] Phase 6: Checking Ports...")
    print("******************************************")
    port_links = search_for_ports(base_url)

    print("**************************************")
    print("[*] Phase 8: Saving Results to HTML...")
    print("**************************************")
    with open('terminal_output.txt', 'w') as f:
        f.writelines(capture_stream.content)
    # Combine all the links into a single set
    all_links = internal_links | external_links | google_links | set(duckduckgo_links)
if __name__ == "__main__":
    main()