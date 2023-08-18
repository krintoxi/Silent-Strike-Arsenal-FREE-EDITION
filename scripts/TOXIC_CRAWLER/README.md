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
               \.       )---. )_.--; (   /'             ||=||
                \\     //|:: /--\:::\\\ //             _||= |
                 \\   ||::\:|----|:/:||/--.______,--==' \ - /
          -._     \`.  \\:|:|-- -|:\:/-.,,\\  .----'//'_.`-'
      \.     `-.   \ \ _|:|:|-- -|::||::\,,||-'////---' |/'
       \\       `._)\ / |\/:|-/|--\:/|. :\_,'---'       
        \\_      /,,\/:.'\\/-.'`-.-//  \ |
        /`\-    //,,,' |-.\-'\--/|-/ ./| |             
         /||-   ||, /| |\. |.-==-.| . /| |            
       \.=| `_/|-          |\`-| -/| `--------'
        \\` ./|-/-         |\`-| |-|Krintoxi________
         `--\ |=|'        _|\`-| |-|----'.-._ ..\`-.
             -|-|-     .-':`-;-| |./.-.-( | ||..|=-\\
             `'= /'   / ,--.:|-| ||_|_|_|_|-'__ .`-._)
              /|-|- .' /\ \ \|-` \\ ____,---'  `-. ..|
               /\=\/..'\ \_&gt;-'`-\ \'              \ .
               `,-':/\`.&gt;' |\/ \/\ \              `- 
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
             //;;'            TOX1C_CR@WL3R A C.I Toolkit Module! 
             `-'

# C.I Toolkit Module: TOX1C CR@WL3R

Welcome to the TOXIC_CRAWLER A C.I Toolkit Module! This module offers a versatile script designed to assist with reconnaissance tasks on target websites. Whether you're gathering information on common directories, searching for interesting files, checking subdomains, or more, this script aims to streamline the process.

## Features

- Access common directories on the target website.
- Search Google and DuckDuckGo for related URLs.
- Browse directories for interesting links.
- Search for files with various extensions.
- Check for subdomains using a wordlist.
- Check common ports for accessibility.

Let's delve into each phase of the C.I Toolkit Module TOXIC CRAWLER and understand what each one does:

### Phase 1: Accessing Common Directories
In this phase, the script attempts to access common directories on the target website. It uses a predefined wordlist (`common_wordlist.txt`) containing common directory names like "admin," "wp-admin," and "uploads." For each directory in the wordlist, it constructs a URL by appending the directory name to the base URL and sends a HEAD request to that URL. The script then prints whether the directory exists, returned a "404 Error," or encountered other HTTP status codes.

### Phase 2: Using Google Search Engine
In this phase, the script performs a Google search using the "site:" operator to look for URLs related to the target website. It fetches the search results, extracts the URLs, and processes each URL. If the URL's domain matches the target website's domain, the script processes it and prints whether the URL was found to be active.

### Phase 3: Checking DuckDuckGo
This phase is similar to Phase 2, but it uses the DuckDuckGo search engine instead of Google. The script searches for URLs related to the target website on DuckDuckGo and processes the extracted URLs, printing whether they were found to be active.

### Phase 4: Browsing Directories for Interesting Links
In this phase, the script starts browsing internal links found in the previous phases. It visits each internal link, extracts all links present on the page, and processes them. If a link is determined to be internal, the script processes it and adds it to the list of internal links. If a link is external, the script adds it to the list of external links. The script continues this process within a time limit of 15 minutes.

### Phase 5: Searching for Interesting Files
The script searches for interesting files on the target website using a predefined list of file extensions (`interesting_files`). For each filename in a wordlist (`wordlist.txt`), it constructs URLs by combining the base URL, the filename, and various file extensions. It then checks if these URLs exist and if they return valid content. If found, the script adds the URL to the list of all links.

### Phase 6: Checking Subdomains
In this phase, the script searches for subdomains using a wordlist (`sub_domain_wordlist.txt`). It constructs URLs by combining subdomain prefixes with the base URL and checks if these URLs exist. If found, the script adds the URL to the list of all links.

### Phase 7: Checking Ports
This phase checks common ports (e.g., 80, 443, 8080) on the target website. The script constructs URLs with port numbers and checks if they exist, printing the results for each port.

### Phase 8: Saving Results 
After all phases are completed, the script saves the captured terminal output to an TEXT file named `terminal_output.txt`. This file will contain all the printed information from the script's execution.

### User Interaction and Control
Throughout the execution, the script allows for user interaction. Pressing "Ctrl+C" will terminate the script and save the results. Additionally, the script provides the option to pause and resume execution by pressing "p" and cancel execution by pressing "c."

Please note that the script is meant for educational and ethical purposes only. Always ensure that you have explicit permission to perform any kind of reconnaissance or testing on target systems.

