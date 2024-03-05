#!/usr/bin/env python3
import sys #line:3:import sys
import sqlite3 #line:4:import sqlite3
import subprocess #line:5:import subprocess
import questionary as q #line:6:import questionary as q
from tabulate import tabulate #line:7:from tabulate import tabulate
import matplotlib .pyplot as plt #line:8:import matplotlib.pyplot as plt
import hashlib #line:9:import hashlib
import os #line:10:import os
DATABASE_FILE ="control_panel.db"#line:12:DATABASE_FILE = "control_panel.db"
SALT =b'\x99\xc5\xff\x17\xc6\xdey\xab\x96\x08+\xd8\xd2F3\xaa'#line:13:SALT = b'\x99\xc5\xff\x17\xc6\xdey\xab\x96\x08+\xd8\xd2F3\xaa'
if __name__ =="__main__":#line:15:if __name__ == "__main__":
    ascii_art ="""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠈⠙⠻⣿⣿⠟⠋⠁⠉⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⢠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿⣷⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⣶⣿⡇⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀    #ALPHA6⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠓⠒⠶⠤⠤⢤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣷⣦⣤⣀⡀⠀⢀⣼⣿⠀⠉⠉⠉⠉⠉⠉⠁⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢻⣿⣿⣿⡿⢷⣿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠉⠀⠈⣻⣿⣦⣀⡀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⡁⠹⡈⣳⠶⣿⣿⣽⣛⠋⠁⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⢱⣠⣿⣿⣷⣿⣿⣿⡿⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """#line:42:"""
    print (ascii_art )#line:44:print(ascii_art)
def install_required_packages ():#line:45:def install_required_packages():
    try :#line:46:try:
        import questionary #line:47:import questionary
        import matplotlib #line:48:import matplotlib
        import tabulate #line:49:import tabulate
    except ImportError :#line:50:except ImportError:
        print ("Installing required packages...")#line:51:print("Installing required packages...")
        try :#line:52:try:
            subprocess .run (["pip","install","questionary","matplotlib","tabulate","sqlite3",],check =True )#line:53:subprocess.run(["pip", "install", "questionary", "matplotlib", "tabulate","sqlite3",], check=True)
        except subprocess .CalledProcessError as OO00OO0O000O00OO0 :#line:54:except subprocess.CalledProcessError as e:
            print ("Error installing required packages. Make sure you have pip installed.")#line:55:print("Error installing required packages. Make sure you have pip installed.")
            sys .exit (1 )#line:56:sys.exit(1)
def connect_db ():#line:58:def connect_db():
    try :#line:59:try:
        OO0O00O00OOO0OOO0 =sqlite3 .connect (DATABASE_FILE )#line:60:conn = sqlite3.connect(DATABASE_FILE)
        return OO0O00O00OOO0OOO0 #line:61:return conn
    except sqlite3 .Error as OOOO00OOO0O0O0O0O :#line:62:except sqlite3.Error as e:
        print ("Error connecting to the database:",OOOO00OOO0O0O0O0O )#line:63:print("Error connecting to the database:", e)
        sys .exit (1 )#line:64:sys.exit(1)
def create_tables ():#line:66:def create_tables():
    O00OOOO00OOOOOO0O =connect_db ()#line:67:conn = connect_db()
    OOOOOO0OO0OOOOOO0 =O00OOOO00OOOOOO0O .cursor ()#line:68:cursor = conn.cursor()
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS target_companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL,
        industry TEXT,
        contact_info TEXT,
        description TEXT
    )''')#line:77:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS target_agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_name TEXT NOT NULL,
        position TEXT,
        contact_info TEXT,
        assigned_company TEXT
    )''')#line:85:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS vulnerable_domains (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        domain_name TEXT NOT NULL,
        vulnerability_type TEXT,
        risk_level TEXT,
        affected_company TEXT
    )''')#line:93:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL
    )''')#line:99:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS communist_agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT,
        communist_party TEXT,
        personal_info TEXT
    )''')#line:107:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS shells (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT,
        type TEXT,
        capacity TEXT
    )''')#line:115:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS interesting_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            file_url TEXT NOT NULL
        )''')#line:121:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note_title TEXT NOT NULL,
            note_content TEXT NOT NULL
        )''')#line:126:)''')
    OOOOOO0OO0OOOOOO0 .execute ('''CREATE TABLE IF NOT EXISTS aes_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL,
    aes_key TEXT NOT NULL,
    creation_date TEXT NOT NULL
    )''')#line:132:)''')
    O00OOOO00OOOOOO0O .commit ()#line:135:conn.commit()
    O00OOOO00OOOOOO0O .close ()#line:136:conn.close()
def hash_password (O00OO0OO0000OO00O ):#line:138:def hash_password(password):
    O0O0OO00O00000OO0 =SALT +O00OO0OO0000OO00O .encode ('utf-8')#line:140:salted_password = SALT + password.encode('utf-8')
    OOOO0OOO00000O000 =hashlib .sha256 (O0O0OO00O00000OO0 ).hexdigest ()#line:141:hashed_password = hashlib.sha256(salted_password).hexdigest()
    return OOOO0OOO00000O000 #line:142:return hashed_password
def admin_registration ():#line:144:def admin_registration():
    O0OO000O000O00000 =connect_db ()#line:145:conn = connect_db()
    O0OO0O0000O0OO00O =O0OO000O000O00000 .cursor ()#line:146:cursor = conn.cursor()
    O0OO0O0000O0OO00O .execute ("SELECT COUNT(*) FROM admin")#line:148:cursor.execute("SELECT COUNT(*) FROM admin")
    O000O00000OO000O0 =O0OO0O0000O0OO00O .fetchone ()[0 ]#line:149:count = cursor.fetchone()[0]
    if O000O00000OO000O0 ==0 :#line:150:if count == 0:
        print ("Admin registration required. Please provide the admin credentials.")#line:151:print("Admin registration required. Please provide the admin credentials.")
        OO0OO0O0000OO00O0 =q .text ("Admin Username:").ask ()#line:152:admin_username = q.text("Admin Username:").ask()
        O0O00OOO00O000O00 =q .password ("Admin Password:").ask ()#line:153:admin_password = q.password("Admin Password:").ask()
        O00O00O0O0OOOOOO0 =hash_password (O0O00OOO00O000O00 )#line:154:hashed_password = hash_password(admin_password)
        O0OO0O0000O0OO00O .execute ("INSERT INTO admin (username, password_hash) VALUES (?, ?)",(OO0OO0O0000OO00O0 ,O00O00O0O0OOOOOO0 ))#line:156:cursor.execute("INSERT INTO admin (username, password_hash) VALUES (?, ?)", (admin_username, hashed_password))
        O0OO000O000O00000 .commit ()#line:157:conn.commit()
        print ("Admin registration successful.")#line:158:print("Admin registration successful.")
    else :#line:159:else:
        print ("Admin is already registered.")#line:160:print("Admin is already registered.")
    O0OO000O000O00000 .close ()#line:161:conn.close()
def admin_login ():#line:163:def admin_login():
    OOO00OO000OO000OO =connect_db ()#line:164:conn = connect_db()
    OOOOO00O0O0O000O0 =OOO00OO000OO000OO .cursor ()#line:165:cursor = conn.cursor()
    OOOOO00O0O0O000O0 .execute ("SELECT COUNT(*) FROM admin")#line:167:cursor.execute("SELECT COUNT(*) FROM admin")
    OOOOO0OOOO0O0000O =OOOOO00O0O0O000O0 .fetchone ()[0 ]#line:168:count = cursor.fetchone()[0]
    if OOOOO0OOOO0O0000O ==0 :#line:169:if count == 0:
        print ("Admin not registered. Please register first.")#line:170:print("Admin not registered. Please register first.")
        sys .exit (1 )#line:171:sys.exit(1)
    print ("*********************")#line:172:print("*********************")
    print ("Admin login required.")#line:173:print("Admin login required.")
    print ("*********************")#line:174:print("*********************")
    O00O0O00O0O0O00OO =q .text ("Admin Username #").ask ()#line:175:admin_username = q.text("Admin Username #").ask()
    OO000OOO0OO000OOO =q .password ("Admin Password #").ask ()#line:176:admin_password = q.password("Admin Password #").ask()
    OOOOO000OO0OOOOOO =hash_password (OO000OOO0OO000OOO )#line:177:hashed_password = hash_password(admin_password)
    OOOOO00O0O0O000O0 .execute ("SELECT COUNT(*) FROM admin WHERE username = ? AND password_hash = ?",(O00O0O00O0O0O00OO ,OOOOO000OO0OOOOOO ))#line:179:cursor.execute("SELECT COUNT(*) FROM admin WHERE username = ? AND password_hash = ?", (admin_username, hashed_password))
    OOOOO0OOOO0O0000O =OOOOO00O0O0O000O0 .fetchone ()[0 ]#line:180:count = cursor.fetchone()[0]
    if OOOOO0OOOO0O0000O ==0 :#line:181:if count == 0:
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")#line:182:print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print ("Admin login failed. Incorrect credentials.")#line:183:print("Admin login failed. Incorrect credentials.")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")#line:184:print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        sys .exit (1 )#line:185:sys.exit(1)
    print ("************************")#line:186:print("************************")
    print ("Admin login successful.")#line:187:print("Admin login successful.")
    print ("************************")#line:188:print("************************")
    OOO00OO000OO000OO .close ()#line:190:conn.close()
def main ():#line:192:def main():
    install_required_packages ()#line:193:install_required_packages()
    create_tables ()#line:194:create_tables()
    admin_registration ()#line:195:admin_registration()
    admin_login ()#line:196:admin_login()
if __name__ =="__main__":#line:200:if __name__ == "__main__":
    main ()#line:201:main()
def add_target_company (O0O0OO00OOOO00OOO ,OOO000O0O0OOOO00O ,OOO0O0OOOOOOO00OO ,O0O000OOOOOOO0OO0 ):#line:204:def add_target_company(company_name, industry, contact_info, description):
    OOOO000000OOO0OOO =connect_db ()#line:205:conn = connect_db()
    OOO000OO0O00O0OO0 =OOOO000000OOO0OOO .cursor ()#line:206:cursor = conn.cursor()
    OOO000OO0O00O0OO0 .execute ("INSERT INTO target_companies (company_name, industry, contact_info, description) VALUES (?, ?, ?, ?)",(O0O0OO00OOOO00OOO ,OOO000O0O0OOOO00O ,OOO0O0OOOOOOO00OO ,O0O000OOOOOOO0OO0 ))#line:209:(company_name, industry, contact_info, description))
    OOOO000000OOO0OOO .commit ()#line:211:conn.commit()
    print ("Target company added successfully.")#line:212:print("Target company added successfully.")
    OOOO000000OOO0OOO .close ()#line:213:conn.close()
def edit_target_company ():#line:215:def edit_target_company():
    O0O000O0O0OOOOO00 =connect_db ()#line:216:conn = connect_db()
    O00OO0000OOO0000O =O0O000O0O0OOOOO00 .cursor ()#line:217:cursor = conn.cursor()
    view_target_companies ()#line:219:view_target_companies()
    O000OO0OOO00O00O0 =q .text ("Enter the ID of the company you want to edit:").ask ()#line:220:company_id = q.text("Enter the ID of the company you want to edit:").ask()
    O00OO0000OOO0000O .execute ("SELECT * FROM target_companies WHERE id = ?",(O000OO0OOO00O00O0 ,))#line:222:cursor.execute("SELECT * FROM target_companies WHERE id = ?", (company_id,))
    O0O00O00OOO0O0000 =O00OO0000OOO0000O .fetchone ()#line:223:company = cursor.fetchone()
    if not O0O00O00OOO0O0000 :#line:225:if not company:
        print ("Company not found.")#line:226:print("Company not found.")
        O0O000O0O0OOOOO00 .close ()#line:227:conn.close()
        return #line:228:return
    print ("Company details:")#line:230:print("Company details:")
    print ("1. Company Name:",O0O00O00OOO0O0000 [1 ])#line:231:print("1. Company Name:", company[1])
    print ("2. Industry:",O0O00O00OOO0O0000 [2 ])#line:232:print("2. Industry:", company[2])
    print ("3. Contact Info:",O0O00O00OOO0O0000 [3 ])#line:233:print("3. Contact Info:", company[3])
    print ("4. Description:",O0O00O00OOO0O0000 [4 ])#line:234:print("4. Description:", company[4])
    OOOOOOOOOO00000O0 =q .text ("Enter the number of the field you want to edit:").ask ()#line:236:field = q.text("Enter the number of the field you want to edit:").ask()
    OOO0OOO000OOO0OO0 =q .text ("Enter the new value:").ask ()#line:237:new_value = q.text("Enter the new value:").ask()
    O0OOOOO000O000O00 ={"1":"company_name","2":"industry","3":"contact_info","4":"description"}#line:244:}
    if OOOOOOOOOO00000O0 in O0OOOOO000O000O00 :#line:246:if field in fields:
        OOO0OOO0O00O00OOO =O0OOOOO000O000O00 [OOOOOOOOOO00000O0 ]#line:247:field_name = fields[field]
        O00OO0000OOO0000O .execute (f"UPDATE target_companies SET {OOO0OOO0O00O00OOO} = ? WHERE id = ?",(OOO0OOO000OOO0OO0 ,O000OO0OOO00O00O0 ))#line:248:cursor.execute(f"UPDATE target_companies SET {field_name} = ? WHERE id = ?", (new_value, company_id))
        O0O000O0O0OOOOO00 .commit ()#line:249:conn.commit()
        print ("Company details updated successfully.")#line:250:print("Company details updated successfully.")
    else :#line:251:else:
        print ("Invalid field number.")#line:252:print("Invalid field number.")
    O0O000O0O0OOOOO00 .close ()#line:254:conn.close()
def delete_target_company ():#line:256:def delete_target_company():
    OOO0O00O0OOOOO0OO =connect_db ()#line:257:conn = connect_db()
    OOOO0O000O00OO00O =OOO0O00O0OOOOO0OO .cursor ()#line:258:cursor = conn.cursor()
    view_target_companies ()#line:260:view_target_companies()
    OO0OO00000O0OOO00 =q .text ("Enter the ID of the company you want to delete:").ask ()#line:261:company_id = q.text("Enter the ID of the company you want to delete:").ask()
    OOOO0O000O00OO00O .execute ("SELECT * FROM target_companies WHERE id = ?",(OO0OO00000O0OOO00 ,))#line:263:cursor.execute("SELECT * FROM target_companies WHERE id = ?", (company_id,))
    O0OO0OOOOOO0O000O =OOOO0O000O00OO00O .fetchone ()#line:264:company = cursor.fetchone()
    if not O0OO0OOOOOO0O000O :#line:266:if not company:
        print ("Company not found.")#line:267:print("Company not found.")
        OOO0O00O0OOOOO0OO .close ()#line:268:conn.close()
        return #line:269:return
    O0OO0O0OOOO0OO000 =q .confirm (f"Do you want to delete the company '{O0OO0OOOOOO0O000O[1]}'?").ask ()#line:271:confirm = q.confirm(f"Do you want to delete the company '{company[1]}'?").ask()
    if O0OO0O0OOOO0OO000 :#line:272:if confirm:
        OOOO0O000O00OO00O .execute ("DELETE FROM target_companies WHERE id = ?",(OO0OO00000O0OOO00 ,))#line:273:cursor.execute("DELETE FROM target_companies WHERE id = ?", (company_id,))
        OOO0O00O0OOOOO0OO .commit ()#line:274:conn.commit()
        print ("Company deleted successfully.")#line:275:print("Company deleted successfully.")
    else :#line:276:else:
        print ("Deletion cancelled.")#line:277:print("Deletion cancelled.")
    OOO0O00O0OOOOO0OO .close ()#line:279:conn.close()
def view_target_companies ():#line:281:def view_target_companies():
    O00O00O00O0O000OO =connect_db ()#line:282:conn = connect_db()
    OO00000OOO0000OOO =O00O00O00O0O000OO .cursor ()#line:283:cursor = conn.cursor()
    OO00000OOO0000OOO .execute ("SELECT * FROM target_companies")#line:285:cursor.execute("SELECT * FROM target_companies")
    O0OO00000OOO00O0O =OO00000OOO0000OOO .fetchall ()#line:286:companies = cursor.fetchall()
    if not O0OO00000OOO00O0O :#line:288:if not companies:
        print ("No target companies found.")#line:289:print("No target companies found.")
    else :#line:290:else:
        O00000O00OO000OOO =["ID","Company Name","Industry","Contact Info","Description"]#line:291:table_headers = ["ID", "Company Name", "Industry", "Contact Info", "Description"]
        O0O000O00O0O00O00 =[(OOOO00OOO0O0OOOOO [0 ],OOOO00OOO0O0OOOOO [1 ],OOOO00OOO0O0OOOOO [2 ],OOOO00OOO0O0OOOOO [3 ],OOOO00OOO0O0OOOOO [4 ])for OOOO00OOO0O0OOOOO in O0OO00000OOO00O0O ]#line:292:table_data = [(company[0], company[1], company[2], company[3], company[4]) for company in companies]
        print (tabulate (O0O000O00O0O00O00 ,headers =O00000O00OO000OOO ,tablefmt ="grid"))#line:293:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    O00O00O00O0O000OO .close ()#line:295:conn.close()
def add_target_agent (OO00O0O00O0O000OO ,OOO0OO0O0OO0000OO ,OOO0OOOOO0O0O0O00 ,O000000OOOOO0O0OO ):#line:296:def add_target_agent(agent_name, position, contact_info, assigned_company):
    O00OO000OO00OO0OO =connect_db ()#line:297:conn = connect_db()
    OOOOOO0OO0O000O00 =O00OO000OO00OO0OO .cursor ()#line:298:cursor = conn.cursor()
    OOOOOO0OO0O000O00 .execute ("INSERT INTO target_agents (agent_name, position, contact_info, assigned_company) VALUES (?, ?, ?, ?)",(OO00O0O00O0O000OO ,OOO0OO0O0OO0000OO ,OOO0OOOOO0O0O0O00 ,O000000OOOOO0O0OO ))#line:301:(agent_name, position, contact_info, assigned_company))
    O00OO000OO00OO0OO .commit ()#line:303:conn.commit()
    print ("Target agent added successfully.")#line:304:print("Target agent added successfully.")
    O00OO000OO00OO0OO .close ()#line:305:conn.close()
def edit_target_agent ():#line:307:def edit_target_agent():
    OO00000O0OOOO0O0O =connect_db ()#line:308:conn = connect_db()
    OOO0OOO0OOOOO0OO0 =OO00000O0OOOO0O0O .cursor ()#line:309:cursor = conn.cursor()
    view_target_agents ()#line:311:view_target_agents()
    OOO0O0OOOO0OO000O =q .text ("Enter the ID of the agent you want to edit:").ask ()#line:312:agent_id = q.text("Enter the ID of the agent you want to edit:").ask()
    OOO0OOO0OOOOO0OO0 .execute ("SELECT * FROM target_agents WHERE id = ?",(OOO0O0OOOO0OO000O ,))#line:314:cursor.execute("SELECT * FROM target_agents WHERE id = ?", (agent_id,))
    O00O000O00OO0OO00 =OOO0OOO0OOOOO0OO0 .fetchone ()#line:315:agent = cursor.fetchone()
    if not O00O000O00OO0OO00 :#line:317:if not agent:
        print ("Agent not found.")#line:318:print("Agent not found.")
        OO00000O0OOOO0O0O .close ()#line:319:conn.close()
        return #line:320:return
    print ("Agent details:")#line:322:print("Agent details:")
    print ("1. Agent Name:",O00O000O00OO0OO00 [1 ])#line:323:print("1. Agent Name:", agent[1])
    print ("2. Position:",O00O000O00OO0OO00 [2 ])#line:324:print("2. Position:", agent[2])
    print ("3. Contact Info:",O00O000O00OO0OO00 [3 ])#line:325:print("3. Contact Info:", agent[3])
    print ("4. Assigned Company:",O00O000O00OO0OO00 [4 ])#line:326:print("4. Assigned Company:", agent[4])
    O00OO0O00O00OO00O =q .text ("Enter the number of the field you want to edit:").ask ()#line:328:field = q.text("Enter the number of the field you want to edit:").ask()
    O000000000OO0OO00 =q .text ("Enter the new value:").ask ()#line:329:new_value = q.text("Enter the new value:").ask()
    OOOOOOO00OO0OO0O0 ={"1":"agent_name","2":"position","3":"contact_info","4":"assigned_company"}#line:336:}
    if O00OO0O00O00OO00O in OOOOOOO00OO0OO0O0 :#line:338:if field in fields:
        O0O0O00OOOOO0OO00 =OOOOOOO00OO0OO0O0 [O00OO0O00O00OO00O ]#line:339:field_name = fields[field]
        OOO0OOO0OOOOO0OO0 .execute (f"UPDATE target_agents SET {O0O0O00OOOOO0OO00} = ? WHERE id = ?",(O000000000OO0OO00 ,OOO0O0OOOO0OO000O ))#line:340:cursor.execute(f"UPDATE target_agents SET {field_name} = ? WHERE id = ?", (new_value, agent_id))
        OO00000O0OOOO0O0O .commit ()#line:341:conn.commit()
        print ("Agent details updated successfully.")#line:342:print("Agent details updated successfully.")
    else :#line:343:else:
        print ("Invalid field number.")#line:344:print("Invalid field number.")
    OO00000O0OOOO0O0O .close ()#line:346:conn.close()
def delete_target_agent ():#line:348:def delete_target_agent():
    O0O0OOO0O00OOO0OO =connect_db ()#line:349:conn = connect_db()
    O00O0OOOOO00OO000 =O0O0OOO0O00OOO0OO .cursor ()#line:350:cursor = conn.cursor()
    view_target_agents ()#line:352:view_target_agents()
    OO0OOOO0OOOO0OO00 =q .text ("Enter the ID of the agent you want to delete:").ask ()#line:353:agent_id = q.text("Enter the ID of the agent you want to delete:").ask()
    O00O0OOOOO00OO000 .execute ("SELECT * FROM target_agents WHERE id = ?",(OO0OOOO0OOOO0OO00 ,))#line:355:cursor.execute("SELECT * FROM target_agents WHERE id = ?", (agent_id,))
    O0OOO00000OO000OO =O00O0OOOOO00OO000 .fetchone ()#line:356:agent = cursor.fetchone()
    if not O0OOO00000OO000OO :#line:358:if not agent:
        print ("Agent not found.")#line:359:print("Agent not found.")
        O0O0OOO0O00OOO0OO .close ()#line:360:conn.close()
        return #line:361:return
    OOO0OOOO0OO0OO00O =q .confirm (f"Do you want to delete the agent '{O0OOO00000OO000OO[1]}'?").ask ()#line:363:confirm = q.confirm(f"Do you want to delete the agent '{agent[1]}'?").ask()
    if OOO0OOOO0OO0OO00O :#line:364:if confirm:
        O00O0OOOOO00OO000 .execute ("DELETE FROM target_agents WHERE id = ?",(OO0OOOO0OOOO0OO00 ,))#line:365:cursor.execute("DELETE FROM target_agents WHERE id = ?", (agent_id,))
        O0O0OOO0O00OOO0OO .commit ()#line:366:conn.commit()
        print ("Agent deleted successfully.")#line:367:print("Agent deleted successfully.")
    else :#line:368:else:
        print ("Deletion cancelled.")#line:369:print("Deletion cancelled.")
    O0O0OOO0O00OOO0OO .close ()#line:371:conn.close()
def view_target_agents ():#line:373:def view_target_agents():
    O000OOO0O00O000OO =connect_db ()#line:374:conn = connect_db()
    O00OO0OO00000OOOO =O000OOO0O00O000OO .cursor ()#line:375:cursor = conn.cursor()
    O00OO0OO00000OOOO .execute ("SELECT * FROM target_agents")#line:377:cursor.execute("SELECT * FROM target_agents")
    OOO0OO0OO00OO0O00 =O00OO0OO00000OOOO .fetchall ()#line:378:agents = cursor.fetchall()
    if not OOO0OO0OO00OO0O00 :#line:380:if not agents:
        print ("No target agents found.")#line:381:print("No target agents found.")
    else :#line:382:else:
        O0OOO00OOOOO0O0OO =["ID","Agent Name","Position","Contact Info","Assigned Company"]#line:383:table_headers = ["ID", "Agent Name", "Position", "Contact Info", "Assigned Company"]
        OO0OOOOOOO000000O =[(OOO0O0OO000000O0O [0 ],OOO0O0OO000000O0O [1 ],OOO0O0OO000000O0O [2 ],OOO0O0OO000000O0O [3 ],OOO0O0OO000000O0O [4 ])for OOO0O0OO000000O0O in OOO0OO0OO00OO0O00 ]#line:384:table_data = [(agent[0], agent[1], agent[2], agent[3], agent[4]) for agent in agents]
        print (tabulate (OO0OOOOOOO000000O ,headers =O0OOO00OOOOO0O0OO ,tablefmt ="grid"))#line:385:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    O000OOO0O00O000OO .close ()#line:387:conn.close()
def add_vulnerable_domain (O0000O0000O0OOO0O ,O0OOO0OO000OOOOOO ,O0O00O0000O000OOO ,O00OO0O0OO00O0O00 ):#line:388:def add_vulnerable_domain(domain_name, vulnerability_type, risk_level, affected_company):
    OO0O0O0OOO0OO0000 =connect_db ()#line:389:conn = connect_db()
    OOOO00OOO0OO0OO00 =OO0O0O0OOO0OO0000 .cursor ()#line:390:cursor = conn.cursor()
    OOOO00OOO0OO0OO00 .execute ("INSERT INTO vulnerable_domains (domain_name, vulnerability_type, risk_level, affected_company) VALUES (?, ?, ?, ?)",(O0000O0000O0OOO0O ,O0OOO0OO000OOOOOO ,O0O00O0000O000OOO ,O00OO0O0OO00O0O00 ))#line:393:(domain_name, vulnerability_type, risk_level, affected_company))
    OO0O0O0OOO0OO0000 .commit ()#line:395:conn.commit()
    print ("Vulnerable domain added successfully.")#line:396:print("Vulnerable domain added successfully.")
    OO0O0O0OOO0OO0000 .close ()#line:397:conn.close()
def edit_vulnerable_domain ():#line:399:def edit_vulnerable_domain():
    OO0OO00OOO0O00O0O =connect_db ()#line:400:conn = connect_db()
    O000O0OOO0OO0O00O =OO0OO00OOO0O00O0O .cursor ()#line:401:cursor = conn.cursor()
    view_vulnerable_domains ()#line:403:view_vulnerable_domains()
    O0000OO0000O0OO00 =q .text ("Enter the ID of the vulnerable domain you want to edit:").ask ()#line:404:domain_id = q.text("Enter the ID of the vulnerable domain you want to edit:").ask()
    O000O0OOO0OO0O00O .execute ("SELECT * FROM vulnerable_domains WHERE id = ?",(O0000OO0000O0OO00 ,))#line:406:cursor.execute("SELECT * FROM vulnerable_domains WHERE id = ?", (domain_id,))
    OO0OOOO000OOO0000 =O000O0OOO0OO0O00O .fetchone ()#line:407:domain = cursor.fetchone()
    if not OO0OOOO000OOO0000 :#line:409:if not domain:
        print ("Vulnerable domain not found.")#line:410:print("Vulnerable domain not found.")
        OO0OO00OOO0O00O0O .close ()#line:411:conn.close()
        return #line:412:return
    print ("Vulnerable domain details:")#line:414:print("Vulnerable domain details:")
    print ("1. Domain Name:",OO0OOOO000OOO0000 [1 ])#line:415:print("1. Domain Name:", domain[1])
    print ("2. Vulnerability Type:",OO0OOOO000OOO0000 [2 ])#line:416:print("2. Vulnerability Type:", domain[2])
    print ("3. Risk Level:",OO0OOOO000OOO0000 [3 ])#line:417:print("3. Risk Level:", domain[3])
    print ("4. Affected Company:",OO0OOOO000OOO0000 [4 ])#line:418:print("4. Affected Company:", domain[4])
    OOOOOO00OO00O00O0 =q .text ("Enter the number of the field you want to edit:").ask ()#line:420:field = q.text("Enter the number of the field you want to edit:").ask()
    O00OO0OO0OO0000OO =q .text ("Enter the new value:").ask ()#line:421:new_value = q.text("Enter the new value:").ask()
    O0OO00000O000OO0O ={"1":"domain_name","2":"vulnerability_type","3":"risk_level","4":"affected_company"}#line:428:}
    if OOOOOO00OO00O00O0 in O0OO00000O000OO0O :#line:430:if field in fields:
        OOOOOOOO0000O00OO =O0OO00000O000OO0O [OOOOOO00OO00O00O0 ]#line:431:field_name = fields[field]
        O000O0OOO0OO0O00O .execute (f"UPDATE vulnerable_domains SET {OOOOOOOO0000O00OO} = ? WHERE id = ?",(O00OO0OO0OO0000OO ,O0000OO0000O0OO00 ))#line:432:cursor.execute(f"UPDATE vulnerable_domains SET {field_name} = ? WHERE id = ?", (new_value, domain_id))
        OO0OO00OOO0O00O0O .commit ()#line:433:conn.commit()
        print ("Vulnerable domain details updated successfully.")#line:434:print("Vulnerable domain details updated successfully.")
    else :#line:435:else:
        print ("Invalid field number.")#line:436:print("Invalid field number.")
    OO0OO00OOO0O00O0O .close ()#line:438:conn.close()
def delete_vulnerable_domain ():#line:440:def delete_vulnerable_domain():
    O00OOOO0O0OO00O0O =connect_db ()#line:441:conn = connect_db()
    O0O0OO00OO0O0OO0O =O00OOOO0O0OO00O0O .cursor ()#line:442:cursor = conn.cursor()
    view_vulnerable_domains ()#line:444:view_vulnerable_domains()
    OO0000000O0O00O0O =q .text ("Enter the ID of the vulnerable domain you want to delete:").ask ()#line:445:domain_id = q.text("Enter the ID of the vulnerable domain you want to delete:").ask()
    O0O0OO00OO0O0OO0O .execute ("SELECT * FROM vulnerable_domains WHERE id = ?",(OO0000000O0O00O0O ,))#line:447:cursor.execute("SELECT * FROM vulnerable_domains WHERE id = ?", (domain_id,))
    OOOOOOOOOOO00OO0O =O0O0OO00OO0O0OO0O .fetchone ()#line:448:domain = cursor.fetchone()
    if not OOOOOOOOOOO00OO0O :#line:450:if not domain:
        print ("Vulnerable domain not found.")#line:451:print("Vulnerable domain not found.")
        O00OOOO0O0OO00O0O .close ()#line:452:conn.close()
        return #line:453:return
    O0O00O0OOOOOOOO00 =q .confirm (f"Do you want to delete the vulnerable domain '{OOOOOOOOOOO00OO0O[1]}'?").ask ()#line:455:confirm = q.confirm(f"Do you want to delete the vulnerable domain '{domain[1]}'?").ask()
    if O0O00O0OOOOOOOO00 :#line:456:if confirm:
        O0O0OO00OO0O0OO0O .execute ("DELETE FROM vulnerable_domains WHERE id = ?",(OO0000000O0O00O0O ,))#line:457:cursor.execute("DELETE FROM vulnerable_domains WHERE id = ?", (domain_id,))
        O00OOOO0O0OO00O0O .commit ()#line:458:conn.commit()
        print ("Vulnerable domain deleted successfully.")#line:459:print("Vulnerable domain deleted successfully.")
    else :#line:460:else:
        print ("Deletion cancelled.")#line:461:print("Deletion cancelled.")
    O00OOOO0O0OO00O0O .close ()#line:463:conn.close()
def view_vulnerable_domains ():#line:465:def view_vulnerable_domains():
    OO0O00O00O0000O0O =connect_db ()#line:466:conn = connect_db()
    OO0OO0OO0OOO0O0O0 =OO0O00O00O0000O0O .cursor ()#line:467:cursor = conn.cursor()
    OO0OO0OO0OOO0O0O0 .execute ("SELECT * FROM vulnerable_domains")#line:469:cursor.execute("SELECT * FROM vulnerable_domains")
    OO0OOOO0O0O000OO0 =OO0OO0OO0OOO0O0O0 .fetchall ()#line:470:domains = cursor.fetchall()
    if not OO0OOOO0O0O000OO0 :#line:472:if not domains:
        print ("No vulnerable domains found.")#line:473:print("No vulnerable domains found.")
    else :#line:474:else:
        O0OO0000000OO0O0O =["ID","Domain Name","Vulnerability Type","Risk Level","Affected Company"]#line:475:table_headers = ["ID", "Domain Name", "Vulnerability Type", "Risk Level", "Affected Company"]
        O000000O0O00O0O00 =[(OOO0O00OO0OOOO0O0 [0 ],OOO0O00OO0OOOO0O0 [1 ],OOO0O00OO0OOOO0O0 [2 ],OOO0O00OO0OOOO0O0 [3 ],OOO0O00OO0OOOO0O0 [4 ])for OOO0O00OO0OOOO0O0 in OO0OOOO0O0O000OO0 ]#line:476:table_data = [(domain[0], domain[1], domain[2], domain[3], domain[4]) for domain in domains]
        print (tabulate (O000000O0O00O0O00 ,headers =O0OO0000000OO0O0O ,tablefmt ="grid"))#line:477:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    OO0O00O00O0000O0O .close ()#line:479:conn.close()
def add_communist_agent (OO0OOOOO0O00OOO0O ,O0OOOOO00OO0OOO00 ,O0OO0OO0OOO0O0OO0 ,OOO0000OO0O00OOO0 ):#line:480:def add_communist_agent(name, country, communist_party, personal_info):
    OO0OOOOOOOOO000O0 =connect_db ()#line:481:conn = connect_db()
    OOO00OO0O0O0O00OO =OO0OOOOOOOOO000O0 .cursor ()#line:482:cursor = conn.cursor()
    OOO00OO0O0O0O00OO .execute ("INSERT INTO communist_agents (name, country, communist_party, personal_info) VALUES (?, ?, ?, ?)",(OO0OOOOO0O00OOO0O ,O0OOOOO00OO0OOO00 ,O0OO0OO0OOO0O0OO0 ,OOO0000OO0O00OOO0 ))#line:485:(name, country, communist_party, personal_info))
    OO0OOOOOOOOO000O0 .commit ()#line:487:conn.commit()
    print ("Communist agent added successfully.")#line:488:print("Communist agent added successfully.")
    OO0OOOOOOOOO000O0 .close ()#line:489:conn.close()
def edit_communist_agent ():#line:491:def edit_communist_agent():
    OO00OO0000O0O00O0 =connect_db ()#line:492:conn = connect_db()
    OO0O000O000OO0000 =OO00OO0000O0O00O0 .cursor ()#line:493:cursor = conn.cursor()
    view_communist_agents ()#line:495:view_communist_agents()
    OOOO00OOO0OO0O0OO =q .text ("Enter the ID of the communist agent you want to edit:").ask ()#line:496:agent_id = q.text("Enter the ID of the communist agent you want to edit:").ask()
    OO0O000O000OO0000 .execute ("SELECT * FROM communist_agents WHERE id = ?",(OOOO00OOO0OO0O0OO ,))#line:498:cursor.execute("SELECT * FROM communist_agents WHERE id = ?", (agent_id,))
    OO0O000O0O0000OO0 =OO0O000O000OO0000 .fetchone ()#line:499:agent = cursor.fetchone()
    if not OO0O000O0O0000OO0 :#line:501:if not agent:
        print ("Communist agent not found.")#line:502:print("Communist agent not found.")
        OO00OO0000O0O00O0 .close ()#line:503:conn.close()
        return #line:504:return
    print ("Communist agent details:")#line:506:print("Communist agent details:")
    print ("1. Name:",OO0O000O0O0000OO0 [1 ])#line:507:print("1. Name:", agent[1])
    print ("2. Country:",OO0O000O0O0000OO0 [2 ])#line:508:print("2. Country:", agent[2])
    print ("3. Communist Party:",OO0O000O0O0000OO0 [3 ])#line:509:print("3. Communist Party:", agent[3])
    print ("4. Personal Info:",OO0O000O0O0000OO0 [4 ])#line:510:print("4. Personal Info:", agent[4])
    OO0000OOOOO00O000 =q .text ("Enter the number of the field you want to edit:").ask ()#line:512:field = q.text("Enter the number of the field you want to edit:").ask()
    OO0O000OO0000OOOO =q .text ("Enter the new value:").ask ()#line:513:new_value = q.text("Enter the new value:").ask()
    OOO0O000O000O0OO0 ={"1":"name","2":"country","3":"communist_party","4":"personal_info"}#line:520:}
    if OO0000OOOOO00O000 in OOO0O000O000O0OO0 :#line:522:if field in fields:
        O000O0O0O0000O000 =OOO0O000O000O0OO0 [OO0000OOOOO00O000 ]#line:523:field_name = fields[field]
        OO0O000O000OO0000 .execute (f"UPDATE communist_agents SET {O000O0O0O0000O000} = ? WHERE id = ?",(OO0O000OO0000OOOO ,OOOO00OOO0OO0O0OO ))#line:524:cursor.execute(f"UPDATE communist_agents SET {field_name} = ? WHERE id = ?", (new_value, agent_id))
        OO00OO0000O0O00O0 .commit ()#line:525:conn.commit()
        print ("Communist agent details updated successfully.")#line:526:print("Communist agent details updated successfully.")
    else :#line:527:else:
        print ("Invalid field number.")#line:528:print("Invalid field number.")
    OO00OO0000O0O00O0 .close ()#line:530:conn.close()
def delete_communist_agent ():#line:532:def delete_communist_agent():
    O0O0OOO0000OO0O00 =connect_db ()#line:533:conn = connect_db()
    OO000OO0OO0000OO0 =O0O0OOO0000OO0O00 .cursor ()#line:534:cursor = conn.cursor()
    view_communist_agents ()#line:536:view_communist_agents()
    O00O0OOOO00O000OO =q .text ("Enter the ID of the communist agent you want to delete:").ask ()#line:537:agent_id = q.text("Enter the ID of the communist agent you want to delete:").ask()
    OO000OO0OO0000OO0 .execute ("SELECT * FROM communist_agents WHERE id = ?",(O00O0OOOO00O000OO ,))#line:539:cursor.execute("SELECT * FROM communist_agents WHERE id = ?", (agent_id,))
    OO0O00OO0O0OOOO0O =OO000OO0OO0000OO0 .fetchone ()#line:540:agent = cursor.fetchone()
    if not OO0O00OO0O0OOOO0O :#line:542:if not agent:
        print ("Communist agent not found.")#line:543:print("Communist agent not found.")
        O0O0OOO0000OO0O00 .close ()#line:544:conn.close()
        return #line:545:return
    O00OOO0O00O0OO0O0 =q .confirm (f"Do you want to delete the communist agent '{OO0O00OO0O0OOOO0O[1]}'?").ask ()#line:547:confirm = q.confirm(f"Do you want to delete the communist agent '{agent[1]}'?").ask()
    if O00OOO0O00O0OO0O0 :#line:548:if confirm:
        OO000OO0OO0000OO0 .execute ("DELETE FROM communist_agents WHERE id = ?",(O00O0OOOO00O000OO ,))#line:549:cursor.execute("DELETE FROM communist_agents WHERE id = ?", (agent_id,))
        O0O0OOO0000OO0O00 .commit ()#line:550:conn.commit()
        print ("Communist agent deleted successfully.")#line:551:print("Communist agent deleted successfully.")
    else :#line:552:else:
        print ("Deletion cancelled.")#line:553:print("Deletion cancelled.")
    O0O0OOO0000OO0O00 .close ()#line:555:conn.close()
def view_communist_agents ():#line:557:def view_communist_agents():
    OO0OOOO0OO0OO00OO =connect_db ()#line:558:conn = connect_db()
    O00O0OOO00O00O0OO =OO0OOOO0OO0OO00OO .cursor ()#line:559:cursor = conn.cursor()
    O00O0OOO00O00O0OO .execute ("SELECT * FROM communist_agents")#line:561:cursor.execute("SELECT * FROM communist_agents")
    OOOO0OO0OOO000O0O =O00O0OOO00O00O0OO .fetchall ()#line:562:agents = cursor.fetchall()
    if not OOOO0OO0OOO000O0O :#line:564:if not agents:
        print ("No communist agents found.")#line:565:print("No communist agents found.")
    else :#line:566:else:
        O0OOOOOOO00OOO00O =["ID","Name","Country","Communist Party","Personal Info"]#line:567:table_headers = ["ID", "Name", "Country", "Communist Party", "Personal Info"]
        O0O0O0OOO0O00OO00 =[(O0OO0O0O00O00000O [0 ],O0OO0O0O00O00000O [1 ],O0OO0O0O00O00000O [2 ],O0OO0O0O00O00000O [3 ],O0OO0O0O00O00000O [4 ])for O0OO0O0O00O00000O in OOOO0OO0OOO000O0O ]#line:568:table_data = [(agent[0], agent[1], agent[2], agent[3], agent[4]) for agent in agents]
        print (tabulate (O0O0O0OOO0O00OO00 ,headers =O0OOOOOOO00OOO00O ,tablefmt ="grid"))#line:569:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    OO0OOOO0OO0OO00OO .close ()#line:571:conn.close()
def add_shell (O0OO00O0O0000OO00 ,O0O00O0O0000OO0OO ,OOO0O000OOO0OOO00 ,O00OOOO0O0OOO0O0O ):#line:572:def add_shell(name, location, shell_type, capacity):
    O00000OO00OOOOO0O =connect_db ()#line:573:conn = connect_db()
    OOOO00O0O000000O0 =O00000OO00OOOOO0O .cursor ()#line:574:cursor = conn.cursor()
    OOOO00O0O000000O0 .execute ("INSERT INTO shells (name, location, type, capacity) VALUES (?, ?, ?, ?)",(O0OO00O0O0000OO00 ,O0O00O0O0000OO0OO ,OOO0O000OOO0OOO00 ,O00OOOO0O0OOO0O0O ))#line:577:(name, location, shell_type, capacity))
    O00000OO00OOOOO0O .commit ()#line:579:conn.commit()
    print ("Shell added successfully.")#line:580:print("Shell added successfully.")
    O00000OO00OOOOO0O .close ()#line:581:conn.close()
def edit_shell ():#line:583:def edit_shell():
    OO00O0O000O00O0O0 =connect_db ()#line:584:conn = connect_db()
    O0OOO000OOO0O0000 =OO00O0O000O00O0O0 .cursor ()#line:585:cursor = conn.cursor()
    view_shells ()#line:587:view_shells()
    OO000OO0OO00OO0OO =q .text ("Enter the ID of the shell you want to edit:").ask ()#line:588:shell_id = q.text("Enter the ID of the shell you want to edit:").ask()
    O0OOO000OOO0O0000 .execute ("SELECT * FROM shells WHERE id = ?",(OO000OO0OO00OO0OO ,))#line:590:cursor.execute("SELECT * FROM shells WHERE id = ?", (shell_id,))
    O0O0O000OO0OO0O0O =O0OOO000OOO0O0000 .fetchone ()#line:591:shell = cursor.fetchone()
    if not O0O0O000OO0OO0O0O :#line:593:if not shell:
        print ("Shell not found.")#line:594:print("Shell not found.")
        OO00O0O000O00O0O0 .close ()#line:595:conn.close()
        return #line:596:return
    print ("Shell details:")#line:598:print("Shell details:")
    print ("1. Name:",O0O0O000OO0OO0O0O [1 ])#line:599:print("1. Name:", shell[1])
    print ("2. Location:",O0O0O000OO0OO0O0O [2 ])#line:600:print("2. Location:", shell[2])
    print ("3. Type:",O0O0O000OO0OO0O0O [3 ])#line:601:print("3. Type:", shell[3])
    print ("4. Capacity:",O0O0O000OO0OO0O0O [4 ])#line:602:print("4. Capacity:", shell[4])
    O0000OO000O00OO00 =q .text ("Enter the number of the field you want to edit:").ask ()#line:604:field = q.text("Enter the number of the field you want to edit:").ask()
    O0O0OOO00OO0O000O =q .text ("Enter the new value:").ask ()#line:605:new_value = q.text("Enter the new value:").ask()
    O000OO0OO0O00OOOO ={"1":"name","2":"location","3":"type","4":"capacity"}#line:612:}
    if O0000OO000O00OO00 in O000OO0OO0O00OOOO :#line:614:if field in fields:
        O0O0O0OO0OOO0OOOO =O000OO0OO0O00OOOO [O0000OO000O00OO00 ]#line:615:field_name = fields[field]
        O0OOO000OOO0O0000 .execute (f"UPDATE shells SET {O0O0O0OO0OOO0OOOO} = ? WHERE id = ?",(O0O0OOO00OO0O000O ,OO000OO0OO00OO0OO ))#line:616:cursor.execute(f"UPDATE shells SET {field_name} = ? WHERE id = ?", (new_value, shell_id))
        OO00O0O000O00O0O0 .commit ()#line:617:conn.commit()
        print ("Shell details updated successfully.")#line:618:print("Shell details updated successfully.")
    else :#line:619:else:
        print ("Invalid field number.")#line:620:print("Invalid field number.")
    OO00O0O000O00O0O0 .close ()#line:622:conn.close()
def delete_shell ():#line:624:def delete_shell():
    O0000O00OO0OOOO0O =connect_db ()#line:625:conn = connect_db()
    OOO00OO000O00000O =O0000O00OO0OOOO0O .cursor ()#line:626:cursor = conn.cursor()
    view_shells ()#line:628:view_shells()
    OOO00O00O0000OO0O =q .text ("Enter the ID of the shell you want to delete:").ask ()#line:629:shell_id = q.text("Enter the ID of the shell you want to delete:").ask()
    OOO00OO000O00000O .execute ("SELECT * FROM shells WHERE id = ?",(OOO00O00O0000OO0O ,))#line:631:cursor.execute("SELECT * FROM shells WHERE id = ?", (shell_id,))
    OOOO0OOO0O00O0OO0 =OOO00OO000O00000O .fetchone ()#line:632:shell = cursor.fetchone()
    if not OOOO0OOO0O00O0OO0 :#line:634:if not shell:
        print ("Shell not found.")#line:635:print("Shell not found.")
        O0000O00OO0OOOO0O .close ()#line:636:conn.close()
        return #line:637:return
    O0000OO0O00O000OO =q .confirm (f"Do you want to delete the shell '{OOOO0OOO0O00O0OO0[1]}'?").ask ()#line:639:confirm = q.confirm(f"Do you want to delete the shell '{shell[1]}'?").ask()
    if O0000OO0O00O000OO :#line:640:if confirm:
        OOO00OO000O00000O .execute ("DELETE FROM shells WHERE id = ?",(OOO00O00O0000OO0O ,))#line:641:cursor.execute("DELETE FROM shells WHERE id = ?", (shell_id,))
        O0000O00OO0OOOO0O .commit ()#line:642:conn.commit()
        print ("Shell deleted successfully.")#line:643:print("Shell deleted successfully.")
    else :#line:644:else:
        print ("Deletion cancelled.")#line:645:print("Deletion cancelled.")
    O0000O00OO0OOOO0O .close ()#line:647:conn.close()
def view_shells ():#line:649:def view_shells():
    OO0000OOO000O00OO =connect_db ()#line:650:conn = connect_db()
    OOO0000OOO00000OO =OO0000OOO000O00OO .cursor ()#line:651:cursor = conn.cursor()
    OOO0000OOO00000OO .execute ("SELECT * FROM shells")#line:653:cursor.execute("SELECT * FROM shells")
    OOOOO00OOO0O0O00O =OOO0000OOO00000OO .fetchall ()#line:654:shells = cursor.fetchall()
    if not OOOOO00OOO0O0O00O :#line:656:if not shells:
        print ("No shells found.")#line:657:print("No shells found.")
    else :#line:658:else:
        O00OOO0OOO0O0O00O =["ID","Name","Location","Type","Capacity"]#line:659:table_headers = ["ID", "Name", "Location", "Type", "Capacity"]
        OOOOOOOO0O000OO00 =[(OO0000O00OOO0OOOO [0 ],OO0000O00OOO0OOOO [1 ],OO0000O00OOO0OOOO [2 ],OO0000O00OOO0OOOO [3 ],OO0000O00OOO0OOOO [4 ])for OO0000O00OOO0OOOO in OOOOO00OOO0O0O00O ]#line:660:table_data = [(shell[0], shell[1], shell[2], shell[3], shell[4]) for shell in shells]
        print (tabulate (OOOOOOOO0O000OO00 ,headers =O00OOO0OOO0O0O00O ,tablefmt ="grid"))#line:661:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    OO0000OOO000O00OO .close ()#line:663:conn.close()
def main_menu ():#line:664:def main_menu():
    while True :#line:665:while True:
        print ("""⠀
              ⣠⠴⠒⠋⠉⠉⠉⠉⠉⠙⠒⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⠀⣀⣀⣠⠤⠤⠤⠤⠤⣄⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡥⠴⠒⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⡀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣷⣤⣀⠈⡆⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣸⣿⣿⣶⣤⡀⠀⣴⣿⡟⢉⠀⠀⠀⠉⠀⢸⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⢀⣩⡛⢿⠉⡍⠛⣷⣾⣿⣷⢤⠴⠷⢄⣇⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⢰⣿⣿⣿⠇⠀⣷⠀⠉⠉⠉⠉⠀⠀⠀⠸⢿⠥⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢀⠀⢹⣦⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⢀⡀⢠⡀⢛⣁⣬⠆⠉⠉⣱⡿⡍⠀⢸⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⢺⣧⣀⣈⣿⣿⣿⣷⣤⣴⣶⡿⣻⠁⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡎⢿⠛⠛⠛⣿⣾⣏⣩⠍⠀⡸⠃⠀⣰⡧⠀#InterCuba.Net⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢮⡳⡌⠉⠻⣿⡿⠀⠀⠼⠁⢠⠞⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀_⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢄⠀⠀⣿⣿⠀⠀⢀⡜⠁⠚⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠈⠻⣗⠦⠽⠿⠤⠞⠁⠀⠀⠀⠀⣿⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⣇⠀⠀⠈⠳⢄⡀⠀⠀⠀⠀⠀⠀⢀⡟⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⡠⠤⠖⠒⠋⠉⡇⠀⠀⢹⡀⠀⠀⠀⠀⠙⠲⢤⡀⠀⢀⡴⠋⠀⢀⡇⠉⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⠤⠒⠋⠉⠀⠀⠀⠀⠀⠀⢰⣧⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⡹⠓⠋⠲⡄⠀⠈⣧⠀⠀⠸⡍⠙⠲⠤⣄⣀⠀⠀⠀⠀⠀
⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⠀⠀⠀⢻⡳⣄⠀⠀⠀⣠⠞⠀⠀⠀⠀⠘⣆⠀⣾⡄⠀⠀⠹⡄⠀⠀⠀⠈⠉⠒⢤⡀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡇⠀⠀⠀⠈⣇⠈⢣⡀⣰⢳⡀⠀⠀⠀⢀⡞⠉⠶⠁⢧⠀⠀⠀⢱⡀⠀⠀⠀⠀⠀⠀⢧⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⢸⡀⠀⠙⠇⠀⢹⠒⠒⠒⢯⠀⠀⠀⠀⢸⡀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠘⣆
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠸⠇⠀⠀⠀⠀⠟⠀⠀⠀⠈⠧⠀⠀⠀⠘⠇⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠻
▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║█
║▌│█║▌║▌║▌│█║▌║█Control Panel Main Menu║▌│█║▌║▌║▌│█║▌║█│█║▌
⠀⠀""")#line:690:⠀⠀""")
        print ("(aes) T-CIPHER Message Menu")#line:691:print("(aes) T-CIPHER Message Menu")
        print ("(1.) Target Companies")#line:692:print("(1.) Target Companies")
        print ("(2.) Target Agents")#line:693:print("(2.) Target Agents")
        print ("(3.) Vulnerable Domains")#line:694:print("(3.) Vulnerable Domains")
        print ("(4.) Communist Agents")#line:695:print("(4.) Communist Agents")
        print ("(5.) Manage Deployed Shells")#line:696:print("(5.) Manage Deployed Shells")
        print ("(6.) Manage Interesting Files")#line:697:print("(6.) Manage Interesting Files")
        print ("(7.) Manage Notes")#line:698:print("(7.) Manage Notes")
        print ("(8.) Export Report")#line:699:print("(8.) Export Report")
        print ("(0.) Exit\n")#line:700:print("(0.) Exit\n")
        OOO00OOO0OOO0O0O0 =q .text ("Enter your choice:").ask ()#line:701:choice = q.text("Enter your choice:").ask()
        if OOO00OOO0OOO0O0O0 =="1":#line:703:if choice == "1":
            target_companies_menu ()#line:704:target_companies_menu()
        elif OOO00OOO0OOO0O0O0 =="2":#line:705:elif choice == "2":
            target_agents_menu ()#line:706:target_agents_menu()
        elif OOO00OOO0OOO0O0O0 =="aes":#line:707:elif choice == "aes":
            aes_message_menu ()#line:708:aes_message_menu()
        elif OOO00OOO0OOO0O0O0 =="3":#line:709:elif choice == "3":
            vulnerable_domains_menu ()#line:710:vulnerable_domains_menu()
        elif OOO00OOO0OOO0O0O0 =="4":#line:711:elif choice == "4":
            communist_agents_menu ()#line:712:communist_agents_menu()
        elif OOO00OOO0OOO0O0O0 =="5":#line:713:elif choice == "5":
            shells_menu ()#line:714:shells_menu()
        elif OOO00OOO0OOO0O0O0 =="8":#line:715:elif choice == "8":
            export_report_menu ()#line:716:export_report_menu()
        elif OOO00OOO0OOO0O0O0 =="7":#line:717:elif choice == "7":
            take_notes_menu ()#line:718:take_notes_menu()
        elif OOO00OOO0OOO0O0O0 =="6":#line:719:elif choice == "6":
            manage_interesting_files_menu ()#line:720:manage_interesting_files_menu()
        elif OOO00OOO0OOO0O0O0 =="0":#line:721:elif choice == "0":
            sys .exit ()#line:722:sys.exit()
        else :#line:723:else:
            print ("Invalid choice. Please try again.")#line:724:print("Invalid choice. Please try again.")
def target_companies_menu ():#line:725:def target_companies_menu():
    while True :#line:726:while True:
        print ("\n---------- Target Companies Menu ----------")#line:727:print("\n---------- Target Companies Menu ----------")
        print ("1. Add Target Company")#line:728:print("1. Add Target Company")
        print ("2. Edit Target Company")#line:729:print("2. Edit Target Company")
        print ("3. Delete Target Company")#line:730:print("3. Delete Target Company")
        print ("4. View All Target Companies")#line:731:print("4. View All Target Companies")
        print ("0. Back to Main Menu")#line:732:print("0. Back to Main Menu")
        O0OO0O0OOO0OO0OO0 =q .text ("Enter your choice:").ask ()#line:733:choice = q.text("Enter your choice:").ask()
        if O0OO0O0OOO0OO0OO0 =="1":#line:735:if choice == "1":
            add_target_company_menu ()#line:736:add_target_company_menu()
        elif O0OO0O0OOO0OO0OO0 =="2":#line:737:elif choice == "2":
            edit_target_company ()#line:738:edit_target_company()
        elif O0OO0O0OOO0OO0OO0 =="3":#line:739:elif choice == "3":
            delete_target_company ()#line:740:delete_target_company()
        elif O0OO0O0OOO0OO0OO0 =="4":#line:741:elif choice == "4":
            view_target_companies ()#line:742:view_target_companies()
        elif O0OO0O0OOO0OO0OO0 =="0":#line:743:elif choice == "0":
            break #line:744:break
        else :#line:745:else:
            print ("Invalid choice. Please try again.")#line:746:print("Invalid choice. Please try again.")
def add_target_company_menu ():#line:748:def add_target_company_menu():
    print ("\n---------- Add Target Company ----------")#line:749:print("\n---------- Add Target Company ----------")
    O0O0000OO0O0000OO =q .text ("Company Name:").ask ()#line:750:company_name = q.text("Company Name:").ask()
    O00OOO00O0O0O0OOO =q .text ("Industry:").ask ()#line:751:industry = q.text("Industry:").ask()
    O0OOOOO00O0000OO0 =q .text ("Contact Info:").ask ()#line:752:contact_info = q.text("Contact Info:").ask()
    OO00O00O0OO0000O0 =q .text ("Description:").ask ()#line:753:description = q.text("Description:").ask()
    add_target_company (O0O0000OO0O0000OO ,O00OOO00O0O0O0OOO ,O0OOOOO00O0000OO0 ,OO00O00O0OO0000O0 )#line:755:add_target_company(company_name, industry, contact_info, description)
def target_agents_menu ():#line:757:def target_agents_menu():
    while True :#line:758:while True:
        print ("\n---------- Target Agents Menu ----------")#line:759:print("\n---------- Target Agents Menu ----------")
        print ("1. Add Target Agent")#line:760:print("1. Add Target Agent")
        print ("2. Edit Target Agent")#line:761:print("2. Edit Target Agent")
        print ("3. Delete Target Agent")#line:762:print("3. Delete Target Agent")
        print ("4. View All Target Agents")#line:763:print("4. View All Target Agents")
        print ("0. Back to Main Menu")#line:764:print("0. Back to Main Menu")
        OOO0OO000O0OO0O0O =q .text ("Enter your choice:").ask ()#line:765:choice = q.text("Enter your choice:").ask()
        if OOO0OO000O0OO0O0O =="1":#line:767:if choice == "1":
            add_target_agent_menu ()#line:768:add_target_agent_menu()
        elif OOO0OO000O0OO0O0O =="2":#line:769:elif choice == "2":
            edit_target_agent ()#line:770:edit_target_agent()
        elif OOO0OO000O0OO0O0O =="3":#line:771:elif choice == "3":
            delete_target_agent ()#line:772:delete_target_agent()
        elif OOO0OO000O0OO0O0O =="4":#line:773:elif choice == "4":
            view_target_agents ()#line:774:view_target_agents()
        elif OOO0OO000O0OO0O0O =="0":#line:775:elif choice == "0":
            break #line:776:break
        else :#line:777:else:
            print ("Invalid choice. Please try again.")#line:778:print("Invalid choice. Please try again.")
def add_target_agent_menu ():#line:779:def add_target_agent_menu():
    print ("\n---------- Add Target Agent ----------")#line:780:print("\n---------- Add Target Agent ----------")
    O0O0OO00O0OO00O0O =q .text ("Agent Name:").ask ()#line:781:agent_name = q.text("Agent Name:").ask()
    O0O0O00O0OOOOOOO0 =q .text ("Position:").ask ()#line:782:position = q.text("Position:").ask()
    OO0O0OO00O0O00OOO =q .text ("Contact Info:").ask ()#line:783:contact_info = q.text("Contact Info:").ask()
    O0O0O0O00OOOO0000 =q .text ("Assigned Company:").ask ()#line:784:assigned_company = q.text("Assigned Company:").ask()
    add_target_agent (O0O0OO00O0OO00O0O ,O0O0O00O0OOOOOOO0 ,OO0O0OO00O0O00OOO ,O0O0O0O00OOOO0000 )#line:786:add_target_agent(agent_name, position, contact_info, assigned_company)
def vulnerable_domains_menu ():#line:788:def vulnerable_domains_menu():
    while True :#line:789:while True:
        print ("\n---------- Vulnerable Domains Menu ----------")#line:790:print("\n---------- Vulnerable Domains Menu ----------")
        print ("1. Add Vulnerable Domain")#line:791:print("1. Add Vulnerable Domain")
        print ("2. Edit Vulnerable Domain")#line:792:print("2. Edit Vulnerable Domain")
        print ("3. Delete Vulnerable Domain")#line:793:print("3. Delete Vulnerable Domain")
        print ("4. View All Vulnerable Domains")#line:794:print("4. View All Vulnerable Domains")
        print ("0. Back to Main Menu")#line:795:print("0. Back to Main Menu")
        O00OOO000OO0OO0OO =q .text ("Enter your choice:").ask ()#line:796:choice = q.text("Enter your choice:").ask()
        if O00OOO000OO0OO0OO =="1":#line:798:if choice == "1":
            add_vulnerable_domain_menu ()#line:799:add_vulnerable_domain_menu()
        elif O00OOO000OO0OO0OO =="2":#line:800:elif choice == "2":
            edit_vulnerable_domain ()#line:801:edit_vulnerable_domain()
        elif O00OOO000OO0OO0OO =="3":#line:802:elif choice == "3":
            delete_vulnerable_domain ()#line:803:delete_vulnerable_domain()
        elif O00OOO000OO0OO0OO =="4":#line:804:elif choice == "4":
            view_vulnerable_domains ()#line:805:view_vulnerable_domains()
        elif O00OOO000OO0OO0OO =="0":#line:806:elif choice == "0":
            break #line:807:break
        else :#line:808:else:
            print ("Invalid choice. Please try again.")#line:809:print("Invalid choice. Please try again.")
def add_vulnerable_domain_menu ():#line:811:def add_vulnerable_domain_menu():
    print ("\n---------- Add Vulnerable Domain ----------")#line:812:print("\n---------- Add Vulnerable Domain ----------")
    O0OO0O0O0OO0OOO0O =q .text ("Domain Name:").ask ()#line:813:domain_name = q.text("Domain Name:").ask()
    OOO000OO00O0O0OO0 =q .text ("Vulnerability Type:").ask ()#line:814:vulnerability_type = q.text("Vulnerability Type:").ask()
    O0OOO000OO00OOO0O =q .text ("Risk Level:").ask ()#line:815:risk_level = q.text("Risk Level:").ask()
    O00OOOOOO0O000O00 =q .text ("Affected Company:").ask ()#line:816:affected_company = q.text("Affected Company:").ask()
    add_vulnerable_domain (O0OO0O0O0OO0OOO0O ,OOO000OO00O0O0OO0 ,O0OOO000OO00OOO0O ,O00OOOOOO0O000O00 )#line:818:add_vulnerable_domain(domain_name, vulnerability_type, risk_level, affected_company)
def communist_agents_menu ():#line:820:def communist_agents_menu():
    while True :#line:821:while True:
        print ("\n---------- Communist Agents Menu ----------")#line:822:print("\n---------- Communist Agents Menu ----------")
        print ("1. Add Communist Agent")#line:823:print("1. Add Communist Agent")
        print ("2. Edit Communist Agent")#line:824:print("2. Edit Communist Agent")
        print ("3. Delete Communist Agent")#line:825:print("3. Delete Communist Agent")
        print ("4. View All Communist Agents")#line:826:print("4. View All Communist Agents")
        print ("0. Back to Main Menu")#line:827:print("0. Back to Main Menu")
        OOOO0O000O0O00O0O =q .text ("Enter your choice:").ask ()#line:828:choice = q.text("Enter your choice:").ask()
        if OOOO0O000O0O00O0O =="1":#line:830:if choice == "1":
            add_communist_agent_menu ()#line:831:add_communist_agent_menu()
        elif OOOO0O000O0O00O0O =="2":#line:832:elif choice == "2":
            edit_communist_agent ()#line:833:edit_communist_agent()
        elif OOOO0O000O0O00O0O =="3":#line:834:elif choice == "3":
            delete_communist_agent ()#line:835:delete_communist_agent()
        elif OOOO0O000O0O00O0O =="4":#line:836:elif choice == "4":
            view_communist_agents ()#line:837:view_communist_agents()
        elif OOOO0O000O0O00O0O =="0":#line:838:elif choice == "0":
            break #line:839:break
        else :#line:840:else:
            print ("Invalid choice. Please try again.")#line:841:print("Invalid choice. Please try again.")
def add_communist_agent_menu ():#line:842:def add_communist_agent_menu():
    print ("\n---------- Add Communist Agent ----------")#line:843:print("\n---------- Add Communist Agent ----------")
    O00O00O0OOOO00000 =q .text ("Name:").ask ()#line:844:name = q.text("Name:").ask()
    OO0O000OOOOO00OOO =q .text ("Country:").ask ()#line:845:country = q.text("Country:").ask()
    OOO0O0OOOOO00OO0O =q .text ("Communist Party:").ask ()#line:846:communist_party = q.text("Communist Party:").ask()
    O0OOOO000O00OO000 =q .text ("Personal Info:").ask ()#line:847:personal_info = q.text("Personal Info:").ask()
    add_communist_agent (O00O00O0OOOO00000 ,OO0O000OOOOO00OOO ,OOO0O0OOOOO00OO0O ,O0OOOO000O00OO000 )#line:849:add_communist_agent(name, country, communist_party, personal_info)
def shells_menu ():#line:851:def shells_menu():
    while True :#line:852:while True:
        print ("\n---------- Shells Menu ----------")#line:853:print("\n---------- Shells Menu ----------")
        print ("1. Add Shell")#line:854:print("1. Add Shell")
        print ("2. Edit Shell")#line:855:print("2. Edit Shell")
        print ("3. Delete Shell")#line:856:print("3. Delete Shell")
        print ("4. View All Shells")#line:857:print("4. View All Shells")
        print ("0. Back to Main Menu")#line:858:print("0. Back to Main Menu")
        O000OO0O00OOO0O00 =q .text ("Enter your choice:").ask ()#line:859:choice = q.text("Enter your choice:").ask()
        if O000OO0O00OOO0O00 =="1":#line:861:if choice == "1":
            add_shell_menu ()#line:862:add_shell_menu()
        elif O000OO0O00OOO0O00 =="2":#line:863:elif choice == "2":
            edit_shell ()#line:864:edit_shell()
        elif O000OO0O00OOO0O00 =="3":#line:865:elif choice == "3":
            delete_shell ()#line:866:delete_shell()
        elif O000OO0O00OOO0O00 =="4":#line:867:elif choice == "4":
            view_shells ()#line:868:view_shells()
        elif O000OO0O00OOO0O00 =="0":#line:869:elif choice == "0":
            break #line:870:break
        else :#line:871:else:
            print ("Invalid choice. Please try again.")#line:872:print("Invalid choice. Please try again.")
def add_shell_menu ():#line:874:def add_shell_menu():
    print ("\n---------- Add Shell ----------")#line:875:print("\n---------- Add Shell ----------")
    O0O000OOO0OO0O00O =q .text ("Name:").ask ()#line:876:name = q.text("Name:").ask()
    OOOOO00O0OOOOOO00 =q .text ("Location:").ask ()#line:877:location = q.text("Location:").ask()
    OO00OOO0O00OOO0OO =q .text ("Type:").ask ()#line:878:shell_type = q.text("Type:").ask()
    O0OO0O0O00O0OOO00 =q .text ("Capacity:").ask ()#line:879:capacity = q.text("Capacity:").ask()
    add_shell (O0O000OOO0OO0O00O ,OOOOO00O0OOOOOO00 ,OO00OOO0O00OOO0OO ,O0OO0O0O00O0OOO00 )#line:881:add_shell(name, location, shell_type, capacity)
def export_report_menu ():#line:883:def export_report_menu():
    while True :#line:884:while True:
        print ("\n---------- Export Report Menu ----------")#line:885:print("\n---------- Export Report Menu ----------")
        print ("1. Export to Text File")#line:886:print("1. Export to Text File")
        print ("0. Back to Main Menu")#line:887:print("0. Back to Main Menu")
        O0OO000OO0OOOOOOO =q .text ("Enter your choice:").ask ()#line:888:choice = q.text("Enter your choice:").ask()
        if O0OO000OO0OOOOOOO =="1":#line:890:if choice == "1":
            export_to_text_file ()#line:891:export_to_text_file()
        elif O0OO000OO0OOOOOOO =="2":#line:892:elif choice == "2":
            export_to_html ()#line:893:export_to_html()
        elif O0OO000OO0OOOOOOO =="0":#line:894:elif choice == "0":
            break #line:895:break
        else :#line:896:else:
            print ("Invalid choice. Please try again.")#line:897:print("Invalid choice. Please try again.")
from tabulate import tabulate #line:899:from tabulate import tabulate
def export_to_text_file ():#line:901:def export_to_text_file():
    OOO00O0O0000000OO =q .text ("Enter the filename for the text report:").ask ()#line:902:filename = q.text("Enter the filename for the text report:").ask()
    with open (OOO00O0O0000000OO ,"w")as OOOO0OOOOO0OO00O0 :#line:904:with open(filename, "w") as file:
        OOOO0OOOOO0OO00O0 .write ("##########################################################\n")#line:905:file.write("##########################################################\n")
        OOOO0OOOOO0OO00O0 .write ("⢀⡠⣤⣶⣶⣦⣄⠀⠀OMEGA_7⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")#line:906:file.write("⢀⡠⣤⣶⣶⣦⣄⠀⠀OMEGA_7⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
        OOOO0OOOOO0OO00O0 .write ("⣿⡟⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⣠⣤⡄⠀⢀⣴⣶⡄\n")#line:907:file.write("⣿⡟⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⣠⣤⡄⠀⢀⣴⣶⡄\n")
        OOOO0OOOOO0OO00O0 .write ("⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣴⣿⣿⣿⣾⣿⣿⣿⡇\n")#line:908:file.write("⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣴⣿⣿⣿⣾⣿⣿⣿⡇\n")
        OOOO0OOOOO0OO00O0 .write ("⢿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁\n")#line:909:file.write("⢿⣇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁\n")
        OOOO0OOOOO0OO00O0 .write ("⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀\n")#line:910:file.write("⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀\n")
        OOOO0OOOOO0OO00O0 .write ("⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀\n")#line:911:file.write("⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀\n")
        OOOO0OOOOO0OO00O0 .write ("⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀\n")#line:912:file.write("⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀\n")
        OOOO0OOOOO0OO00O0 .write ("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀1976⠀⠀⠀⠀⠀⠀\n")#line:913:file.write("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀1976⠀⠀⠀⠀⠀⠀\n")
        OOOO0OOOOO0OO00O0 .write ("##########################################################\n\n")#line:914:file.write("##########################################################\n\n")
        OOOO0OOOOO0OO00O0 .write ("   *** C.I.T Control Panel Report - Classified ***\n\n")#line:915:file.write("   *** C.I.T Control Panel Report - Classified ***\n\n")
        OOOO0OOOOO0OO00O0 .write ("##########################################################\n\n")#line:916:file.write("##########################################################\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Target Companies ]===-----\n")#line:917:file.write("-----===[ Target Companies ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("target_companies"),headers =["ID","Company Name","Industry","Contact Info","Description"],tablefmt ="grid"))#line:918:file.write(tabulate(get_table_data("target_companies"), headers=["ID", "Company Name", "Industry", "Contact Info", "Description"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:919:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Target Agents ]===-----\n")#line:921:file.write("-----===[ Target Agents ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("target_agents"),headers =["ID","Agent Name","Position","Contact Info","Assigned Company"],tablefmt ="grid"))#line:922:file.write(tabulate(get_table_data("target_agents"), headers=["ID", "Agent Name", "Position", "Contact Info", "Assigned Company"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:923:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Vulnerable Domains ]===-----\n")#line:925:file.write("-----===[ Vulnerable Domains ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("vulnerable_domains"),headers =["ID","Domain Name","Vulnerability Type","Risk Level","Affected Company"],tablefmt ="grid"))#line:926:file.write(tabulate(get_table_data("vulnerable_domains"), headers=["ID", "Domain Name", "Vulnerability Type", "Risk Level", "Affected Company"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:927:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Communist Agents ]===-----\n")#line:929:file.write("-----===[ Communist Agents ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("communist_agents"),headers =["ID","Name","Country","Communist Party","Personal Info"],tablefmt ="grid"))#line:930:file.write(tabulate(get_table_data("communist_agents"), headers=["ID", "Name", "Country", "Communist Party", "Personal Info"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:931:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Shells ]===-----\n")#line:933:file.write("-----===[ Shells ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("shells"),headers =["ID","Name","Location","Type","Capacity"],tablefmt ="grid"))#line:934:file.write(tabulate(get_table_data("shells"), headers=["ID", "Name", "Location", "Type", "Capacity"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:935:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Notes ]===-----\n")#line:937:file.write("-----===[ Notes ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("notes"),headers =["ID","note_title","note_content"],tablefmt ="grid"))#line:938:file.write(tabulate(get_table_data("notes"), headers=["ID", "note_title", "note_content"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:939:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("-----===[ Interesting Files ]===-----\n")#line:941:file.write("-----===[ Interesting Files ]===-----\n")
        OOOO0OOOOO0OO00O0 .write (tabulate (get_table_data ("interesting_files"),headers =["ID","file_name","file_url"],tablefmt ="grid"))#line:942:file.write(tabulate(get_table_data("interesting_files"), headers=["ID", "file_name", "file_url"], tablefmt="grid"))
        OOOO0OOOOO0OO00O0 .write ("\n\n")#line:943:file.write("\n\n")
        OOOO0OOOOO0OO00O0 .write ("InterCuba.Net - Krintoxi\n")#line:944:file.write("InterCuba.Net - Krintoxi\n")
    print ("")#line:945:print("")
    print ("***********************************************************************************")#line:946:print("***********************************************************************************")
    print ("Report exported as a text file named : (",OOO00O0O0000000OO ,") Check The Toolkit Directory.")#line:947:print("Report exported as a text file named : (", filename,") Check The Toolkit Directory.")
    print ("***********************************************************************************")#line:948:print("***********************************************************************************")
def get_table_data (O0000OOOO00000O0O ):#line:951:def get_table_data(table_name):
    OOO00OOOOO0000OO0 =connect_db ()#line:952:conn = connect_db()
    O0O000000OO00O0OO =OOO00OOOOO0000OO0 .cursor ()#line:953:cursor = conn.cursor()
    O0O000000OO00O0OO .execute (f"SELECT * FROM {O0000OOOO00000O0O}")#line:954:cursor.execute(f"SELECT * FROM {table_name}")
    OO0OO000OOOO0O000 =O0O000000OO00O0OO .fetchall ()#line:955:data = cursor.fetchall()
    OOO00OOOOO0000OO0 .close ()#line:956:conn.close()
    return OO0OO000OOOO0O000 #line:957:return data
def take_notes_menu ():#line:959:def take_notes_menu():
    print ("\n---------- Notes Menu ----------")#line:960:print("\n---------- Notes Menu ----------")
    print ("1. Create Note")#line:961:print("1. Create Note")
    print ("2. Edit Note")#line:962:print("2. Edit Note")
    print ("3. Delete Note")#line:963:print("3. Delete Note")
    print ("4. View All Notes")#line:964:print("4. View All Notes")
    print ("0. Back to Main Menu")#line:965:print("0. Back to Main Menu")
    O000O00OOOO0OOOOO =q .text ("Enter your choice:").ask ()#line:966:choice = q.text("Enter your choice:").ask()
    if O000O00OOOO0OOOOO =="1":#line:968:if choice == "1":
        create_note ()#line:969:create_note()
    elif O000O00OOOO0OOOOO =="2":#line:970:elif choice == "2":
        edit_note ()#line:971:edit_note()
    elif O000O00OOOO0OOOOO =="3":#line:972:elif choice == "3":
        delete_note ()#line:973:delete_note()
    elif O000O00OOOO0OOOOO =="4":#line:974:elif choice == "4":
        view_notes ()#line:975:view_notes()
    elif O000O00OOOO0OOOOO =="0":#line:976:elif choice == "0":
        return #line:977:return
    else :#line:978:else:
        print ("Invalid choice. Please try again.")#line:979:print("Invalid choice. Please try again.")
def create_note ():#line:980:def create_note():
    O0O0OO00000O0OOOO =q .text ("Note Title:").ask ()#line:981:note_title = q.text("Note Title:").ask()
    O0OOO00O0000OO0OO =q .text ("Note Content:").ask ()#line:982:note_content = q.text("Note Content:").ask()
    O00000O000O0O0OO0 =connect_db ()#line:984:conn = connect_db()
    O0O00OO00OO0OOO00 =O00000O000O0O0OO0 .cursor ()#line:985:cursor = conn.cursor()
    O0O00OO00OO0OOO00 .execute ("INSERT INTO notes (note_title, note_content) VALUES (?, ?)",(O0O0OO00000O0OOOO ,O0OOO00O0000OO0OO ))#line:987:cursor.execute("INSERT INTO notes (note_title, note_content) VALUES (?, ?)", (note_title, note_content))
    O00000O000O0O0OO0 .commit ()#line:988:conn.commit()
    print ("Note created successfully.")#line:990:print("Note created successfully.")
    O00000O000O0O0OO0 .close ()#line:991:conn.close()
def edit_note ():#line:993:def edit_note():
    view_notes ()#line:994:view_notes()
    O00OO0O0O0O00OO00 =q .text ("Enter the ID of the note you want to edit:").ask ()#line:995:note_id = q.text("Enter the ID of the note you want to edit:").ask()
    OO00O00000OO0O00O =connect_db ()#line:997:conn = connect_db()
    O0O0O000OOO0OO000 =OO00O00000OO0O00O .cursor ()#line:998:cursor = conn.cursor()
    O0O0O000OOO0OO000 .execute ("SELECT * FROM notes WHERE id = ?",(O00OO0O0O0O00OO00 ,))#line:1000:cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    O00OO0000O0O0000O =O0O0O000OOO0OO000 .fetchone ()#line:1001:note = cursor.fetchone()
    if not O00OO0000O0O0000O :#line:1003:if not note:
        print ("Note not found.")#line:1004:print("Note not found.")
        OO00O00000OO0O00O .close ()#line:1005:conn.close()
        return #line:1006:return
    print ("Note details:")#line:1008:print("Note details:")
    print ("1. Note Title:",O00OO0000O0O0000O [1 ])#line:1009:print("1. Note Title:", note[1])
    print ("2. Note Content:",O00OO0000O0O0000O [2 ])#line:1010:print("2. Note Content:", note[2])
    O0OOO0OO0OO00OOOO =q .text ("Enter the number of the field you want to edit:").ask ()#line:1012:field = q.text("Enter the number of the field you want to edit:").ask()
    O0OOO000O000OO0OO =q .text ("Enter the new value:").ask ()#line:1013:new_value = q.text("Enter the new value:").ask()
    O00000O0OO0O00O00 ={"1":"note_title","2":"note_content"}#line:1018:}
    if O0OOO0OO0OO00OOOO in O00000O0OO0O00O00 :#line:1020:if field in fields:
        O00O00O0OO000OO0O =O00000O0OO0O00O00 [O0OOO0OO0OO00OOOO ]#line:1021:field_name = fields[field]
        O0O0O000OOO0OO000 .execute (f"UPDATE notes SET {O00O00O0OO000OO0O} = ? WHERE id = ?",(O0OOO000O000OO0OO ,O00OO0O0O0O00OO00 ))#line:1022:cursor.execute(f"UPDATE notes SET {field_name} = ? WHERE id = ?", (new_value, note_id))
        OO00O00000OO0O00O .commit ()#line:1023:conn.commit()
        print ("Note details updated successfully.")#line:1024:print("Note details updated successfully.")
    else :#line:1025:else:
        print ("Invalid field number.")#line:1026:print("Invalid field number.")
    OO00O00000OO0O00O .close ()#line:1028:conn.close()
def delete_note ():#line:1030:def delete_note():
    view_notes ()#line:1031:view_notes()
    OO0O0OOO0OO0OOO00 =q .text ("Enter the ID of the note you want to delete:").ask ()#line:1032:note_id = q.text("Enter the ID of the note you want to delete:").ask()
    OOOO000OOOO0OOOOO =connect_db ()#line:1034:conn = connect_db()
    OO000O0O00OO000O0 =OOOO000OOOO0OOOOO .cursor ()#line:1035:cursor = conn.cursor()
    OO000O0O00OO000O0 .execute ("SELECT * FROM notes WHERE id = ?",(OO0O0OOO0OO0OOO00 ,))#line:1037:cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    OOOOOOO0000OO0O0O =OO000O0O00OO000O0 .fetchone ()#line:1038:note = cursor.fetchone()
    if not OOOOOOO0000OO0O0O :#line:1040:if not note:
        print ("Note not found.")#line:1041:print("Note not found.")
        OOOO000OOOO0OOOOO .close ()#line:1042:conn.close()
        return #line:1043:return
    OOOOO00OO0000O0OO =q .confirm (f"Do you want to delete the note '{OOOOOOO0000OO0O0O[1]}'?").ask ()#line:1045:confirm = q.confirm(f"Do you want to delete the note '{note[1]}'?").ask()
    if OOOOO00OO0000O0OO :#line:1046:if confirm:
        OO000O0O00OO000O0 .execute ("DELETE FROM notes WHERE id = ?",(OO0O0OOO0OO0OOO00 ,))#line:1047:cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        OOOO000OOOO0OOOOO .commit ()#line:1048:conn.commit()
        print ("Note deleted successfully.")#line:1049:print("Note deleted successfully.")
    else :#line:1050:else:
        print ("Deletion cancelled.")#line:1051:print("Deletion cancelled.")
    OOOO000OOOO0OOOOO .close ()#line:1053:conn.close()
def view_notes ():#line:1055:def view_notes():
    O0OOOO0O0000O0O0O =connect_db ()#line:1056:conn = connect_db()
    OO0OO00OOO0O0O0OO =O0OOOO0O0000O0O0O .cursor ()#line:1057:cursor = conn.cursor()
    OO0OO00OOO0O0O0OO .execute ("SELECT * FROM notes")#line:1059:cursor.execute("SELECT * FROM notes")
    O0O0O00OO0O0OO00O =OO0OO00OOO0O0O0OO .fetchall ()#line:1060:notes = cursor.fetchall()
    if not O0O0O00OO0O0OO00O :#line:1062:if not notes:
        print ("No notes found.")#line:1063:print("No notes found.")
    else :#line:1064:else:
        O00OO0OOOO00O0O00 =["ID","Note Title","Note Content"]#line:1065:table_headers = ["ID", "Note Title", "Note Content"]
        OO00OO000OO0OO000 =[(O0OO0OOOO0O00OO0O [0 ],O0OO0OOOO0O00OO0O [1 ],O0OO0OOOO0O00OO0O [2 ])for O0OO0OOOO0O00OO0O in O0O0O00OO0O0OO00O ]#line:1066:table_data = [(note[0], note[1], note[2]) for note in notes]
        print (tabulate (OO00OO000OO0OO000 ,headers =O00OO0OOOO00O0O00 ,tablefmt ="grid"))#line:1067:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    O0OOOO0O0000O0O0O .close ()#line:1069:conn.close()
def manage_interesting_files_menu ():#line:1071:def manage_interesting_files_menu():
    print ("\n---------- Interesting Files Menu ----------")#line:1072:print("\n---------- Interesting Files Menu ----------")
    print ("1. Add Interesting File")#line:1073:print("1. Add Interesting File")
    print ("2. Edit Interesting File")#line:1074:print("2. Edit Interesting File")
    print ("3. Delete Interesting File")#line:1075:print("3. Delete Interesting File")
    print ("4. View All Interesting Files")#line:1076:print("4. View All Interesting Files")
    print ("0. Back to Main Menu")#line:1077:print("0. Back to Main Menu")
    O0OOO0OO00OOO0OOO =q .text ("Enter your choice:").ask ()#line:1078:choice = q.text("Enter your choice:").ask()
    if O0OOO0OO00OOO0OOO =="1":#line:1080:if choice == "1":
        add_interesting_file ()#line:1081:add_interesting_file()
    elif O0OOO0OO00OOO0OOO =="2":#line:1082:elif choice == "2":
        edit_interesting_file ()#line:1083:edit_interesting_file()
    elif O0OOO0OO00OOO0OOO =="3":#line:1084:elif choice == "3":
        delete_interesting_file ()#line:1085:delete_interesting_file()
    elif O0OOO0OO00OOO0OOO =="4":#line:1086:elif choice == "4":
        view_interesting_files ()#line:1087:view_interesting_files()
    elif O0OOO0OO00OOO0OOO =="0":#line:1088:elif choice == "0":
        return #line:1089:return
    else :#line:1090:else:
        print ("Invalid choice. Please try again.")#line:1091:print("Invalid choice. Please try again.")
def add_interesting_file ():#line:1092:def add_interesting_file():
    O00OO0O0000000OO0 =q .text ("File Name:").ask ()#line:1093:file_name = q.text("File Name:").ask()
    OO00000O00OOOO000 =q .text ("File URL:").ask ()#line:1094:file_url = q.text("File URL:").ask()
    OOO0O0O0O00OO0OOO =connect_db ()#line:1096:conn = connect_db()
    O0O00O0OO0O0OO0OO =OOO0O0O0O00OO0OOO .cursor ()#line:1097:cursor = conn.cursor()
    O0O00O0OO0O0OO0OO .execute ("INSERT INTO interesting_files (file_name, file_url) VALUES (?, ?)",(O00OO0O0000000OO0 ,OO00000O00OOOO000 ))#line:1099:cursor.execute("INSERT INTO interesting_files (file_name, file_url) VALUES (?, ?)", (file_name, file_url))
    OOO0O0O0O00OO0OOO .commit ()#line:1100:conn.commit()
    print ("Interesting file added successfully.")#line:1102:print("Interesting file added successfully.")
    OOO0O0O0O00OO0OOO .close ()#line:1103:conn.close()
def edit_interesting_file ():#line:1105:def edit_interesting_file():
    view_interesting_files ()#line:1106:view_interesting_files()
    OOOOO00OO0000OOO0 =q .text ("Enter the ID of the interesting file you want to edit:").ask ()#line:1107:file_id = q.text("Enter the ID of the interesting file you want to edit:").ask()
    O00O00OO0OO00000O =connect_db ()#line:1109:conn = connect_db()
    OOO00O00O0OO0OOOO =O00O00OO0OO00000O .cursor ()#line:1110:cursor = conn.cursor()
    OOO00O00O0OO0OOOO .execute ("SELECT * FROM interesting_files WHERE id = ?",(OOOOO00OO0000OOO0 ,))#line:1112:cursor.execute("SELECT * FROM interesting_files WHERE id = ?", (file_id,))
    O000O000OO0OO00OO =OOO00O00O0OO0OOOO .fetchone ()#line:1113:file = cursor.fetchone()
    if not O000O000OO0OO00OO :#line:1115:if not file:
        print ("Interesting file not found.")#line:1116:print("Interesting file not found.")
        O00O00OO0OO00000O .close ()#line:1117:conn.close()
        return #line:1118:return
    print ("Interesting file details:")#line:1120:print("Interesting file details:")
    print ("1. File Name:",O000O000OO0OO00OO [1 ])#line:1121:print("1. File Name:", file[1])
    print ("2. File URL:",O000O000OO0OO00OO [2 ])#line:1122:print("2. File URL:", file[2])
    O0O0OO0OO00OO0OOO =q .text ("Enter the number of the field you want to edit:").ask ()#line:1124:field = q.text("Enter the number of the field you want to edit:").ask()
    O00OOO00O0OO00OO0 =q .text ("Enter the new value:").ask ()#line:1125:new_value = q.text("Enter the new value:").ask()
    OO000OOO000000OOO ={"1":"file_name","2":"file_url"}#line:1130:}
    if O0O0OO0OO00OO0OOO in OO000OOO000000OOO :#line:1132:if field in fields:
        OO0OOOOOOO0O000O0 =OO000OOO000000OOO [O0O0OO0OO00OO0OOO ]#line:1133:field_name = fields[field]
        OOO00O00O0OO0OOOO .execute (f"UPDATE interesting_files SET {OO0OOOOOOO0O000O0} = ? WHERE id = ?",(O00OOO00O0OO00OO0 ,OOOOO00OO0000OOO0 ))#line:1134:cursor.execute(f"UPDATE interesting_files SET {field_name} = ? WHERE id = ?", (new_value, file_id))
        O00O00OO0OO00000O .commit ()#line:1135:conn.commit()
        print ("Interesting file details updated successfully.")#line:1136:print("Interesting file details updated successfully.")
    else :#line:1137:else:
        print ("Invalid field number.")#line:1138:print("Invalid field number.")
    O00O00OO0OO00000O .close ()#line:1140:conn.close()
def delete_interesting_file ():#line:1142:def delete_interesting_file():
    view_interesting_files ()#line:1143:view_interesting_files()
    O0OOOOO00O0OO0O00 =q .text ("Enter the ID of the interesting file you want to delete:").ask ()#line:1144:file_id = q.text("Enter the ID of the interesting file you want to delete:").ask()
    O0O0O000OO00O000O =connect_db ()#line:1146:conn = connect_db()
    OOOO0OOOOOO0OOOO0 =O0O0O000OO00O000O .cursor ()#line:1147:cursor = conn.cursor()
    OOOO0OOOOOO0OOOO0 .execute ("SELECT * FROM interesting_files WHERE id = ?",(O0OOOOO00O0OO0O00 ,))#line:1149:cursor.execute("SELECT * FROM interesting_files WHERE id = ?", (file_id,))
    O0OOOO0OOO0O0O000 =OOOO0OOOOOO0OOOO0 .fetchone ()#line:1150:file = cursor.fetchone()
    if not O0OOOO0OOO0O0O000 :#line:1152:if not file:
        print ("Interesting file not found.")#line:1153:print("Interesting file not found.")
        O0O0O000OO00O000O .close ()#line:1154:conn.close()
        return #line:1155:return
    OO00O0OOOO0OOO0OO =q .confirm (f"Do you want to delete the interesting file '{O0OOOO0OOO0O0O000[1]}'?").ask ()#line:1157:confirm = q.confirm(f"Do you want to delete the interesting file '{file[1]}'?").ask()
    if OO00O0OOOO0OOO0OO :#line:1158:if confirm:
        OOOO0OOOOOO0OOOO0 .execute ("DELETE FROM interesting_files WHERE id = ?",(O0OOOOO00O0OO0O00 ,))#line:1159:cursor.execute("DELETE FROM interesting_files WHERE id = ?", (file_id,))
        O0O0O000OO00O000O .commit ()#line:1160:conn.commit()
        print ("Interesting file deleted successfully.")#line:1161:print("Interesting file deleted successfully.")
    else :#line:1162:else:
        print ("Deletion cancelled.")#line:1163:print("Deletion cancelled.")
    O0O0O000OO00O000O .close ()#line:1165:conn.close()
def view_interesting_files ():#line:1167:def view_interesting_files():
    O0OO0000OO0OO0O0O =connect_db ()#line:1168:conn = connect_db()
    OO00O00000O0OOOOO =O0OO0000OO0OO0O0O .cursor ()#line:1169:cursor = conn.cursor()
    OO00O00000O0OOOOO .execute ("SELECT * FROM interesting_files")#line:1171:cursor.execute("SELECT * FROM interesting_files")
    O0000O000000O0OO0 =OO00O00000O0OOOOO .fetchall ()#line:1172:files = cursor.fetchall()
    if not O0000O000000O0OO0 :#line:1174:if not files:
        print ("No interesting files found.")#line:1175:print("No interesting files found.")
    else :#line:1176:else:
        O00O0O0O00OOO0O0O =["ID","File Name","File URL"]#line:1177:table_headers = ["ID", "File Name", "File URL"]
        O00OO0O0OO0O0O0O0 =[(OOOOOO0OOO0O0O000 [0 ],OOOOOO0OOO0O0O000 [1 ],OOOOOO0OOO0O0O000 [2 ])for OOOOOO0OOO0O0O000 in O0000O000000O0OO0 ]#line:1178:table_data = [(file[0], file[1], file[2]) for file in files]
        print (tabulate (O00OO0O0OO0O0O0O0 ,headers =O00O0O0O00OOO0O0O ,tablefmt ="grid"))#line:1179:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    O0OO0000OO0OO0O0O .close ()#line:1181:conn.close()
def connect_db ():#line:1183:def connect_db():
    OOOOO000OOOO00OOO =sqlite3 .connect ("control_panel.db")#line:1184:conn = sqlite3.connect("control_panel.db")
    return OOOOO000OOOO00OOO #line:1185:return conn
def add_aes_message (O000OO000OOOOO000 ,OO0OOO0OO00OOOO00 ,OOO00O0OO0OO0OOOO ):#line:1187:def add_aes_message(message, aes_key, creation_date):
    OOOO0OOO0OOOO00OO =connect_db ()#line:1188:conn = connect_db()
    O0O00OOO00OO00O00 =OOOO0OOO0OOOO00OO .cursor ()#line:1189:cursor = conn.cursor()
    O0O00OOO00OO00O00 .execute ("INSERT INTO aes_messages (message, aes_key, creation_date) VALUES (?, ?, ?)",(O000OO000OOOOO000 ,OO0OOO0OO00OOOO00 ,OOO00O0OO0OO0OOOO ))#line:1192:(message, aes_key, creation_date))
    OOOO0OOO0OOOO00OO .commit ()#line:1194:conn.commit()
    print ("AES message added successfully.")#line:1195:print("AES message added successfully.")
    OOOO0OOO0OOOO00OO .close ()#line:1196:conn.close()
def view_aes_messages ():#line:1198:def view_aes_messages():
    OOO0OOOOO0O0OO0O0 =connect_db ()#line:1199:conn = connect_db()
    O0OOOOOO0OO0O00OO =OOO0OOOOO0O0OO0O0 .cursor ()#line:1200:cursor = conn.cursor()
    O0OOOOOO0OO0O00OO .execute ("SELECT * FROM aes_messages")#line:1202:cursor.execute("SELECT * FROM aes_messages")
    O0O0O0O0O0O000O00 =O0OOOOOO0OO0O00OO .fetchall ()#line:1203:aes_messages = cursor.fetchall()
    if not O0O0O0O0O0O000O00 :#line:1205:if not aes_messages:
        print ("No AES messages found.")#line:1206:print("No AES messages found.")
    else :#line:1207:else:
        O0OO00O000O00O0O0 =["ID","Message","AES Key","Creation Date"]#line:1208:table_headers = ["ID", "Message", "AES Key", "Creation Date"]
        OOO00O0OO0O0O0OOO =[(OOOO0O00OO0OO0OO0 [0 ],OOOO0O00OO0OO0OO0 [1 ],OOOO0O00OO0OO0OO0 [2 ],OOOO0O00OO0OO0OO0 [3 ])for OOOO0O00OO0OO0OO0 in O0O0O0O0O0O000O00 ]#line:1209:table_data = [(msg[0], msg[1], msg[2], msg[3]) for msg in aes_messages]
        print (tabulate (OOO00O0OO0O0O0OOO ,headers =O0OO00O000O00O0O0 ,tablefmt ="grid"))#line:1210:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
def add_aes_message (O0O0O0O0OO0OOO0O0 ,O00OOOO0OOOO0O0O0 ,O000OOOOO00OO0O00 ,OO0O000OOO00OOOO0 ):#line:1212:def add_aes_message(message, aes_key, creation_date, conn):
    OO0OO0OOO00O00O0O =OO0O000OOO00OOOO0 .cursor ()#line:1213:cursor = conn.cursor()
    OO0OO0OOO00O00O0O .execute ("INSERT INTO aes_messages (message, aes_key, creation_date) VALUES (?, ?, ?)",(O0O0O0O0OO0OOO0O0 ,O00OOOO0OOOO0O0O0 ,O000OOOOO00OO0O00 ))#line:1215:cursor.execute("INSERT INTO aes_messages (message, aes_key, creation_date) VALUES (?, ?, ?)", (message, aes_key, creation_date))
    OO0O000OOO00OOOO0 .commit ()#line:1217:conn.commit()
    print ("AES message added successfully.")#line:1218:print("AES message added successfully.")
def add_aes_message_interactive (O0O0O00OOOOO00000 ):#line:1220:def add_aes_message_interactive(conn):
    OOOOO0OOOO0000OOO =q .text ("Enter the message:").ask ()#line:1221:message = q.text("Enter the message:").ask()
    O0O00O00O000OO0O0 =q .text ("Enter the AES key:").ask ()#line:1222:aes_key = q.text("Enter the AES key:").ask()
    O00O0O00000O00O0O =q .text ("Enter the creation date:").ask ()#line:1223:creation_date = q.text("Enter the creation date:").ask()
    add_aes_message (OOOOO0OOOO0000OOO ,O0O00O00O000OO0O0 ,O00O0O00000O00O0O ,O0O0O00OOOOO00000 )#line:1225:add_aes_message(message, aes_key, creation_date, conn)  # Pass the 'conn' variable to the 'add_aes_message' function
def view_aes_messages ():#line:1228:def view_aes_messages():
    OO0O000000OOOO00O =connect_db ()#line:1229:conn = connect_db()
    OO00000OOOO00OO00 =OO0O000000OOOO00O .cursor ()#line:1230:cursor = conn.cursor()
    OO00000OOOO00OO00 .execute ("SELECT * FROM aes_messages")#line:1232:cursor.execute("SELECT * FROM aes_messages")
    O000OO0O0O00OOOO0 =OO00000OOOO00OO00 .fetchall ()#line:1233:aes_messages = cursor.fetchall()
    if not O000OO0O0O00OOOO0 :#line:1235:if not aes_messages:
        print ("No AES messages found.")#line:1236:print("No AES messages found.")
    else :#line:1237:else:
        O00OOOOOOO000OOO0 =["ID","Message","AES Key","Creation Date"]#line:1238:table_headers = ["ID", "Message", "AES Key", "Creation Date"]
        O0O00000OOO0O000O =[(O000OOOOOOOOO0000 [0 ],O000OOOOOOOOO0000 [1 ],O000OOOOOOOOO0000 [2 ],O000OOOOOOOOO0000 [3 ])for O000OOOOOOOOO0000 in O000OO0O0O00OOOO0 ]#line:1239:table_data = [(msg[0], msg[1], msg[2], msg[3]) for msg in aes_messages]
        print (tabulate (O0O00000OOO0O000O ,headers =O00OOOOOOO000OOO0 ,tablefmt ="grid"))#line:1240:print(tabulate(table_data, headers=table_headers, tablefmt="grid"))
    OO0O000000OOOO00O .close ()#line:1242:conn.close()
def aes_message_menu ():#line:1244:def aes_message_menu():
    OOOO000O000OO0000 =connect_db ()#line:1245:conn = connect_db()  # Define the 'conn' variable here
    while True :#line:1247:while True:
        print ("\n***** AES Message Management *****")#line:1248:print("\n***** AES Message Management *****")
        print ("1. Add AES Message")#line:1249:print("1. Add AES Message")
        print ("2. View AES Messages")#line:1250:print("2. View AES Messages")
        print ("3. Back to Main Menu")#line:1251:print("3. Back to Main Menu")
        O0OOO0O0OO0OOO000 =q .text ("Enter your choice (#):").ask ()#line:1253:choice = q.text("Enter your choice (#):").ask()
        if O0OOO0O0OO0OOO000 =="1":#line:1255:if choice == "1":
            add_aes_message_interactive (OOOO000O000OO0000 )#line:1256:add_aes_message_interactive(conn)  # Pass the 'conn' variable to the interactive function
        elif O0OOO0O0OO0OOO000 =="2":#line:1257:elif choice == "2":
            view_aes_messages ()#line:1258:view_aes_messages()
        elif O0OOO0O0OO0OOO000 =="3":#line:1259:elif choice == "3":
            print ("Returning to the Main Menu.")#line:1260:print("Returning to the Main Menu.")
            OOOO000O000OO0000 .close ()#line:1261:conn.close()  # Close the database connection here
            break #line:1262:break
        else :#line:1263:else:
            print ("Invalid choice. Please select a valid option.")#line:1264:print("Invalid choice. Please select a valid option.")
if __name__ =="__main__":#line:1268:if __name__ == "__main__":
    create_tables ()#line:1269:create_tables()
    main_menu ()#line:1270:main_menu()
