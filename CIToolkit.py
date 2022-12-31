#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import getpass
#import argparse
#import time
#import http.client
#import subprocess
#print ("--------------------------------------------------------")
#from time import sleep
#lines = ["C.I-Tool-Kit is for educational research only!"]
#for line in lines:          # for each line of text (or each message)
#    for c in line:          # for each character in each line
 #       print(c, end='')    # print a single character, and keep the cursor there.
  #      sys.stdout.flush()  # flush the buffer
   #     sleep(0.1)          # wait a little to make the effect look good.
    #print('') 
    #print("-------------------------------------------------------")

print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣶⣶⣶⣾⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⠿⠿⠛⠛⠛⠋⠉⠉⠁⠀⠀⠈⠛⠿⢿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣶⡄⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇ 75 ⣿⡇⠀⠀⠈⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀x⢀⣿⠇⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣶⠿⠋⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠃⠀⠀⠀⠀⢀⣴⣿⣥⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢀⣴⣿⣋⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣽⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣶⣤⣶⠿⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀o⠀⠀⠀⠀⢀⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀o⠀⠀⠀⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠀#SOSCUBA⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣾⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⠿⣿⡏⠉⠀⠈⠛⢿⣶⣤⣄⣀⣀⣤⣴⣶⠟⠋⠀⠉⠙⢻⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⠿⠟⠛⣿⡆⠀⠘⣿⡄⠀⠀⠀⣠⣾⠟⢉⣿⣯⠙⢿⣦⣄⠀⠀⠀⢀⣾⠏⠀⢨⣿⠛⠻⢿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣴⣾⣿⣿⠿⠟⠋⠉⠀⠀⠀⣀⣼⣿⠄⠀⠙⣿⡀⢀⣼⡟⠁⠀⣸⡟⢻⣆⠀⠈⢿⣇⠀⢀⣾⠏⠀⢠⣾⣇⡀⠀⠀⠀⠉⠙⠻⠿⣿⣿⣶⣦⣄⡀⠀⠀⠀
⠀⠀⢠⣿⣿⠟⠋⢻⣧⠀⣀⣠⣴⡾⠟⠛⠉⠀⠀⠀⠀⠹⣿⣸⡿⣷⡄⣰⡿⠀⠘⣿⡆⢀⣾⢿⣄⣾⠏⠀⠀⠀⠈⠛⠻⠿⣦⣤⣀⡀⠀⠀⣼⡟⠛⠻⣿⣷⠀⠀⠀
⠀⠀⣼⣿⡇⠀⠀⠈⢿⡷⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠃⠘⢿⣿⠃⠀⠀⠘⣿⡿⠃⠘⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⢶⣶⡿⠁⠀⠀⢻⣿⣧⠀⠀
⠀⢀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣧⡀⢀⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠈⣿⣿⠀⠀
⠀⢸⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡿⠋⠀⠀⢀⡀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀
⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢸⡟⠛k⢻r⠛i⠛n⠛t⣿ox⢻i⣯⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀
⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀xxxxx⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠸⠿⠾⠷⠾⠿⠾⠿⠷⠿⠿⠿⠿⠾⠟⠿⠿⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀
⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀xxxxxxxxxxx⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀
⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀
⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
""")
lines = ["""
╔═╗┌─┐┬ ┬┌┐┌┌┬┐┌─┐┬─┐  ╦┌┐┌┌┬┐┌─┐┬  ┬  ┬┌─┐┌─┐┌┐┌┌─┐┌─┐  ╔╦╗┌─┐┌─┐┬  ┬┌─┬┌┬┐   
║  │ ││ ││││ │ ├┤ ├┬┘  ║│││ │ ├┤ │  │  ││ ┬├┤ ││││  ├┤    ║ │ ││ ││  ├┴┐│ │     
╚═╝└─┘└─┘┘└┘ ┴ └─┘┴└─  ╩┘└┘ ┴ └─┘┴─┘┴─┘┴└─┘└─┘┘└┘└─┘└─┘   ╩ └─┘└─┘┴─┘┴ ┴┴ ┴  
"""]              

from time import sleep
import sys

for line in lines:          # for each line of text (or each message)
    for c in line:          # for each character in each line
        print(c, end='')    # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.006)          # wait a little to make the effect look good.
    print('')               # line break (optional, could also be part of the message)
#End Of Title Area  
#Start Of Authentication
#key = "25" #User Authentication Key
#print ("*********************************")
#kitkey = getpass.getpass("C.I Tool-Kit access key : ")# Verify Key
#print ("*********************************")

#if kitkey == key:
#    print("")
#    print ("*****************************")
#    print ("Authentication Successful!") #SuccessFul Authentication
#    #print ("*****************************")
#    print ("please run: (update) before first command.")

#else:
#    print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#    print("Wrong Key! YOU HAVE BEEN BOOTED OFF ") #Wrong Key Warrning
#    print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#    print ("-Krintoxi")
#    sys.exit(0) #Exists Tool-Kit if Authentication Key is Wrong
#End Of Authentication      
def loopfunc():    
#START of options    
    choice = input("C.I Tool-Kit Command :")
    print ("*****************************")



#START of ADMIN PANEL FINDER    
    if choice == "apf":
            print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        ****************************
            Admin Panel Module
        ****************************
        """)
            cmd1 = os.system ("perl scripts/finder.pl")
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
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
        print("-------------------------")
        print(" SQL Injector Module....")
        print("-------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("sudo apt-get install tor")
        cmd1 = os.system ("sudo service tor start")
        cmd1 = os.system ("sudo python2 scripts/sqli.pyc")
#----------------------End of SQL injection module call----------------------------------



        
    if choice == "vulscan":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
      
        print("The Toolkit Script requires Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("sudo python2 scripts/vulscan.py")

    #Start of Misc Options
    if choice == "itor":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
        print("******************")
        print("Installing Tor....")
        print("******************")
        cmd1 = os.system ("sudo apt-get install tor")
        cmd1 = os.system ("sudo apt-get install proxychains")
        cmd1 = os.system ("sudo service tor start")
        
    if choice == "stor":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
        print("****************")
        print("Starting Tor....")
        print("****************")
        cmd1 = os.system ("sudo service tor start")
        
    if choice == "tors":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
        print("****************")
        print("Tor Status Check")
        print("****************")
        cmd1 = os.system ("sudo service tor status")
                
    if choice == "dvpn":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
        print ("*****************************************************")
        print ("Downloading ans installing BitMask (RiseUp.Net) V.P.N")
        print ("*****************************************************") 
        cmd1 = os.system ("echo 'deb http://deb.bitmask.net/debian wheezy main' | sudo tee -a /etc/apt/sources.list.d/bitmask.list")    
        cmd1 = os.system ("curl https://dl.bitmask.net/apt.key | sudo apt-key add -")
        cmd1 = os.system ("sudo apt-get update")
        cmd1 = os.system ("sudo apt-get install bitmask leap-keyring")


    if choice == "shells":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
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
        print("-------------------------------------")
        print("Launching Deploy Script.. ")
        print("-------------------------------------")
        print("deploy a specific backdoor, such as a netcat backdoor or msfvenom backdoor")
        cmd1 = os.system ("sudo python scripts/sshbackdoors/dependencies.py")
        cmd1 = os.system ("sudo python scripts/sshbackdoors/master.py")

    if choice == "discover":
        print("-------------------------------------")
        print("Launching Discover.... ")
        print("-------------------------------------")
        cmd1 = os.system ("sudo apt-get install git")
        cmd1 = os.system ("sudo git clone git://github.com/leebaird/discover.git /opt/discover/")
        cmd1 = os.system ("cd /opt/discover/")
        cmd1 = os.system ("/opt/discover/./discover.sh")    
            

    if choice == "dinfo":
        print("-------------------------------------")
        print(" ##Launching NSlookup Script## ")
        print("-------------------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 scripts/dns.py")

    if choice == "hash type" or choice == "hashtype" or choice == "tipo de hash":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
        """)
        print("----------------------------------")
        print(" **Launching Hash Identify Script**")
        print("----------------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 scripts/Hash_ID.pyc")

    if choice == "numconverter":
        print("----------------------------------")
        print(" **Launching Converter Script**")
        print("----------------------------------")
        cmd1 = os.system ("python scripts/NumberConverter.pyc")

    if choice == "hexconv" or choice == "hex converter" or choice == "hex conv" or choice == "convertidor de hex":
        print("""
                ________/\\\\\\\\\________/\\\\\\\\\\\________/\\\\\\\\\\\\\\\_        
 _____/\\\////////________\/////\\\///________\///////\\\/////__       
  ___/\\\/_____________________\/\\\_________________\/\\\_______      
   __/\\\_______________________\/\\\_________________\/\\\_______     
    _\/\\\_______________________\/\\\_________________\/\\\_______    
     _\//\\\______________________\/\\\_________________\/\\\_______   
      __\///\\\____________________\/\\\_________________\/\\\_______  
       ____\////\\\\\\\\\__/\\\__/\\\\\\\\\\\__/\\\_______\/\\\_______ 
        _______\/////////__\///__\///////////__\///________\///________
                        Counter Intelligence Toolkit
                        """)
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
        print("       **Launching Steghide GUI**")
        print("----------------------------------")
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 tools/pySteg/pysteg.py")

    if choice == "dping":
        print("----------------------------------")
        print("     Launching DOS/PING Script     ")
        print("----------------------------------")
        tar = input('Target link #Include http://# : ')
        cmd1 = os.system ("python scripts/dping.pyc -c 10 -t 1000 "+tar )

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
        print("Finished!") 
    
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

    if choice =="localports":
        cmd1 = os.system ("python3 scripts/portscanLOCAL.py")
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
        cmd1 = os.systen ("sh tools/vpn/./bitmask")
        cmd1 = os.system ("bitmask")

    #Testing Toxic Crawler
    if choice == "toxicdork":
        print("The Toolkit Script requires Tor and Python2.")
        print("Please follow the on screen install.")
        cmd1 = os.system ("sudo apt-get install python2")
        cmd1 = os.system ("python2 scripts/Tox1cDorkeR.py")



    #        
	#if choice == "tcrawl":
	#	print("Starting Toxic Crawler")
	#	cmd1 = os.system ("python IN DEVELOPMENT SCRIPTS/ToxicCrawler/ToxicCrawler.py")
loopfunc()
loopfunc()


