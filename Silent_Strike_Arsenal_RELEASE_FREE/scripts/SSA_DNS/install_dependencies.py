import subprocess
print("""
░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
░░░░░░▐▌░░░░▀▀███████▀
▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒""")
# Install nmap using pip
subprocess.call(["pip", "install", "tqdm"])

# Install other required packages using pip
required_packages = [
    "python-whois",
    "requests",
    "tqdm",
]

for package in required_packages:
    subprocess.call(["pip", "install", package])
print("""     
                       (\.-./)
                       /     \
                     .'   :   '.
                _.-'`     '     `'-._
             .-'          :          '-.
           ,'_.._         .         _.._',
           '`    `'-.     '     .-'`    `'
                     '.   :   .'
                       \_. ._/
                 \       |^|InterCuba.Net
                  |      | ;
                  \'.___.' /
                   '-....-'  """)
print("✅ Dependencies installed successfully.")
