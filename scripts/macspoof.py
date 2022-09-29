import os
def loopfunc():
	print ("****************")
	print ("")
	print ("1.(install) - Will make sure your system can SPOOF MAC ADDRESS with a random one.")
	print ("")
	print ("2.(macspoof on)- will turn ON MAC ADDRESS spoofing for WIFI and Ethernet interfaces")
	print ()
	print ("3.(macspoof off) will turn OFF MAC ADDRESS spoofing for WIFI and Ethernet interfaces")
	print ("")
	print ("****************")
	command = input("Command:")
	print ("****************")
	if command == "install" or "INSTALL":
		print("Loading....")
		cmd1 = os.system ("pip install macspoof")
	if command == "macspoof on" or "MACSPOOF ON":
		cmd1 = os.system ("macspoof --on")
	if command == "macspoof off" or "MACSPOOF OFF":
		cmd1 = os.system ("macspoof --off") 

loopfunc()