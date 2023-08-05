#!/usr/bin/env python3

import sys
import sqlite3
import subprocess
import questionary as q
from tabulate import tabulate
import matplotlib.pyplot as plt
import hashlib
import os

DATABASE_FILE = "control_panel.db"
SALT = b'\x99\xc5\xff\x17\xc6\xdey\xab\x96\x08+\xd8\xd2F3\xaa'

if __name__ == "__main__":
    ascii_art = """
    ⠀⢀⣤⣤⣤⣤⣤⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠻⢿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣼⣿⡏⠀⠀⠀⢀⣀⣀⣀⣀⠀⢸⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
    ⠀⣿⣿⠁⠀⠀⢰⣿⣿⣿⣿⣿⡆⠘⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
    ⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣀⣈⣿⣿⣿⣿⣿⣦⡀⠀⠀
    ⠀⣿⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
    ⠀⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
    ⠀⢿⣿⡆⠀⠀⠀⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⡇⠀
    ⠀⠸⣿⣧⡀⠀  ALPHA#66⠈⠙⢿⣿⡇⠀
    ⠀⠀⠛⢿⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣿⡇⠀⠀
    ⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠿⠛⠉
    """

    print(ascii_art)
def install_required_packages():
    try:
        import questionary
        import matplotlib
        import tabulate
    except ImportError:
        print("Installing required packages...")
        try:
            subprocess.run(["pip", "install", "questionary", "matplotlib", "tabulate","sqlite3",], check=True)
        except subprocess.CalledProcessError as e:
            print("Error installing required packages. Make sure you have pip installed.")
            sys.exit(1)

def connect_db():
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS target_companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        industry TEXT,
        contact_info TEXT,
        description TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS target_agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_name TEXT NOT NULL,
        position TEXT,
        contact_info TEXT,
        assigned_company TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS vulnerable_domains (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain_name TEXT NOT NULL,
        vulnerability_type TEXT,
        risk_level TEXT,
        affected_company TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS communist_agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT,
        communist_party TEXT,
        personal_info TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS shells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT,
        type TEXT,
        capacity TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS interesting_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            file_url TEXT NOT NULL
        )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note_title TEXT NOT NULL,
            note_content TEXT NOT NULL
        )''')

    conn.commit()
    conn.close()

def hash_password(password):
    # Hash the password with the salt before storing it in the database
    salted_password = SALT + password.encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

def admin_registration():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM admin")
    count = cursor.fetchone()[0]
    if count == 0:
        print("Admin registration required. Please provide the admin credentials.")
        admin_username = q.text("Admin Username:").ask()
        admin_password = q.password("Admin Password:").ask()
        hashed_password = hash_password(admin_password)

        cursor.execute("INSERT INTO admin (username, password_hash) VALUES (?, ?)", (admin_username, hashed_password))
        conn.commit()
        print("Admin registration successful.")
    else:
        print("Admin is already registered.")
    conn.close()

def admin_login():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM admin")
    count = cursor.fetchone()[0]
    if count == 0:
        print("Admin not registered. Please register first.")
        sys.exit(1)
    print("*********************")
    print("Admin login required.")
    print("*********************")
    admin_username = q.text("Admin Username #").ask()
    admin_password = q.password("Admin Password #").ask()
    hashed_password = hash_password(admin_password)

    cursor.execute("SELECT COUNT(*) FROM admin WHERE username = ? AND password_hash = ?", (admin_username, hashed_password))
    count = cursor.fetchone()[0]
    if count == 0:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Admin login failed. Incorrect credentials.")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        sys.exit(1)
    print("************************")
    print("Admin login successful.")
    print("************************")

    conn.close()

def main():
    install_required_packages()
    create_tables()
    admin_registration()
    admin_login()

    # ... (Rest of the main function)

if __name__ == "__main__":
    main()


def add_target_company(company_name, industry, contact_info, description):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO target_companies (company_name, industry, contact_info, description) VALUES (?, ?, ?, ?)",
                   (company_name, industry, contact_info, description))

    conn.commit()
    print("Target company added successfully.")
    conn.close()

def edit_target_company():
    conn = connect_db()
    cursor = conn.cursor()

    view_target_companies()
    company_id = q.text("Enter the ID of the company you want to edit:").ask()

    cursor.execute("SELECT * FROM target_companies WHERE id = ?", (company_id,))
    company = cursor.fetchone()

    if not company:
        print("Company not found.")
        conn.close()
        return

    print("Company details:")
    print("1. Company Name:", company[1])
    print("2. Industry:", company[2])
    print("3. Contact Info:", company[3])
    print("4. Description:", company[4])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "company_name",
        "2": "industry",
        "3": "contact_info",
        "4": "description"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE target_companies SET {field_name} = ? WHERE id = ?", (new_value, company_id))
        conn.commit()
        print("Company details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_target_company():
    conn = connect_db()
    cursor = conn.cursor()

    view_target_companies()
    company_id = q.text("Enter the ID of the company you want to delete:").ask()

    cursor.execute("SELECT * FROM target_companies WHERE id = ?", (company_id,))
    company = cursor.fetchone()

    if not company:
        print("Company not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the company '{company[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM target_companies WHERE id = ?", (company_id,))
        conn.commit()
        print("Company deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_target_companies():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM target_companies")
    companies = cursor.fetchall()

    if not companies:
        print("No target companies found.")
    else:
        table_headers = ["ID", "Company Name", "Industry", "Contact Info", "Description"]
        table_data = [(company[0], company[1], company[2], company[3], company[4]) for company in companies]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()
def add_target_agent(agent_name, position, contact_info, assigned_company):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO target_agents (agent_name, position, contact_info, assigned_company) VALUES (?, ?, ?, ?)",
                   (agent_name, position, contact_info, assigned_company))

    conn.commit()
    print("Target agent added successfully.")
    conn.close()

def edit_target_agent():
    conn = connect_db()
    cursor = conn.cursor()

    view_target_agents()
    agent_id = q.text("Enter the ID of the agent you want to edit:").ask()

    cursor.execute("SELECT * FROM target_agents WHERE id = ?", (agent_id,))
    agent = cursor.fetchone()

    if not agent:
        print("Agent not found.")
        conn.close()
        return

    print("Agent details:")
    print("1. Agent Name:", agent[1])
    print("2. Position:", agent[2])
    print("3. Contact Info:", agent[3])
    print("4. Assigned Company:", agent[4])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "agent_name",
        "2": "position",
        "3": "contact_info",
        "4": "assigned_company"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE target_agents SET {field_name} = ? WHERE id = ?", (new_value, agent_id))
        conn.commit()
        print("Agent details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_target_agent():
    conn = connect_db()
    cursor = conn.cursor()

    view_target_agents()
    agent_id = q.text("Enter the ID of the agent you want to delete:").ask()

    cursor.execute("SELECT * FROM target_agents WHERE id = ?", (agent_id,))
    agent = cursor.fetchone()

    if not agent:
        print("Agent not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the agent '{agent[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM target_agents WHERE id = ?", (agent_id,))
        conn.commit()
        print("Agent deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_target_agents():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM target_agents")
    agents = cursor.fetchall()

    if not agents:
        print("No target agents found.")
    else:
        table_headers = ["ID", "Agent Name", "Position", "Contact Info", "Assigned Company"]
        table_data = [(agent[0], agent[1], agent[2], agent[3], agent[4]) for agent in agents]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()
def add_vulnerable_domain(domain_name, vulnerability_type, risk_level, affected_company):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO vulnerable_domains (domain_name, vulnerability_type, risk_level, affected_company) VALUES (?, ?, ?, ?)",
                   (domain_name, vulnerability_type, risk_level, affected_company))

    conn.commit()
    print("Vulnerable domain added successfully.")
    conn.close()

def edit_vulnerable_domain():
    conn = connect_db()
    cursor = conn.cursor()

    view_vulnerable_domains()
    domain_id = q.text("Enter the ID of the vulnerable domain you want to edit:").ask()

    cursor.execute("SELECT * FROM vulnerable_domains WHERE id = ?", (domain_id,))
    domain = cursor.fetchone()

    if not domain:
        print("Vulnerable domain not found.")
        conn.close()
        return

    print("Vulnerable domain details:")
    print("1. Domain Name:", domain[1])
    print("2. Vulnerability Type:", domain[2])
    print("3. Risk Level:", domain[3])
    print("4. Affected Company:", domain[4])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "domain_name",
        "2": "vulnerability_type",
        "3": "risk_level",
        "4": "affected_company"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE vulnerable_domains SET {field_name} = ? WHERE id = ?", (new_value, domain_id))
        conn.commit()
        print("Vulnerable domain details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_vulnerable_domain():
    conn = connect_db()
    cursor = conn.cursor()

    view_vulnerable_domains()
    domain_id = q.text("Enter the ID of the vulnerable domain you want to delete:").ask()

    cursor.execute("SELECT * FROM vulnerable_domains WHERE id = ?", (domain_id,))
    domain = cursor.fetchone()

    if not domain:
        print("Vulnerable domain not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the vulnerable domain '{domain[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM vulnerable_domains WHERE id = ?", (domain_id,))
        conn.commit()
        print("Vulnerable domain deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_vulnerable_domains():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM vulnerable_domains")
    domains = cursor.fetchall()

    if not domains:
        print("No vulnerable domains found.")
    else:
        table_headers = ["ID", "Domain Name", "Vulnerability Type", "Risk Level", "Affected Company"]
        table_data = [(domain[0], domain[1], domain[2], domain[3], domain[4]) for domain in domains]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()
def add_communist_agent(name, country, communist_party, personal_info):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO communist_agents (name, country, communist_party, personal_info) VALUES (?, ?, ?, ?)",
                   (name, country, communist_party, personal_info))

    conn.commit()
    print("Communist agent added successfully.")
    conn.close()

def edit_communist_agent():
    conn = connect_db()
    cursor = conn.cursor()

    view_communist_agents()
    agent_id = q.text("Enter the ID of the communist agent you want to edit:").ask()

    cursor.execute("SELECT * FROM communist_agents WHERE id = ?", (agent_id,))
    agent = cursor.fetchone()

    if not agent:
        print("Communist agent not found.")
        conn.close()
        return

    print("Communist agent details:")
    print("1. Name:", agent[1])
    print("2. Country:", agent[2])
    print("3. Communist Party:", agent[3])
    print("4. Personal Info:", agent[4])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "name",
        "2": "country",
        "3": "communist_party",
        "4": "personal_info"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE communist_agents SET {field_name} = ? WHERE id = ?", (new_value, agent_id))
        conn.commit()
        print("Communist agent details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_communist_agent():
    conn = connect_db()
    cursor = conn.cursor()

    view_communist_agents()
    agent_id = q.text("Enter the ID of the communist agent you want to delete:").ask()

    cursor.execute("SELECT * FROM communist_agents WHERE id = ?", (agent_id,))
    agent = cursor.fetchone()

    if not agent:
        print("Communist agent not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the communist agent '{agent[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM communist_agents WHERE id = ?", (agent_id,))
        conn.commit()
        print("Communist agent deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_communist_agents():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM communist_agents")
    agents = cursor.fetchall()

    if not agents:
        print("No communist agents found.")
    else:
        table_headers = ["ID", "Name", "Country", "Communist Party", "Personal Info"]
        table_data = [(agent[0], agent[1], agent[2], agent[3], agent[4]) for agent in agents]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()
def add_shell(name, location, shell_type, capacity):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO shells (name, location, type, capacity) VALUES (?, ?, ?, ?)",
                   (name, location, shell_type, capacity))

    conn.commit()
    print("Shell added successfully.")
    conn.close()

def edit_shell():
    conn = connect_db()
    cursor = conn.cursor()

    view_shells()
    shell_id = q.text("Enter the ID of the shell you want to edit:").ask()

    cursor.execute("SELECT * FROM shells WHERE id = ?", (shell_id,))
    shell = cursor.fetchone()

    if not shell:
        print("Shell not found.")
        conn.close()
        return

    print("Shell details:")
    print("1. Name:", shell[1])
    print("2. Location:", shell[2])
    print("3. Type:", shell[3])
    print("4. Capacity:", shell[4])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "name",
        "2": "location",
        "3": "type",
        "4": "capacity"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE shells SET {field_name} = ? WHERE id = ?", (new_value, shell_id))
        conn.commit()
        print("Shell details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_shell():
    conn = connect_db()
    cursor = conn.cursor()

    view_shells()
    shell_id = q.text("Enter the ID of the shell you want to delete:").ask()

    cursor.execute("SELECT * FROM shells WHERE id = ?", (shell_id,))
    shell = cursor.fetchone()

    if not shell:
        print("Shell not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the shell '{shell[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM shells WHERE id = ?", (shell_id,))
        conn.commit()
        print("Shell deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_shells():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM shells")
    shells = cursor.fetchall()

    if not shells:
        print("No shells found.")
    else:
        table_headers = ["ID", "Name", "Location", "Type", "Capacity"]
        table_data = [(shell[0], shell[1], shell[2], shell[3], shell[4]) for shell in shells]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()
def main_menu():
    while True:
        print("\n---------- Control Panel Main Menu ----------")
        print("1. Target Companies")
        print("2. Target Agents")
        print("3. Vulnerable Domains")
        print("4. Communist Agents")
        print("5. Manage Deployed Shells")
        print("6. Manage Interesting Files")
        print("7. Manage Notes")
        print("8. Export Report")
        print("0. Exit")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            target_companies_menu()
        elif choice == "2":
            target_agents_menu()
        elif choice == "3":
            vulnerable_domains_menu()
        elif choice == "4":
            communist_agents_menu()
        elif choice == "5":
            shells_menu()
        elif choice == "8":
            export_report_menu()
        elif choice == "7":
            take_notes_menu()
        elif choice == "6":
            manage_interesting_files_menu()
        elif choice == "0":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
def target_companies_menu():
    while True:
        print("\n---------- Target Companies Menu ----------")
        print("1. Add Target Company")
        print("2. Edit Target Company")
        print("3. Delete Target Company")
        print("4. View All Target Companies")
        print("0. Back to Main Menu")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            add_target_company_menu()
        elif choice == "2":
            edit_target_company()
        elif choice == "3":
            delete_target_company()
        elif choice == "4":
            view_target_companies()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def add_target_company_menu():
    print("\n---------- Add Target Company ----------")
    company_name = q.text("Company Name:").ask()
    industry = q.text("Industry:").ask()
    contact_info = q.text("Contact Info:").ask()
    description = q.text("Description:").ask()

    add_target_company(company_name, industry, contact_info, description)

def target_agents_menu():
    while True:
        print("\n---------- Target Agents Menu ----------")
        print("1. Add Target Agent")
        print("2. Edit Target Agent")
        print("3. Delete Target Agent")
        print("4. View All Target Agents")
        print("0. Back to Main Menu")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            add_target_agent_menu()
        elif choice == "2":
            edit_target_agent()
        elif choice == "3":
            delete_target_agent()
        elif choice == "4":
            view_target_agents()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
def add_target_agent_menu():
    print("\n---------- Add Target Agent ----------")
    agent_name = q.text("Agent Name:").ask()
    position = q.text("Position:").ask()
    contact_info = q.text("Contact Info:").ask()
    assigned_company = q.text("Assigned Company:").ask()

    add_target_agent(agent_name, position, contact_info, assigned_company)

def vulnerable_domains_menu():
    while True:
        print("\n---------- Vulnerable Domains Menu ----------")
        print("1. Add Vulnerable Domain")
        print("2. Edit Vulnerable Domain")
        print("3. Delete Vulnerable Domain")
        print("4. View All Vulnerable Domains")
        print("0. Back to Main Menu")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            add_vulnerable_domain_menu()
        elif choice == "2":
            edit_vulnerable_domain()
        elif choice == "3":
            delete_vulnerable_domain()
        elif choice == "4":
            view_vulnerable_domains()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def add_vulnerable_domain_menu():
    print("\n---------- Add Vulnerable Domain ----------")
    domain_name = q.text("Domain Name:").ask()
    vulnerability_type = q.text("Vulnerability Type:").ask()
    risk_level = q.text("Risk Level:").ask()
    affected_company = q.text("Affected Company:").ask()

    add_vulnerable_domain(domain_name, vulnerability_type, risk_level, affected_company)

def communist_agents_menu():
    while True:
        print("\n---------- Communist Agents Menu ----------")
        print("1. Add Communist Agent")
        print("2. Edit Communist Agent")
        print("3. Delete Communist Agent")
        print("4. View All Communist Agents")
        print("0. Back to Main Menu")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            add_communist_agent_menu()
        elif choice == "2":
            edit_communist_agent()
        elif choice == "3":
            delete_communist_agent()
        elif choice == "4":
            view_communist_agents()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
def add_communist_agent_menu():
    print("\n---------- Add Communist Agent ----------")
    name = q.text("Name:").ask()
    country = q.text("Country:").ask()
    communist_party = q.text("Communist Party:").ask()
    personal_info = q.text("Personal Info:").ask()

    add_communist_agent(name, country, communist_party, personal_info)

def shells_menu():
    while True:
        print("\n---------- Shells Menu ----------")
        print("1. Add Shell")
        print("2. Edit Shell")
        print("3. Delete Shell")
        print("4. View All Shells")
        print("0. Back to Main Menu")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            add_shell_menu()
        elif choice == "2":
            edit_shell()
        elif choice == "3":
            delete_shell()
        elif choice == "4":
            view_shells()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def add_shell_menu():
    print("\n---------- Add Shell ----------")
    name = q.text("Name:").ask()
    location = q.text("Location:").ask()
    shell_type = q.text("Type:").ask()
    capacity = q.text("Capacity:").ask()

    add_shell(name, location, shell_type, capacity)

def export_report_menu():
    while True:
        print("\n---------- Export Report Menu ----------")
        print("1. Export to Text File")
        print("0. Back to Main Menu")
        choice = q.text("Enter your choice:").ask()

        if choice == "1":
            export_to_text_file()
        elif choice == "2":
            export_to_html()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

from tabulate import tabulate

def export_to_text_file():
    filename = q.text("Enter the filename for the text report:").ask()

    with open(filename, "w") as file:
        file.write("##########################################################\n")
        file.write("⢀⡠⣤⣶⣶⣦⣄⠀⠀OMEGA_7⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
        file.write("⣿⡟⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⣠⣤⡄⠀⢀⣴⣶⡄\n")
        file.write("⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣴⣿⣿⣿⣾⣿⣿⣿⡇\n")
        file.write("⢿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁\n")
        file.write("⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀\n")
        file.write("⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀\n")
        file.write("⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀\n")
        file.write("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀1976⠀⠀⠀⠀⠀⠀\n")
        file.write("##########################################################\n\n")
        file.write("   *** C.I.T Control Panel Report - Classified ***\n\n")
        file.write("##########################################################\n\n")
        file.write("-----===[ Target Companies ]===-----\n")
        file.write(tabulate(get_table_data("target_companies"), headers=["ID", "Company Name", "Industry", "Contact Info", "Description"], tablefmt="grid"))
        file.write("\n\n")

        file.write("-----===[ Target Agents ]===-----\n")
        file.write(tabulate(get_table_data("target_agents"), headers=["ID", "Agent Name", "Position", "Contact Info", "Assigned Company"], tablefmt="grid"))
        file.write("\n\n")

        file.write("-----===[ Vulnerable Domains ]===-----\n")
        file.write(tabulate(get_table_data("vulnerable_domains"), headers=["ID", "Domain Name", "Vulnerability Type", "Risk Level", "Affected Company"], tablefmt="grid"))
        file.write("\n\n")

        file.write("-----===[ Communist Agents ]===-----\n")
        file.write(tabulate(get_table_data("communist_agents"), headers=["ID", "Name", "Country", "Communist Party", "Personal Info"], tablefmt="grid"))
        file.write("\n\n")

        file.write("-----===[ Shells ]===-----\n")
        file.write(tabulate(get_table_data("shells"), headers=["ID", "Name", "Location", "Type", "Capacity"], tablefmt="grid"))
        file.write("\n\n")

        file.write("-----===[ Notes ]===-----\n")
        file.write(tabulate(get_table_data("notes"), headers=["ID", "note_title", "note_content"], tablefmt="grid"))
        file.write("\n\n")

        file.write("-----===[ Interesting Files ]===-----\n")
        file.write(tabulate(get_table_data("interesting_files"), headers=["ID", "file_name", "file_url"], tablefmt="grid"))
        file.write("\n\n")
        file.write("InterCuba.Net - Krintoxi\n")
    print("")
    print("***********************************************************************************")
    print("Report exported as a text file named : (", filename,") Check The Toolkit Directory.")
    print("***********************************************************************************")


def get_table_data(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    conn.close()
    return data

def take_notes_menu():
    print("\n---------- Notes Menu ----------")
    print("1. Create Note")
    print("2. Edit Note")
    print("3. Delete Note")
    print("4. View All Notes")
    print("0. Back to Main Menu")
    choice = q.text("Enter your choice:").ask()

    if choice == "1":
        create_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        view_notes()
    elif choice == "0":
        return
    else:
        print("Invalid choice. Please try again.")
def create_note():
    note_title = q.text("Note Title:").ask()
    note_content = q.text("Note Content:").ask()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO notes (note_title, note_content) VALUES (?, ?)", (note_title, note_content))
    conn.commit()

    print("Note created successfully.")
    conn.close()

def edit_note():
    view_notes()
    note_id = q.text("Enter the ID of the note you want to edit:").ask()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = cursor.fetchone()

    if not note:
        print("Note not found.")
        conn.close()
        return

    print("Note details:")
    print("1. Note Title:", note[1])
    print("2. Note Content:", note[2])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "note_title",
        "2": "note_content"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE notes SET {field_name} = ? WHERE id = ?", (new_value, note_id))
        conn.commit()
        print("Note details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_note():
    view_notes()
    note_id = q.text("Enter the ID of the note you want to delete:").ask()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = cursor.fetchone()

    if not note:
        print("Note not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the note '{note[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
        print("Note deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_notes():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    if not notes:
        print("No notes found.")
    else:
        table_headers = ["ID", "Note Title", "Note Content"]
        table_data = [(note[0], note[1], note[2]) for note in notes]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()

def manage_interesting_files_menu():
    print("\n---------- Interesting Files Menu ----------")
    print("1. Add Interesting File")
    print("2. Edit Interesting File")
    print("3. Delete Interesting File")
    print("4. View All Interesting Files")
    print("0. Back to Main Menu")
    choice = q.text("Enter your choice:").ask()

    if choice == "1":
        add_interesting_file()
    elif choice == "2":
        edit_interesting_file()
    elif choice == "3":
        delete_interesting_file()
    elif choice == "4":
        view_interesting_files()
    elif choice == "0":
        return
    else:
        print("Invalid choice. Please try again.")
def add_interesting_file():
    file_name = q.text("File Name:").ask()
    file_url = q.text("File URL:").ask()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO interesting_files (file_name, file_url) VALUES (?, ?)", (file_name, file_url))
    conn.commit()

    print("Interesting file added successfully.")
    conn.close()

def edit_interesting_file():
    view_interesting_files()
    file_id = q.text("Enter the ID of the interesting file you want to edit:").ask()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interesting_files WHERE id = ?", (file_id,))
    file = cursor.fetchone()

    if not file:
        print("Interesting file not found.")
        conn.close()
        return

    print("Interesting file details:")
    print("1. File Name:", file[1])
    print("2. File URL:", file[2])

    field = q.text("Enter the number of the field you want to edit:").ask()
    new_value = q.text("Enter the new value:").ask()

    fields = {
        "1": "file_name",
        "2": "file_url"
    }

    if field in fields:
        field_name = fields[field]
        cursor.execute(f"UPDATE interesting_files SET {field_name} = ? WHERE id = ?", (new_value, file_id))
        conn.commit()
        print("Interesting file details updated successfully.")
    else:
        print("Invalid field number.")

    conn.close()

def delete_interesting_file():
    view_interesting_files()
    file_id = q.text("Enter the ID of the interesting file you want to delete:").ask()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interesting_files WHERE id = ?", (file_id,))
    file = cursor.fetchone()

    if not file:
        print("Interesting file not found.")
        conn.close()
        return

    confirm = q.confirm(f"Do you want to delete the interesting file '{file[1]}'?").ask()
    if confirm:
        cursor.execute("DELETE FROM interesting_files WHERE id = ?", (file_id,))
        conn.commit()
        print("Interesting file deleted successfully.")
    else:
        print("Deletion cancelled.")

    conn.close()

def view_interesting_files():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interesting_files")
    files = cursor.fetchall()

    if not files:
        print("No interesting files found.")
    else:
        table_headers = ["ID", "File Name", "File URL"]
        table_data = [(file[0], file[1], file[2]) for file in files]
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))

    conn.close()

def connect_db():
    conn = sqlite3.connect("control_panel.db")
    return conn

if __name__ == "__main__":
    create_tables()
    main_menu()
