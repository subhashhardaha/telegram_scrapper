#!/bin/env python3

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser

print("[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input("[+] enter api ID : ")
cpass.set('cred', 'id', xid)
xhash = input("[+] enter hash ID : ")
cpass.set('cred', 'hash', xhash)
xphone = input("[+] enter phone number : ")
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print("[+] setup complete !")
print("[+] now you can run any tool !")
