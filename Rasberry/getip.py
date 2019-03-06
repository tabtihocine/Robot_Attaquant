#!/usr/bin/python3.7
import os

def getMyIp():
    os.system("ifconfig > myip.txt")
    file = open("myip.txt", "r")
    i = 0
    while i < 19:
        line = file.readline()
        i = i + 1 
    ipsplit = line.split()
    file.close()
    ipsplit = ipsplit[1].split('.')
    ipsplit[3] = '0'
    ipsplit = ".".join([ipsplit[0],ipsplit[1],ipsplit[2],ipsplit[3]])
    adress = ipsplit + "/24"
    return adress
getMyIp()