import requests #line:1:import requests
from urllib .parse import urlparse ,urljoin #line:2:from urllib.parse import urlparse, urljoin
from PATH import paths as light_paths #line:3:from PATH import paths as light_paths
from DEEPPATH import paths as deep_paths #line:4:from DEEPPATH import paths as deep_paths
import sys #line:5:import sys
import logging #line:6:import logging
logging .basicConfig (level =logging .INFO ,format ='%(asctime)s - %(levelname)s - %(message)s',handlers =[logging .FileHandler ('admin_finder_log.txt'),logging .StreamHandler (sys .stdout )])#line:16:)
def normalize_url (OOOOO00OO00O0OOOO ):#line:18:def normalize_url(url):
    O0O0O000OOO00OO00 =urlparse (OOOOO00OO00O0OOOO )#line:19:parsed_url = urlparse(url)
    if not O0O0O000OOO00OO00 .scheme :#line:20:if not parsed_url.scheme:
        OOOOO00OO00O0OOOO ="http://"+OOOOO00OO00O0OOOO #line:21:url = "http://" + url
    return OOOOO00OO00O0OOOO #line:22:return url
def validate_url (OOOOOOOOOO00O00O0 ):#line:24:def validate_url(url):
    try :#line:25:try:
        O0O0O00OOOOO00O00 =requests .get (OOOOOOOOOO00O00O0 ,timeout =5 )#line:26:response = requests.get(url, timeout=5)
        return O0O0O00OOOOO00O00 .status_code ==200 #line:27:return response.status_code == 200
    except requests .exceptions .RequestException :#line:28:except requests.exceptions.RequestException:
        return False #line:29:return False
def check_admin_login (OOO00O00OOOO0O000 ,O00OOO0OOO000OOOO ):#line:31:def check_admin_login(url, admin_login_url):
    OO00000O0OO0O0000 =urljoin (OOO00O00OOOO0O000 ,O00OOO0OOO000OOOO )#line:32:full_url = urljoin(url, admin_login_url)
    if validate_url (OO00000O0OO0O0000 ):#line:33:if validate_url(full_url):
        return OO00000O0OO0O0000 #line:34:return full_url
def find_admin_logins (OOOO00OOOO0O0000O ,O00000O0OOO0OOO0O ):#line:36:def find_admin_logins(target_domain, scan_type):
    if O00000O0OOO0OOO0O =="Light Scan":#line:37:if scan_type == "Light Scan":
        OO0OO0O0OOO0O000O =light_paths #line:38:paths = light_paths
    elif O00000O0OOO0OOO0O =="Deep Scan":#line:39:elif scan_type == "Deep Scan":
        OO0OO0O0OOO0O000O =deep_paths #line:40:paths = deep_paths
    else :#line:41:else:
        logging .error ("Invalid scan type.")#line:42:logging.error("Invalid scan type.")
        return []#line:43:return []
    OO0OO0OO0000OOOO0 =[]#line:45:admin_logins = []
    OO0O00OOOOOO00O0O =len (OO0OO0O0OOO0O000O )#line:46:total_paths = len(paths)
    logging .info (f"""
░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░
░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░
░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░
░░░░░░▐▌░░░░▀▀███████▀
▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒
""")#line:53:""")
    logging .info (f"*************************")#line:54:logging.info(f"*************************")
    logging .info (f"Initiating {O00000O0OOO0OOO0O}...")#line:55:logging.info(f"Initiating {scan_type}...")
    logging .info (f"Target Domain: {OOOO00OOOO0O0000O}")#line:56:logging.info(f"Target Domain: {target_domain}")
    logging .info (f"Total Paths to Check: {OO0O00OOOOOO00O0O}")#line:57:logging.info(f"Total Paths to Check: {total_paths}")
    logging .info (f"*************************")#line:58:logging.info(f"*************************")
    for O0O00OO00O00O0OOO ,O00O000O0000O00O0 in enumerate (OO0OO0O0OOO0O000O ,1 ):#line:61:for index, path in enumerate(paths, 1):
        O00O0O000OOO00OOO =urljoin (OOOO00OOOO0O0000O ,O00O000O0000O00O0 )#line:62:admin_login_url = urljoin(target_domain, path)
        O0O000OOO000000O0 =f"[+] Checking Path [{O0O00OO00O00O0OOO}/{OO0O00OOOOOO00O0O}]:"#line:63:formatted_output = f"[+] Checking Path [{index}/{total_paths}]:"
        OO000O0000O0000O0 =f"    {O00O0O000OOO00OOO}"#line:64:formatted_url = f"    {admin_login_url}"
        logging .info (O0O000OOO000000O0 )#line:65:logging.info(formatted_output)
        logging .info (OO000O0000O0000O0 )#line:66:logging.info(formatted_url)
        O000O00O0OO000000 =check_admin_login (OOOO00OOOO0O0000O ,O00O0O000OOO00OOO )#line:67:result = check_admin_login(target_domain, admin_login_url)
        if O000O00O0OO000000 :#line:68:if result:
            OO0OO0OO0000OOOO0 .append (O000O00O0OO000000 )#line:69:admin_logins.append(result)
    return OO0OO0OO0000OOOO0 #line:71:return admin_logins
def main ():#line:73:def main():
    try :#line:74:try:
        print ("""
⠀⠀⠀⠀            ⠀⠀⢻⣼⡿⢀⣙⣀⡦⣤⣤⣀⠀⠈⠻⣿⣶⣶⣶⣿⠟⠁⠀⣀⣤⣶⢶⣄⣉⠀⢿⣧⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀           ⠀⠸⡿⠁⣹⣰⣿⣿⣿⣷⣿⣿⣦⣤⢼⡿⠿⣿⣧⣤⣴⣿⣿⣾⣿⣿⣿⡤⣍⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀          ⠀⢹⣄⠁⢿⡟⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⢻⡟⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀          ⠀⣸⣿⡆⠈⢷⣿⣿⣿⣿⣿⣿⠟⢹⣀⣀⣐⣟⣻⣿⣿⣿⣿⣿⣧⡾⠀⣰⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀          ⠀⠀⠀⠀⣾⡿⡿⣃⠀⣉⡛⠛⠻⢿⡿⣞⣵⡞⣻⣿⣜⣿⣮⡻⢿⡭⡟⢛⣛⣁⠀⣉⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀            ⠀⠀⠈⢷⣷⢭⣭⣈⣥⡶⠖⠀⠈⠛⣽⢻⣿⣿⣿⡘⣏⠋⠃⠀⠺⢶⣄⣩⣭⡵⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ,.     .             .-,--.             .-,--'        .         
   / |   ,-| ,-,-. . ,-.  '|__/ ,-. ,-. ,-.  \|__ . ,-. ,-| ,-. ,-. 
  /~~|-. | | | | | | | |  ,|    ,-| | | |-'   |   | | | | | |-' |   
,'   `-' `-^ ' ' ' ' ' '  `'    `-^ `-| `-'  `'   ' ' ' `-^ `-' '   
                                     ,|                                                                 `'                                                                                                                                                         ⠀⠀⠀⠀     """)#line:86:,|                                                                 `'                                                                                                                                                         ⠀⠀⠀⠀     """)
        print ("****************************************************************************")#line:88:print("****************************************************************************")
        print (" S.S.A Admin Page Finder ")#line:89:print(" S.S.A Admin Page Finder ")
        print ("****************************************************************************")#line:90:print("****************************************************************************")
        print (""" 
        if you pass "example.com" to this function, it will return "http://example.com." 
        If you pass "https://example.com," it will return "https://example.com." 
        This allows the script to handle both HTTP and HTTPS URLs correctly.\n""")#line:94:This allows the script to handle both HTTP and HTTPS URLs correctly.\n""")
        print ("****************************************************************************")#line:95:print("****************************************************************************")
        OO000OO000000O0O0 =input ("[+] Enter the target domain: ")#line:97:target_domain = input("[+] Enter the target domain: ")
        if not OO000OO000000O0O0 .startswith ("http://")and not OO000OO000000O0O0 .startswith ("https://"):#line:100:if not target_domain.startswith("http://") and not target_domain.startswith("https://"):
            OO000OO000000O0O0 ="http://"+OO000OO000000O0O0 #line:101:target_domain = "http://" + target_domain
        OO000OO000000O0O0 =normalize_url (OO000OO000000O0O0 )#line:104:target_domain = normalize_url(target_domain)
        if not validate_url (OO000OO000000O0O0 ):#line:105:if not validate_url(target_domain):
            logging .error ("Invalid target domain!")#line:106:logging.error("Invalid target domain!")
            return #line:107:return
        print ("\n[+] Scan Types:")#line:109:print("\n[+] Scan Types:")
        print ("*******************************")#line:110:print("*******************************")
        print ("1. Light Scan")#line:111:print("1. Light Scan")
        print ("2. Deep Scan")#line:112:print("2. Deep Scan")
        O0OOO0000OOOOOO00 =input ("\n[+] Choose a scan type (enter the number or scan type): ")#line:114:scan_choice = input("\n[+] Choose a scan type (enter the number or scan type): ")
        if O0OOO0000OOOOOO00 =="1"or O0OOO0000OOOOOO00 .lower ()=="light scan":#line:116:if scan_choice == "1" or scan_choice.lower() == "light scan":
            O0O0OO0O0O000O00O ="Light Scan"#line:117:scan_type = "Light Scan"
        elif O0OOO0000OOOOOO00 =="2"or O0OOO0000OOOOOO00 .lower ()=="deep scan":#line:118:elif scan_choice == "2" or scan_choice.lower() == "deep scan":
            O0O0OO0O0O000O00O ="Deep Scan"#line:119:scan_type = "Deep Scan"
        else :#line:120:else:
            print ("xxxxxxxxxxxxxxxxxxxxxxxx")#line:121:print("xxxxxxxxxxxxxxxxxxxxxxxx")
            print ("[-] Invalid scan choice.")#line:122:print("[-] Invalid scan choice.")
            print ("xxxxxxxxxxxxxxxxxxxxxxxx")#line:123:print("xxxxxxxxxxxxxxxxxxxxxxxx")
            return #line:124:return
        print ("\n[+] Scanning target domain: "+OO000OO000000O0O0 )#line:126:print("\n[+] Scanning target domain: " + target_domain)
        print ("[+] Scan Type: "+O0O0OO0O0O000O00O )#line:127:print("[+] Scan Type: " + scan_type)
        print ("****************************************************************************")#line:128:print("****************************************************************************")
        OO0O0O00OO000O0O0 =find_admin_logins (OO000OO000000O0O0 ,O0O0OO0O0O000O00O )#line:129:admin_logins = find_admin_logins(target_domain, scan_type)
        if OO0O0O00OO000O0O0 :#line:131:if admin_logins:
            print ("\n[+] Found "+str (len (OO0O0O00OO000O0O0 ))+" admin login page(s):")#line:132:print("\n[+] Found " + str(len(admin_logins)) + " admin login page(s):")
            for OOO0O0OO0O0OO0OOO ,OOOOOOO0O0O000O0O in enumerate (OO0O0O00OO000O0O0 ,1 ):#line:133:for index, login in enumerate(admin_logins, 1):
                print ("[+] "+OOOOOOO0O0O000O0O )#line:134:print("[+] " + login)
                logging .info ("Found admin login page: "+OOOOOOO0O0O000O0O )#line:135:logging.info("Found admin login page: " + login)
        else :#line:136:else:
            print ("***********************************************")#line:137:print("***********************************************")
            print ("\n[-] No admin login pages found.")#line:138:print("\n[-] No admin login pages found.")
            logging .info ("No admin login pages found.")#line:139:logging.info("No admin login pages found.")
            print ("***********************************************")#line:140:print("***********************************************")
    except KeyboardInterrupt :#line:141:except KeyboardInterrupt:
        print ("\n[-] Scan interrupted by the user. Exiting...")#line:142:print("\n[-] Scan interrupted by the user. Exiting...")
        logging .info ("Scan interrupted by the user. Exiting...")#line:143:logging.info("Scan interrupted by the user. Exiting...")
        sys .exit ()#line:144:sys.exit()
if __name__ =='__main__':#line:146:if __name__ == '__main__':
    main ()#line:147:main()

