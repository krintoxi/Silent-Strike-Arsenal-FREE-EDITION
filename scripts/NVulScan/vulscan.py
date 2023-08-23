# -*- coding: utf-8 -*-
import os
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⠶⠒⠒⠒⠒⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠛⠉⠀⠀⠀⠈⠉⠉⠽⠿⣲⣶⢬⣉⣛⣓⣶⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠀⠀⠀⣀⡴⠂⠀⠀⠀⠀⠀⠀⠈⠉⠙⣿⣞⡋⠉⠁⠀⠙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⠿⠁⠀⢀⡶⣷⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⡉⠛⠶⢄⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⢞⡿⠃⠀⠀⠠⠴⠋⠁⠀⠀⠀⢠⣤⣴⣾⣿⣧⣤⣖⣒⠀⠈⣿⣻⢷⣤⣼⡆⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣞⣧⠞⠁⠀⠀⠀⠀⠀⣀⡀⢀⣴⣾⣽⣿⣾⣿⣿⣿⣿⣿⣭⣄⡀⠙⣿⡳⣯⣷⡇⠀⠀⣸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⠏⡾⠃⠀⠀⣠⣴⣶⡿⢋⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⠿⣦⣤⣈⣽⣶⣎⣠⣶⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡟⡼⠁⠀⣠⣾⣿⠿⣯⢾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢿⡍⠛⠛⠻⣷⣯⡭⣿⣛⡻⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠇⠇⠀⣴⣿⡿⣣⣾⡁⣿⣿⣿⠀ Counter Intel⠀⠘⣿⣿⡇⢈⣿⣿⣷⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⣟⠀⢀⣨⠿⢋⣼⣿⣿⣧⢿⣿⣿⠁⠀⠀  Toolkit⠀⠀⠀⠀⠘⣿⣿⡇⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠹⣦⣀⣤⡴⠋⣿⢸⣿⡇⣸⣿⡿⠓⠂⠀⢶⣦⣀⠀⠀⠀⠀⠀⣠⣴⠶⠀⠐⠻⣿⣿⣇⢻⣿⡏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣼⡿⢀⣙⣀⡦⣤⣤⣀⠀⠈⠻⣿⣶⣶⣶⣿⠟⠁⠀⣀⣤⣶⢶⣄⣉⠀⢿⣧⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⡿⠁⣹⣰⣿⣿⣿⣷⣿⣿⣦⣤⢼⡿⠿⣿⣧⣤⣴⣿⣿⣾⣿⣿⣿⡤⣍⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣄⠁⢿⡟⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⢻⡟⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡆⠈⢷⣿⣿⣿⣿⣿⣿⠟⢹⣀⣀⣐⣟⣻⣿⣿⣿⣿⣿⣧⡾⠀⣰⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⡿⡿⣃⠀⣉⡛⠛⠻⢿⡿⣞⣵⡞⣻⣿⣜⣿⣮⡻⢿⡭⡟⢛⣛⣁⠀⣉⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⣷⢭⣭⣈⣥⡶⠖⠀⠈⠛⣽⢻⣿⣿⣿⡘⣏⠋⠃⠀⠺⢶⣄⣩⣭⡵⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⡛⠲⣔⡆⢸⡃⣾⣿⢹⣿⣧⢘⡂⢰⣠⠖⢿⣿⣿⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡄⠙⠽⢾⣧⣹⡟⠈⠛⣋⣿⡷⠶⠃⢰⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠹⡿⣿⣤⣀⣬⣀⡈⢁⠀⡀⠀⣀⣀⢠⣴⣿⣿⠻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣏⣀⣿⣿⢿⣿⣿⣿⣿⣾⣷⣿⣿⣿⣿⡿⡟⣿⣾⣀⣹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀
⠀⠀⠀⡾⠋⠓⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣽⣸⡈⡽⠉⣿⠙⡏⢩⣇⣧⡗⠉⠉⠉⠉⠈⠉⠓⠒⠒⠒⠒⠒⢒⣲⠖⠊⢹⠟⠋
⠀⠀⠀⣧⣶⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣒⣿⣶⣿⠿⠿⢉⣙⣛⣛⣛⠻⠷⠶⠶⠶⠶⠾⠟⠋⣉⣠⠴⠋⠁⠀⠀
⠀⠀⠀⢹⣿⣿⠟⠛⠛⠛⠛⠛⢻⣿⠛⡿⢻⣟⣟⢻⣿⣟⠉⡍⣽⣽⡟⢿⠉⣹⡟⠓⠒⠒⠒⠒⠒⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠻⣷⡀⠘⡈⠋⠛⢿⡟⠚⠛⠉⠈⠃⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆⠙⠰⠆⣴⠀⡴⢰⠀⠃⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣄⣠⣽⢤⣧⣄⣤⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
print ("******************************")
print ("N Vulnerability Scanner")
print ("C.I Toolkit Module")
print ("******************************")
target = input('Scan Target: ')
cmd1 = os.system ('perl '+'tools/vscan/nikto.pl -h ' +target+' -o NV_SCAN_Result.html')