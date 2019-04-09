#!/usr/bin/python
import re
from subprocess import Popen, PIPE
import os
import subprocess

DN = open(os.devnull, 'w')

#Recuperation de l interface wifi
def iwconfig():
    monitors = []
    proc = Popen(['iwconfig'], stdout=PIPE, stderr=DN)
    for line in proc.communicate()[0].split('\n'):
        if len(line) == 0: continue
        if line[0] != ' ':
            wired_search = re.search('eth[0-9]|em[0-9]|p[1-9]p[1-9]', line)
            if not wired_search:
                iface = line[:line.find(' ')]
                monitors.append(iface)
    return str(monitors[0])

#Recuperation du canal utilise par l interface wifi
def channel():
    card = str(iwconfig())
    channels = subprocess.check_output("iwlist {} channel".format(card),shell=True)
    for chan in channels.split('\n'):
        if "Current" in chan:
            chann= chan.strip()
    numbers =  re.findall('\d+', chann)
    currentChannel = numbers[-1]
    return currentChannel
