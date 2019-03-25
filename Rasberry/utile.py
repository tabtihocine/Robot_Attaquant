#!/usr/bin/env python

import time
import thread
import csv
import os

# found in www.StackOverFlow.com
#used to wait result for scannig
def wait_result():

    def work():
        time.sleep(5)

    def lock_call(func,lock):
        lock.acquire()
        func()
        lock.release()

    lock = thread.allocate_lock()
    thread.start_new_thread( lock_call, ( work, lock, ) )
    
    while(not lock.locked()):
        time.sleep(1)
    while(lock.locked()):
        time.sleep(1)
    
# methode to parse the results and format it to creat a csv file
# to use it in exploittion 
def parcer_result_scannig(result_of_scannig):
    filed=["host","ref"]
    rows=[]
    result_of_scannig=open(str(result_of_scannig) ,"r")
    lines=csv.reader(result_of_scannig)
    for line in lines:
            if (str(line[5])=="High" and str(line[11])!="NOCVE"):
                    rows.append({'host':str(line[0]),'ref': str(line[11])})
    result_of_scannig.close()

    high_vul=open("high_vul.csv" , "w")
    writer=csv.DictWriter(high_vul,fieldnames=filed)
    writer.writerows(rows)
    high_vul.close()

    liste_of_hosts=[]

    high_vul=open("high_vul.csv","r")
    lines=csv.reader(high_vul)
    for line in lines:
            liste_of_hosts.append(line)
    temp=[liste_of_hosts[0]]
    liste_of_hosts.pop(0)
    for host in liste_of_hosts: 
            tmp=True
            for tem in temp:
                    if tem[0] == host[0]:
                            tmp=False
                            tem[1]= tem[1]+" "+host[1]
            if tmp == True:
                    temp.append(host)
    liste_of_hosts=temp
    high_vul.close()

    temp=[]
    for host in liste_of_hosts:
            temp.append({'host':str(host[0]),'ref': str(host[1])})

    high_vul=open("high_vul.csv","w")
    writer=csv.DictWriter(high_vul,fieldnames=filed)
    writer.writerows(temp)
    high_vul.close()

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