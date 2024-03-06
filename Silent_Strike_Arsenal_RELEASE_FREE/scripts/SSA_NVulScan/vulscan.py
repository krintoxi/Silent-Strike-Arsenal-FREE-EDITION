import os #line:2:import os
print ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⠶⠒⠒⠒⠒⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠀⠀⠀⠈⠉⠉⠽⠿⣲⣶⢬⣉⣛⣓⣶⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠀⣀⡴⠂⠀⠀⠀⠀⠀⠀⠈⠉⠙⣿⣞⡋⠉⠁⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠿⠁⠀⢀⡶⣷⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡉⠛⠶⢄⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⢞⡿⠃⠀⠀⠠⠴⠋⠁⠀⠀⠀⢠⣤⣴⣾⣿⣧⣤⣖⣒⠀⠈⣿⣻⢷⣤⣼⡆⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣞⣧⠞⠁⠀⠀⠀⠀⠀⣀⡀⢀⣴⣾⣽⣿⣾⣿⣿⣿⣿⣿⣭⣄⡀⠙⣿⡳⣯⣷⡇⠀⠀⣸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⠏⡾⠃⠀⠀⣠⣴⣶⡿⢋⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠿⣦⣤⣈⣽⣶⣎⣠⣶⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡟⡼⠁⠀⣠⣾⣿⠿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾
⠹⣦⣀⣤⠀⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣾⣿
⠀⠀⠀⠀⠀⠀⢀⣠⡶⠞⡛⢩⡁⢆⡐⢎⠰⡁⠆⣌⠰⣉⠙⡛⠷⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣲⠀⠀⠀⠀⢠⣿⠀⠀⠀
⠀⠀⠀⠀⣠⡾⠛⡡⢂⡱⢈⠅⡒⠰⢌⠢⠥⡑⢊⠤⢃⠤⢃⠜⡰⢠⢉⠛⣷⣄⠀⠀⠀⠀⠀⠀⣷⠹⣆⠀⣀⣴⠟⠙⢧⣀⠀
⠀⠀⣠⡾⢋⡔⢃⡑⠢⠔⡡⢊⠔⡉⢆⡑⢢⢁⢣⠘⡌⠢⢅⢊⠔⡡⢊⠔⡠⠛⢷⡄⠀⠀⠀⠀⢸⡆⠘⢿⡙⠳⣄⠀⣠⣿⡗
⠀⢰⡟⡠⢃⠄⠣⢌⣱⣬⣴⣥⣎⣔⣨⠐⠣⢌⠢⡑⢌⠱⡈⢆⡘⢄⠣⡘⠤⡉⢌⣻⣆⠀⠀⠀⢸⡇⣂⠈⢻⣄⢙⣿⠉⠉⠀
⠀⣿⢁⠦⡉⢌⣷⡿⠛⠉⠉⠛⠛⠿⢿⣯⡱⢈⠆⡱⢈⢦⣵⣶⠿⠿⢶⣷⣤⡑⠢⠄⢿⡆⠀⠀⠨⣷⢈⢆⡀⠹⣮⠃⠀⠀⠀
⢸⡟⡨⢆⠱⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡡⢚⣰⣿⠟⠋⠀⠀⠀⠀⠀⠹⢿⣧⡘⢸⣧⠀⠀⢀⣿⠨⠜⣠⠁⢻⣆⠀⠀⠀
⢸⣇⡱⢊⢼⡿⠀⠀⠀⠄⠀⠀⣸⣧⠀⠀⢿⡟⡰⣾⡏⠀⠀⣤⡀⠀⠀⠂⠀⠘⣿⣷⢉⣿⠀⠀⢨⡇⠣⡍⢤⡙⠤⣿⠀⠀⠀
⢸⡇⡇⢎⢚⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠐⣿⡇⠀⠐⠛⠁⠀⠀⠀⠀⠀⣿⣿⢸⡏⠀⠀⠐⣯⠀⠍⠦⡘⡔⣿⠂⠀⠀
⢸⡗⡌⢂⢎⡻⣷⣄⠀⠀⠀⠀⠀⢀⣠⣿⡿⢃⠌⣿⣿⣄⠀⠀⠀⠀⠀⠀⣠⡾⣻⢇⣿⠁⠀⠀⢘⡿⢠⡄⠑⡈⠔⣿⡁⠀⠀
⠘⣿⡄⢣⠸⣿⣿⣿⣷⣶⣤⣤⣶⣿⣿⡿⠑⣌⣲⡘⣿⣿⣷⣶⣤⣤⣴⣾⣿⣿⠏⣼⠏⠀⠀⠀⢸⡇⠥⢳⡀⠈⠐⣿⠃⠀⠀
⠀⢻⣇⠆⡱⢨⡙⣛⠻⠿⠿⠿⡟⢫⡱⢌⡡⢋⠭⡑⢢⢍⡛⠿⣿⣿⣿⡿⢟⢻⣼⠏⠀⠀⠀⠀⢸⡏⡒⡅⢦⠁⣈⣿⠀⠀⠀
⠀⠀⠹⢷⣆⡅⢢⠑⡍⢎⡱⢣⠜⡥⢊⠔⡄⢃⠆⡱⢈⠲⣉⠖⣡⠎⡴⠘⣬⡿⠁⠀⠀⠀⠀⡴⣿⢁⠣⢜⡠⢃⢸⡏⠀⠀⠀
⠀⠀⠀⠀⠙⠻⣶⣥⡘⢄⠒⡡⢊⠔⡡⢊⠔⡉⢆⠡⢃⡱⢠⠩⡐⢌⣰⣽⠏⠀⠀⠀⠀⠀⠀⣿⣿⣾⣷⣶⣶⣿⢾⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣾⣤⣑⠊⡔⢡⠊⡔⢡⢊⡑⠦⡐⣡⢒⣵⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⣠⣤⣼⠷⢿⣾⠷⢾⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠷⢶⣧⣼⣤⣦⣼⣤⣷⠾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⣿⣿⣶⣿⣣⣾⢿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢢⠻⠿⢿⣿⣴⣾⠁⠀⠀⠀ S.S.A_WEB_Vulnerability Scanner⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
▌│█║▌║▌║ ▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
▌│█║▌║▌║ ▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║""")#line:31:▌│█║▌║▌║ ▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║▌║▌║▌│█║""")
print ("******************************")#line:33:print ("******************************")
target =input ('Scan Target: ')#line:34:target = input('Scan Target: ')
print ("******************************")#line:35:print ("******************************")
cmd1 =os .system ('perl '+'tools/VSCAN/vscan.pl -h '+target +' -o V_SCAN_Result.html')#line:36:cmd1 = os.system ('perl '+'tools/VSCAN/vscan.pl -h ' +target+' -o V_SCAN_Result.html')