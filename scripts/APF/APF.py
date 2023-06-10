import requests
from urllib.parse import urlparse, urljoin
from PATH import paths as light_paths
from DEEPPATH import paths as deep_paths


def normalize_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "http://" + url
    return url


def validate_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def check_admin_login(url, admin_login_url):
    full_url = urljoin(url, admin_login_url)
    if validate_url(full_url):
        return full_url


def find_admin_logins(target_domain, scan_type):
    if scan_type == "Light Scan":
        paths = light_paths
    elif scan_type == "Deep Scan":
        paths = deep_paths
    else:
        print("[-] Invalid scan type.")
        return []

    admin_logins = []
    total_paths = len(paths)
    print(f"\n\033[1m[+] Initiating {scan_type}...\033[0m")
    print(f"\033[1m[+] Target Domain:\033[0m {target_domain}")
    print(f"\033[1m[+] Total Paths to Check:\033[0m {total_paths}")
    print("\033[1m---------------------------------------------\033[0m")

    for index, path in enumerate(paths, 1):
        admin_login_url = urljoin(target_domain, path)
        print(f"\n\033[1m[+] Checking Path [{index}/{total_paths}]:\033[0m")
        print(f"    \033[93m{admin_login_url}\033[0m")
        result = check_admin_login(target_domain, admin_login_url)
        if result:
            admin_logins.append(result)

    return admin_logins


def main():
    # Prompt the user to enter the target domain
    print("\033[1m*************************")
    print(" C.I.T Admin Page Finder ")
    print("*************************\033[0m")
    target_domain = input("\033[1m[+] Enter the target domain:\033[0m ")

    # Normalize and validate the target domain URL
    target_domain = normalize_url(target_domain)
    if not validate_url(target_domain):
        print("[-] Invalid target domain.")
        return

    print("\n\033[1m[+] Scan Types:\033[0m")
    print("1. Light Scan")
    print("2. Deep Scan")
    scan_choice = input("\n\033[1m[+] Choose a scan type (enter the number):\033[0m ")

    if scan_choice == "1":
        scan_type = "Light Scan"
    elif scan_choice == "2":
        scan_type = "Deep Scan"
    else:
        print("[-] Invalid scan choice.")
        return

    print("\n\033[1m[+] Scanning target domain:\033[0m", target_domain)
    print("\033[1m[+] Scan Type:\033[0m", scan_type)
    print("\033[1m---------------------------------------------\033[0m")
    admin_logins = find_admin_logins(target_domain, scan_type)

    if admin_logins:
        print("\n\033[1m[+] Found", len(admin_logins), "admin login page(s):\033[0m\n")
        for index, login in enumerate(admin_logins, 1):
            print("\033[92m[+]\033[0m", login)
    else:
        print("\n\033[1m[-] No admin login pages found.\033[0m")


if __name__ == '__main__':
    main()
