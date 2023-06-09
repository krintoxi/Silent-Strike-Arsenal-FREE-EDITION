# TsqliPAYLOADS.py

payloads = []

# Read payloads from the file
with open("payloads.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            payloads.append(line)

# Export the payloads list for other scripts to use
def get_payloads():
    return payloads
