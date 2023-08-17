Phase 1: Attempting to access common directories

In this phase, the script attempts to access common directories on the target website. These directories are specified in the common_directories list, such as /files, /data, and /uploads. The script sends HTTP HEAD requests to each directory URL and checks the response status codes to determine if the directory exists. The results are printed in the terminal, indicating whether each directory was found or not.

Phase 2: Browsing Directories

In this phase, the script explores the internal links found in the HTML content of the previously accessed common directories. It scrapes the links using BeautifulSoup and requests, and then processes these links. It checks if each link is internal to the base URL, and if so, it sends an HTTP GET request to the link. The resulting HTML content is parsed again to find more links. This process continues until either all internal links are explored or a timeout is reached. The results of each link exploration are printed in the terminal.

Phase 3: Using Google Search Engine

In this phase, the script uses the Google search engine to find URLs related to the target website. It constructs a search query using the site: operator and the base URL. It sends a request to Google, parses the search results using BeautifulSoup, and extracts URLs from the search results. The script processes each URL by sending an HTTP HEAD request to determine if the URL exists. The results are printed in the terminal.

Phase 4: Searching for Interesting Files

In this phase, the script searches for files with specific interesting extensions, such as .pdf, .txt, .mp3, etc., on the target website. It constructs URLs with these extensions appended to the base URL and sends HTTP HEAD requests to check if the files exist. If a file is found, its URL is added to the results.

Phase 5: Checking Subdomains

In this phase, the script checks for common subdomains like www, blog, shop, and admin. It constructs URLs with these subdomains and the base URL, sends HTTP HEAD requests, and checks the responses to determine if the subdomains exist.

Phase 6: Checking Ports

In this phase, the script checks for common ports (e.g., 80, 443, 8080) on the target website. It constructs URLs with these ports appended to the base URL, sends HTTP HEAD requests, and checks the responses to determine if the ports are open.

Phase 7: Saving Results to HTML

In this phase, the script combines all the collected results from previous phases (internal links, external links, Google links, DuckDuckGo links, interesting files, subdomains, and ports) into a single set. It then exports these results to an HTML report named CRAWLER_RESULTS.html. Additionally, the terminal output captured by the custom stream is saved to a text file named terminal_output.txt.

Each phase contributes to the overall goal of discovering information about the target website, such as its structure, linked content, relevant search engine results, and potentially interesting files. The script keeps the user informed by printing the progress and results of each phase in the terminal.