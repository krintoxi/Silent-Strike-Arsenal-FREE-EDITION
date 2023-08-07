
---

# T-SQL Injection (TSQLI) Detection Tool

This repository contains a Python-based SQL injection detection tool (`TSQLI.py`) designed for private security firms and internal use. The tool checks for potential SQL injection vulnerabilities in a given URL and provides an automated way to perform SQL injection testing. The tool uses a set of predefined SQL injection payloads to test the target website.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Payloads](#payloads)


## Introduction

SQL injection is a critical web application vulnerability that can lead to unauthorized access, data breaches, and other security risks. The T-SQL Injection (TSQLI) Detection Tool helps security firms and internal security teams identify and mitigate potential SQL injection vulnerabilities.

## Getting Started

1. Clone or download this repository to your local machine:

```bash
git clone https://github.com/krintoxi/C.I.T.git
cd C.I.T
```

2. Ensure you have Python (version 3.x) installed on your system.

3. Install the required Python modules using the following command:

```bash
pip install requests beautifulsoup4
```

4. **Optional**: If you want to update the `payloads.txt` file with fresh payloads from an external source, you can run the `Payloadimport.py` script as follows:

```bash
python Payloadimport.py
```

## Usage

The primary tool for SQL injection detection is `TSQLI.py`. To use it, follow these steps:

1. Make sure you have the `payloads.txt` file with a list of SQL injection payloads. If you ran `Payloadimport.py`, this file should already be populated.

2. Execute the `TSQLI.py` script:

```bash
python TSQLI.py
```

3. The script will prompt you to enter the full vulnerable URL, including the injection point (e.g., `https://example.com/?id=1`).

4. The tool will then perform SQL injection testing using the payloads from `payloads.txt` and display the results.

5. If positive findings are detected, they will be saved to an HTML file named `positive_findings.html`, and the file will open in your default web browser.

**Note:** Always ensure you have permission to test the target website for vulnerabilities, and use this tool responsibly within your organization.

## Payloads

The `payloads.txt` file contains a list of SQL injection payloads used by the tool for testing. The payloads are essential inputs that simulate various SQL injection attempts on the target website. The file is already populated with a set of predefined payloads, which you can find in the `scripts/TSQLI/payloads.txt` file.

### Updating Payloads (Optional)

If you need to update the payloads, you can run the `Payloadimport.py` script. This script fetches payloads from an external URL and saves them to the `payloads.txt` file.

#### Payloadimport.py

The `Payloadimport.py` script is optional and designed to fetch SQL injection payloads from an external URL. Here's how it works:

1. The script sends a GET request to the specified URL, which points to a GitHub repository containing a list of SQL injection payloads.

2. It scrapes the payloads from the HTML content using the BeautifulSoup library and extracts the payloads from code blocks in the repository's README.md file.

3. The extracted payloads are saved to the `payloads.txt` file in the `scripts/TSQLI/` directory.

4. You can then use the `TsqliPAYLOADS.py` script to read and utilize these payloads in the primary detection tool (`TSQLI.py`).

**Note:** If you do not wish to update the payloads from an external source, you can use the existing `payloads.txt` file, and the `TsqliPAYLOADS.py` script will work as intended.

### TsqliPAYLOADS.py

The `TsqliPAYLOADS.py` script plays a critical role in the SQL injection detection process. It reads the SQL injection payloads from the `payloads.txt` file and stores them in a Python list.

The script follows these steps:

1. It initializes an empty list called `payloads` to store the SQL injection payloads.

2. The script reads the payloads from the `scripts/TSQLI/payloads.txt` file and appends each payload to the `payloads` list.

3. It defines a function named `get_payloads()` that allows other scripts, like `TSQLI.py`, to access the list of payloads.

By using the `get_payloads()` function, `TSQLI.py` can access and utilize the payloads for SQL injection testing. This separation of concerns helps organize the code and ensures that the payloads are managed and accessed efficiently.

## Contributing

Contributions to this project are not accepted due to its private and sensitive nature. As an internal security tool, it is crucial to maintain the confidentiality and integrity of the code.

## License

This project is licensed under a private license, and all rights are reserved by the owners. Redistribution or use of the code without explicit permission is strictly prohibited.

---

We hope this T-SQL Injection (TSQLI) Detection Tool helps strengthen your security efforts and enhances your ability to identify and mitigate SQL injection vulnerabilities. Remember to use this tool responsibly and in accordance with your organization's security policies. If you have any questions or need assistance, please refer to your internal security team or relevant experts within your organization.
InterCuba.Net