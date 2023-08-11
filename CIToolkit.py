# -*- coding: utf-8 -*-
import os
if __name__ == "__main__":
    with open("scripts/PANEL/logos/mainlogo.txt", "r") as f:
        hacker_art = f.read()

    print("\033[32m" + hacker_art + "\033[0m")
#Start Of Authentication
import warnings
import getpass
import sys
from getpass import GetPassWarning
warnings.filterwarnings("ignore", category=GetPassWarning)
VALID_KEY = "FREECUBA"
def authenticate():
    print("C.I Tool-Kit Authentication")
    print("***************************")
    entered_key = getpass.getpass("Access Key: ")
    if entered_key == VALID_KEY:
        print("***************************")
        print("Authentication Successful!")
        print("********************************************************")
        print("Please run: (update) before the first command.(commands)")
        print("********************************************************")
    else:
        print("xxxxxxxxxxxxxxxxxxxxx")
        print("Access Denied!")
        print("xxxxxxxxxxxxxxxxxxxxx")
        print("Invalid key. You have been denied access to the C.I Tool-Kit.")
        sys.exit(0)
if __name__ == "__main__":
    authenticate()
#End Of Authentication      
def loopfunc():    
#START of options    
    choice = input("C.I Tool-Kit Command :")
    print ("*****************************")
#START of ADMIN PANEL FINDER    
    if choice == "apf":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
            cmd1 = os.system ("python3 scripts/APF/APF.py")
#END OF ADMIN PANEL FINDER

#START OF CALL FOR TERMINAL
    if choice == "terminal":
        cmd1 = os.system("sudo apt-get install xterm")
        cmd1 = os.system("xterm")
#END OF CALL FOR TERMINAL

    #Commands and help call
    if choice == "commands":
        print("Scanning modules...")
        cmd1 = os.system("python3 scripts/commands.py")
    if choice == "help":
        print("Scanning modules...")
        cmd1 = os.system("python3 scripts/commands.py")
    if choice == "Commands":
        print("Scanning modules...")
        cmd1 = os.system("python3 scripts/commands.py")
    if choice == "COMMANDS":
        print("Scanning modules...")
        cmd1 = os.system("python3 scripts/commands.py")
    if choice == "What can i do?":
        print("Scanning modules...")
        cmd1 = os.system("python3 scripts/commands.py")
    if choice == "what can i do?":
        print("Scanning modules...")
        cmd1 = os.system("python3 scripts/commands.py")
    if choice == "panel":
        print("Opening Control Panel...")
        cmd1 = os.system("python3 scripts/PANEL/setup.py")
        cmd1 = os.system("python3 scripts/PANEL/panel.py")
#END of commands and help call
    #START OF SYSTEM INFORMATION   
    if choice == "sys":
        print ("************************************************************************")
        print ("                        System Information:")
        print ("************************************************************************")
        cmd1 = os.system("                  lsb_release -a")
        print ("************************************************************************")
        #End System Information    

#---------------------Start of SQL Injection module call--------------------------------
    if choice == "sqli":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("*************************")
        print(" SQL Injector Module....")
        print("*************************")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("sudo apt-get install tor")
        cmd1 = os.system ("sudo service tor start")
        cmd1 = os.system ("sudo python2 scripts/sqli.pyc")
#----------------------End of SQL injection module call----------------------------------

    if choice == "vulscan":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
      
        print("The Toolkit Script requires Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("sudo python2 scripts/vulscan.py")

    #Start of Misc Options
    if choice == "itor":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("******************")
        print("Installing Tor....")
        print("******************")
        cmd1 = os.system ("sudo apt-get install tor")
        cmd1 = os.system ("sudo apt-get install proxychains")
        cmd1 = os.system ("sudo service tor start")
        
    if choice == "stor":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("****************")
        print("Starting Tor....")
        print("****************")
        cmd1 = os.system ("sudo service tor start")
        
    if choice == "tors":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("****************")
        print("Tor Status Check")
        print("****************")
        cmd1 = os.system ("sudo service tor status")
                
    if choice == "dvpn":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("*****************************************************")
        print("Downloading ans installing BitMask (RiseUp.Net) V.P.N")
        print("*****************************************************")
        cmd1 = os.system("echo 'deb http://deb.bitmask.net/debian wheezy main' | sudo tee -a /etc/apt/sources.list.d/bitmask.list")
        cmd1 = os.system("curl https://dl.bitmask.net/apt.key | sudo apt-key add -")
        cmd1 = os.system("sudo apt-get update")
        cmd1 = os.system("sudo apt-get install bitmask leap-keyring")

    if choice == "shells":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("*******************************************************")
        ooro = input("Obfuscated or Deobfuscated Shells?: ")
        print("*******************************************************")
        if ooro == "deobfuscated":
            print (ooro+" shell directory is: scripts/shells/Deobfuscated")
            print("***************************************************************")
            cmd1 = os.system("ls scripts/shells/Deobfuscated")
        if ooro == "obfuscated":
            print (ooro+" shell directory is: scripts/shells/Obfuscated")
            print("***************************************************************")
            cmd1 = os.system("ls scripts/shells/Obfuscated")
         
    if choice == "phptools":
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system("python2 scripts/phptools.py")

    if choice == "backdoorssh":
        print("************************************")
        print("Launching Deploy Script.. ")
        print("************************************")
        print("deploy a specific backdoor, such as a netcat backdoor or msfvenom backdoor")
        cmd1 = os.system ("sudo python scripts/sshbackdoors/dependencies.py")
        cmd1 = os.system ("sudo python scripts/sshbackdoors/master.py")

    if choice == "discover":
        print("*************************************")
        print("Launching Discover.... ")
        print("")
        cmd1 = os.system ("sudo apt-get install git")
        cmd1 = os.system ("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
        cmd1 = os.system ("cd /opt/discover/")
        cmd1 = os.system ("/opt/discover/./discover.sh")    

    if choice == "dinfo":
        print("***********************************************")
        print(" ##Launching Domain Whois Information Script## ")
        print("***********************************************")
        cmd1 = os.system ("python3 scripts/DNS/dns.py")

    if choice == "hash type" or choice == "hashtype" or choice == "tipo de hash":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("----------------------------------")
        print(" **Launching Hash Identify Script**")
        print("----------------------------------")
        cmd1 = os.system ("python3 scripts/HashID/HID.py")

    if choice == "numconverter":
        print("----------------------------------")
        print(" **Launching Converter Script**")
        print("----------------------------------")
        cmd1 = os.system ("python scripts/NumberConverter.pyc")

    if choice == "hexconv" or choice == "hex converter" or choice == "hex conv" or choice == "convertidor de hex":
        if __name__ == "__main__":
            with open("scripts/PANEL/logos/CIT.txt", "r") as f:
                hacker_art = f.read()

            print("\033[32m" + hacker_art + "\033[0m")
        print("----------------------------------------")
        print(" * * *Launching Converter Script * * * ")
        print("----------------------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 scripts/hex_converter.pyc")
    
    if choice == "update":
        print("----------------------------------")
        print("  * * * UPDATING THE SYSTEM * * * ")
        print("----------------------------------")
        cmd1 = os.system ("sudo apt-get update")
        cmd1 = os.system ("sudo apt-get upgrade")
        cmd1 = os.system ("sudo apt-get dist-upgrade")
        cmd1 = os.system ("sudo apt-get install python")
        cmd1 = os.system ("sudo apt-get install python3")
        cmd1 = os.system ("sudo apt-get install python3-pip")
        cmd1 = os.system ("sudo apt-get install python2")

    if choice == "converters":
        print("----------------------------------")
        print("**Launching Binary Converter Website**")
        print("----------------------------------")
        cmd1 = os.system ("sudo apt-get install iceweasel")
        cmd1 = os.system ("iceweasel http://www.exploringbinary.com/converters-and-calculators/")
        cmd1 = os.system ("firefox http://www.exploringbinary.com/converters-and-calculators/")

    if choice == "aconv":
        print("----------------------------------")
        print(" **Launching ASCII Converter Website** ")
        print("----------------------------------")
        cmd1 = os.system ("iceweasel https://www.branah.com/ascii-converter")
		
#OSINT call start 
    if choice == "osint":
        print("----------------------------------")
        print(" **Launching OSCARF OSINT Script**")
        print("----------------------------------")
        cmd1 = os.system("sudo python2 scripts/OSCAR/DEPENDENCY_CHECK.py")
        cmd1 = os.system("sudo pip install -r scripts/OSCAR/requirements.txt")
        cmd1 = os.system ("sudo apt-get install python-dev")
        print("Done Checking For Updates!")
        cmd1 = os.system ("sudo python2 scripts/OSCAR/OSCARf.py")
#OSINT call end

    if choice == "steghide":
        print("----------------------------------")
        print("   **Launching Steghide GUI      **")
        print("----------------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python tools/pySteg/pysteg.py")

    if choice == "ddos":
        cmd1 = os.system ("python3 scripts/DDOS/ddos.py")
    if choice == "tsqli":
        cmd1 = os.system ("python3 scripts/TSQLI/TSQLI.py")

    if choice == "encdns":
        print("---------------------------------------")
        print("Launching DNS Encryption Install!.....")
        print("---------------------------------------")    
        cmd1 = os.system ("git clone git://github.com/simonclausen/dnscrypt-autoinstall.git kitdns/")
        cmd1 = os.system ("sh /kitdns/dnscrypt-autoinstall.sh")

    if choice == "stegattack":
        print("-------------------------------------")
        print("        Steghide Attacker")
        print("-------------------------------------")
        print("@In order to use this script , you must call: ")
        print("# pyhon scripts/steghidecracker.py [stegfile] [wordlist]")
        cmd1 = os.system ("sudo apt-get install xterm")
        cmd1 = os.system ("xterm echo ")    

    if choice == "clear":
        cmd1 = os.system ("clear")
        print("--------------")
        print("Fresh Terminal")
        print("--------------")

    if choice == "home":
        cmd1 = os.system ("python3 CIToolkit.py")

    if choice == "uihanalysis":
        print("---------------------------")
        print("Launching Analysis Script...")
        print("---------------------------")
        uihtarget = input ("Url , Hash Or IP for Analysis: ")
        cmd1 = os.system ("automater -b "+uihtarget +" -w uihresult.html")           

    if choice == "exit" or choice == "quit" or choice == "q":
        sys.exit()

    if choice == "toolbox":
        print("""
        ####################
        Launching ToolBox...
        ####################
        """)
        print("This Toolbox has some requirements , if you think you have them, continue.")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 scripts/toolbox.py")
    
    if choice == "spoof my mac":
        print("""***********************
        Launching Mac Spoofing Script...
        ********************************
        """)
        cmd1 = os.system ("python3 scripts/macspoof.py")
    #IMAGE MATADATE
    if choice == "exif":
        print("----------------------------------------------")
        print("Launching IMAGE METADATA EXTRACTOR AND REMOVER")
        print("----------------------------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ('sudo apt-get install libimage-exiftool-perl')
        cmd1 = os.system ('python2 scripts/exifpwn.pyc')
        print("Launched!")
    #Start Of Local Port Scan
    if choice =="localports":
        cmd1 = os.system ("python3 scripts/portscanLOCAL.py")
    #End Of Local Port Scan
    if choice == "portscan":
        cmd1 = os.system("python3 scripts/portscanNET.py")    
    if choice == "sqlscan":
        print("-----------------------------------------")
        print("Example: http://target.net/index.php?id=1")
        sqltarget = input('Target Domain: ')
        cmd1 = os.system('python scripts/sqlscan.py -u '+sqltarget)
    if choice == "anonsearch":
        cmd1 = os.system('sudo apt-get install proxychains')
        cmd1 = os.system("sudo apt-get install tor")
        cmd1 = os.system("sudo service tor start")
        cmd1 = os.system("sudo service tor status")
        cmd1 = os.system("sudo apt-get install firefox")
        print("----------------------")
        asearch = input('Anonymous Web Search: ')
        cmd1 = os.system("proxychains firefox https://duckduckgo.com/?q="+asearch)
    if choice == "noobpasswd":
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system("python2 scripts/noobcrack.py")
     #EASTEREGGS   
    if choice == "wle":
        print ("-----------------------------")
        email_db = input("Podesta or DNC?:")
        cmd1 = os.system("python scripts/WikileaksEmailDownloader.py --start 1 --end  -1 --retries 5 "+email_db)
    if choice == "vpn":
        print("Starting VPN (BITMASK)")
        cmd1 = os.system ("sh tools/vpn/./bitmask")
        cmd1 = os.system ("bitmask")
    #Testing Toxic Crawler
    if choice == "toxicdork":
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 scripts/Tox1cDorkeR.py")
	#if choice == "tcrawl":
	#	print("Starting Toxic Crawler")
	#	cmd1 = os.system ("python IN DEVELOPMENT SCRIPTS/ToxicCrawler/ToxicCrawler.py")
loopfunc()
loopfunc()


