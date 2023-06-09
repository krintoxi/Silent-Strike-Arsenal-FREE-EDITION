import requests
from bs4 import BeautifulSoup

url = "https://github.com/payloadbox/sql-injection-payload-list/blob/master/README.md"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section with payloads
    section = soup.find("article", class_="markdown-body")

    if section:
        # Find all the code blocks within the section
        code_blocks = section.find_all("code")

        if code_blocks:
            payloads = []

            # Extract the payload text from each code block
            for code_block in code_blocks:
                payload = code_block.get_text().strip()
                payloads.append(payload)

            # Save the payloads to a text file
            with open("payloads.txt", "w") as file:
                for payload in payloads:
                    file.write(payload + "\n")

            print("Payloads extracted and saved to 'payloads.txt' file.")
        else:
            print("No payloads found on the page.")
    else:
        print("Payloads section not found on the page.")
else:
    print("Failed to retrieve the payloads list.")

