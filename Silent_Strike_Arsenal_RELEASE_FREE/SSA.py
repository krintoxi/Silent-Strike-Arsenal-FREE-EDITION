import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
import subprocess
import requests
import re
import uuid
import socket
import platform
import random
# Function to get the public IP address
def get_public_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except requests.RequestException:
        return "IP Unavailable"
# Function to get the MAC address
def get_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(re.findall('..', mac_num))
    return mac

# Create a function to update IP and MAC information
def update_network_info():
    ip_info_label.config(text=f"IP: {get_public_ip()}\nMAC: {get_mac_address()}")

# Simple tooltip class
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background='black', foreground='red', relief='solid', borderwidth=1,
                         font=('Arial', 10, 'bold'),  # Increase font size as needed
                         wraplength=200)  # Adjust wrap length as needed
        label.pack(ipadx=1, ipady=1)

    def close(self, event=None):
        if self.tw:
            self.tw.destroy()


# Placeholder functions for each script
# Placeholder functions for each script
def script_panel():
    print("Running PANEL")
    os.system("python3 scripts/SSA_PANEL/setup.py")
    os.system("gnome-terminal -- python3 scripts/SSA_PANEL/Panel.py")

def script_vulnerability_scan():
    print("Running Vulnerability Scan")
    os.system("gnome-terminal -- python3 scripts/SSA_NVulScan/vulscan.py")

def script_admin_page_finder():
    print("Running Admin Page Finder")
    os.system("gnome-terminal -- python3 scripts/SSA_APF/APF.py")

def script_ddos():
    print("Running DDOS")
    os.system("gnome-terminal -- python3 scripts/SSA_DDOS/ddos.py")

def script_dns_info():
    print("Running DNS INFO")
    os.system("python3 scripts/SSA_DNS/install_dependencies.py")
    os.system("gnome-terminal -- python3 scripts/SSA_DNS/dns.py")

def script_hash_cracker():
    print("Running HASH CRACKER")
    os.system("python3 scripts/SSA_HASH_CRACKER/install_required_packages.py")
    os.system("gnome-terminal -- python3 scripts/SSA_HASH_CRACKER/SSA_HASH_CRACK.py")

def script_hashid():
    print("Running HASHID")
    os.system("gnome-terminal -- python3 scripts/SSA_HashID/HID.py")

def script_mac_spoof():
    print("Running MAC SPOOF")
    os.system("gnome-terminal -- python3 scripts/SSA_MACSPOOF/macspoof.py")

def script_phptools():
    print("Running PHPTOOLS")
    os.system("gnome-terminal -- python3 scripts/SSA_PHPTOOLS/phptools.py")

def script_setinel2att():
    print("Running SETINEL2ATT")
    os.system("python3 scripts/SSA_SENTINEL2ATT/install_requirements.py")
    os.system("gnome-terminal -- python3 scripts/SSA_SENTINEL2ATT/Sentinel2Attack.py")

def script_spider():
    print("Running SPIDER")
    os.system("gnome-terminal -- python3 scripts/SSA_Spider/SpiderGUI.py")

def script_sqli_m():
    print("Running SQLI_M")
    os.system("gnome-terminal -- python3 scripts/SSA_SQLI_M/sqli.py")

def script_t_cipher():
    print("Running T-CIPHER")
    os.system("python3 scripts/SSA_TCipher/install_requirements.py")
    os.system("gnome-terminal -- python3 scripts/SSA_TCipher/T-Cipher.py")

def script_exif_pwn():
    print("| S.S.A_MetaDive Fotográfico |")
    os.system("gnome-terminal -- python3 scripts/SSA_EXIF/exifpwn.py")

def script_hex_converter():
    print("| S.S.A_Hex-Converter |")
    os.system("gnome-terminal -- python3 scripts/SSA_HEX_CONVERTER/hexconverter.py")

def script_binary_converter():
    print("| S.S.A_Binary-Converter |")
    os.system("gnome-terminal -- python3 scripts/SSA_BINARY_CONVERTER/binaryconverter.py")

def script_open_shells():
    print("| S.S.A_Shell Extractor |")
    os.system("gnome-terminal -- python3 tools/SHELLS/extract.py")

def script_tele_grab():
    print("| S.S.A_Telegram Grabber |")
    os.system("gnome-terminal -- python3 scripts/SSA_TELEGRAM/SSA_T.py")

# Function to open a hyperlink
def open_link(url):
    try:
        webbrowser.open(url, new=2)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open URL: {e}")

# Function to validate the password
def validate_password():
    entered_password = password_entry.get()
    if entered_password == "FREECUBA":
        # Hide the password input widgets
        password_label.grid_forget()
        password_entry.grid_forget()
        submit_button.grid_forget()

        # Show authentication message
        auth_message_label.config(text="You are now Authenticated")
        auth_message_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Enable the first four script buttons
        for widget in script_buttons[:9]:  # Only the first four script buttons should be enabled
            widget['state'] = 'normal'

        # Keep the rest disabled and show tooltip prompting upgrade
        upgrade_message = "Upgrade to the full edition to unlock this feature."
        for button in script_buttons[9:]:  # Apply this to buttons from the fifth onwards
            button['state'] = 'disabled'
            CreateToolTip(button, upgrade_message)
            CreateToolTip(command_entry1, upgrade_message)
            CreateToolTip(command_entry2, upgrade_message)
            CreateToolTip(command_entry3, upgrade_message)
    else:
        messagebox.showerror("Error", "Incorrect password.")


# Function to run multiple Linux commands in new GNOME terminals
def run_multiple_commands():
    commands = [command_entry1.get(), command_entry2.get(), command_entry3.get()]
    for cmd in commands:
        if cmd.strip():
            full_cmd = f"{cmd}; exec bash"
            try:
                subprocess.Popen(["gnome-terminal", "--", "bash", "-c", full_cmd])
            except Exception as e:
                messagebox.showerror("Error", f"Failed to execute command: {e}")

# Function to get detailed public IP information
def get_detailed_ip_info():
    try:
        response = requests.get('http://ipinfo.io/json')
        data = response.json()
        ip_info = f"The Public IP of your device: {data['ip']}\nCity you are in: {data['city']}\nRegion you are in: {data['region']}\n Country you are in: {data['country']}\nYour Service Provider: {data['org']}"
        return ip_info
    except requests.RequestException:
        return "IP Info Unavailable"

# Function to get local IP and hostname
def get_local_network_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return f"Your Device Name: {hostname}"

# Function to update network information
# Function to get MAC Address
def get_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = ':'.join(re.findall('..', mac_num))
    return f"Your Device MAC Address:\n {mac}"

# Function to update network information
def update_network_info():
    detailed_ip_info = get_detailed_ip_info()
    local_network_info = get_local_network_info()
    mac_address = get_mac_address()
    network_info_label.config(text=f"{detailed_ip_info}")
# Create the main window
root = tk.Tk()
root.title("Silent Strike Arsenal")
root.configure(bg='#000')
# Configure root grid (all rows and columns should be given a weight)
for i in range(8):  # Assuming 8 is the maximum grid row number used
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # Assuming 4 is the maximum grid column number used
    root.grid_columnconfigure(i, weight=1)
# Set the window icon
try:
    icon_image = PhotoImage(file="scripts/SSA_PANEL/logos/Logo.png")
    root.iconphoto(True, icon_image)
except Exception as e:
    print(f"Error setting icon: {e}")

# Load and display the logo
# List of logo file names
logos = ["Logo.png", "Logo2.png", "Logo3.png","Logo4.png","Logo5.png","Logo6.png","Logo7.png"]

# Pick a random logo
selected_logo = random.choice(logos)

# Load and display the logo
try:
    logo_path = f"scripts/SSA_PANEL/logos/{selected_logo}"
    logo_image = ImageTk.PhotoImage(Image.open(logo_path))
    logo_label = tk.Label(root, image=logo_image, bg='#000')
    logo_label.grid(row=0, column=0, columnspan=4)
except FileNotFoundError:
    print("Logo file not found. Please check the path.")
except Exception as e:
    print(f"Error loading logo image: {e}")

# Create frames for better organization
auth_frame = tk.Frame(root, bg='#000')
auth_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
# Configure the auth_frame grid
auth_frame.grid_columnconfigure(0, weight=1)
auth_frame.grid_columnconfigure(1, weight=1)
auth_frame.grid_columnconfigure(2, weight=1)
auth_frame.grid_columnconfigure(3, weight=1)

main_frame = tk.Frame(root, bg='#000')
main_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Command entry fields and "Run All" button setup in command_frame
command_frame = tk.Frame(root, bg='#000')
command_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

# Configure the command_frame grid
command_frame.grid_columnconfigure(0, weight=1)
command_frame.grid_columnconfigure(1, weight=1)
command_frame.grid_columnconfigure(2, weight=1)
command_frame.grid_columnconfigure(3, weight=1)

footer_frame = tk.Frame(root, bg='#000')
footer_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

# Authentication widgets setup in auth_frame
# Improved "Enter Password" Text Label
password_label = tk.Label(auth_frame, text="Enter Password:", fg='white', bg='#000',
                          font=('Helvetica', 12, 'bold'), borderwidth=2, relief="groove")
password_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Password entry
# Improved Password Entry
password_entry = tk.Entry(auth_frame, show='*', width=25, font=('Helvetica', 10), borderwidth=1, relief="groove", fg='RED', bg='black')
password_entry.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Submit button
# Improved Submit Button
submit_button = tk.Button(auth_frame, text="Authenticate", command=validate_password,
                          bg='black', fg='green', font=('Helvetica', 12, 'bold'), 
                          borderwidth=2, relief="raised")
submit_button.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

# Improved Authentication Message Label
auth_message_label = tk.Label(auth_frame, text="", bg='#000', fg='lightblue', 
                              font=('Helvetica', 12, 'bold'))
auth_message_label.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

# Script buttons creation in main_frame
# Styling the buttons
button_style = {
    'bg': '#333333', 'fg': 'white', 'font': ('Courier New', 10, 'bold'),
    'activebackground': 'black', 'activeforeground': 'red',
    'relief': 'raised', 'bd': 1
}

# Creating and disabling script buttons
script_functions = [
    script_panel, script_vulnerability_scan, script_admin_page_finder, script_ddos, script_dns_info,
    script_hash_cracker, script_hashid, script_mac_spoof, script_t_cipher, script_sqli_m,
    script_spider,script_tele_grab, script_exif_pwn, script_hex_converter, script_binary_converter, script_open_shells, script_setinel2att, script_phptools
]
script_names = [
    "S.S.A AGENT PANEL", "S.S.A Web Vulnerability Scanner", "S.S.A Admin Page Finder", "S.S.A Denial Of Service", "S.S.A DNS Intelligence Report", 
    "S.S.A MULTI HASH CRACKER", "S.S.A Hash Identifier", "S.S.A MAC Address Spoofer ", "S.S.A T-CIPHER (Cryptography)", "S.S.A SQLi Scanner/Exploiter",
    "S.S.A SPIDER (OSINT)","Tele Grab (Telegram)", "S.S.A_MetaDive (Metadata)", "S.S.A_HEX CONVERTER", "S.S.A_BINARY CONVERTER", "PHP SHELLS", "WEB SETINEL2ATT", "PHP Tools"
]

script_buttons = []
for i, (func, name) in enumerate(zip(script_functions, script_names)):
    button = tk.Button(main_frame, text=name, command=func, **button_style, state='disabled')
    row = i // 4
    column = i % 4
    main_frame.grid_rowconfigure(row, weight=1)
    main_frame.grid_columnconfigure(column, weight=1)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    script_buttons.append(button)

# Command entry fields and "Run All" button setup in command_frame
command_label1 = tk.Label(command_frame, text="Linux Terminal Command 1:", fg='red', bg='#000', font=('Arial', 11))
command_label1.grid(row=0, column=0, padx=5, pady=2, sticky='nsew')

command_entry1 = tk.Entry(command_frame, width=30)
command_entry1.grid(row=1, column=0, padx=5, pady=2, sticky='nsew')
command_entry1['state'] = 'disabled'

command_label2 = tk.Label(command_frame, text="Linux Terminal Command  2:", fg='red', bg='#000', font=('Arial', 11))
command_label2.grid(row=0, column=1, padx=5, pady=2, sticky='nsew')

command_entry2 = tk.Entry(command_frame, width=30)
command_entry2.grid(row=1, column=1, padx=5, pady=2, sticky='nsew')
command_entry2['state'] = 'disabled'

command_label3 = tk.Label(command_frame, text="Linux Terminal Command 3:", fg='red', bg='#000', font=('Arial', 11))
command_label3.grid(row=0, column=2, padx=5, pady=2, sticky='nsew')

command_entry3 = tk.Entry(command_frame, width=30)
command_entry3.grid(row=1, column=2, padx=5, pady=2, sticky='nsew')
command_entry3['state'] = 'disabled'

# Improved "Run All Commands" Button
run_all_button = tk.Button(command_frame, text="Run All Commands", command=run_multiple_commands, 
                           bg='black',fg='red', font=('Helvetica', 12, 'bold'), 
                           borderwidth=0, relief="raised")
run_all_button.grid(row=0, column=3, rowspan=15, padx=20, pady=20, sticky='nsew')
run_all_button['state'] = 'disabled'

#Create a frame for the network information label
network_info_frame = tk.Frame(root, bg='black')
# Place the frame below the logo, adjust the row and column as needed
network_info_frame.grid(row=0, column=0, sticky='w')  # Align to the left (west)

# Create a label to display the network information inside the frame
# Create a label to display the network information inside the frame
network_info_label = tk.Label(network_info_frame, text="", fg='red', bg='black', font=('Helvetica', 10, 'bold'))
network_info_label.pack(side='top', fill='x', padx=10, pady=10)  # Pack the label at the top

# Create a refresh button for updating network information
refresh_button = tk.Button(network_info_frame, text="""
  (Click to View/Re-Check)
  Network Information""", command=update_network_info, 
                           borderwidth='0', bg='black', fg='red', font=('Helvetica', 8))
refresh_button.pack(side='bottom', fill='x', padx=0, pady=0)  # Place it at the bottom of the frame

# Adjust the column configuration of root
root.grid_columnconfigure(0, weight=2)  # Adjust the weight as needed

# Adding a text paragraph
text_paragraph = tk.Label(root, text="This Software is for use on Authorized Systems only.",fg='red', bg='#000', font=('Arial', 8))
text_paragraph.grid(row=7, column=0, columnspan=4, pady=(10, 0))

# Adding a footer with link
def open_intercuba():
    webbrowser.open("https://intercuba.net")

# Load the flag image
flag_image = PhotoImage(file="scripts/SSA_PANEL/logos/flag.png")  # Replace with the path to your flag image

# Create the flag label
flag_label = tk.Label(footer_frame, image=flag_image, bg='#000')
flag_label.pack(side='left', padx=(10, 0))

# Create the clickable text label
footer_text = "© InterCuba.net"
footer_label = tk.Label(footer_frame, text=footer_text, fg='white', bg='#000', font=('Arial', 10), cursor="hand2")
footer_label.pack(side='left')
footer_label.bind("<Button-1>", lambda e: open_intercuba())

# Add all widgets that need to be authenticated in a list
authenticated_widgets = [password_entry, submit_button, run_all_button] + script_buttons
# Start the GUI loop
root.mainloop()
