import requests
from urllib.parse import urljoin
from TsqliPAYLOADS import payloads

# Input parameters
target_url = input("Enter the target URL: ")
target_param = input("Enter the target parameter: ")

# Construct the complete URL
complete_url = urljoin(target_url, target_param)

# Perform injection
for payload in payloads:
    # Prepare the payload
    params = {target_param: payload}

    try:
        # Send the request
        response = requests.get(complete_url, params=params)

        # Check for successful injection
        if "error" in response.text:
            print(f"Payload: {payload} - Injection successful!")
        else:
            print(f"Payload: {payload} - No injection detected.")
    except requests.RequestException as e:
        print(f"Payload: {payload} - Error occurred: {str(e)}")
