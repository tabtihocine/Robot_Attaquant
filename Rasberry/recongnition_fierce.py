#!/usr/bin/env python
import os
import sys


def recon():
    os.system('fierce -dns ' + str(sys.argv[1]) +' -file  fierce_recon.txt -threads 100')
    file = open("fierce_recon.txt","r")
    
    word=""
    listip = []  

    while len(word)!=1:
        word = file.readline()
    word=""
    while len(word)!=1:
        word=file.readline() 

    line=file.readline()
    line=line.split()
    
    if line[0]=="Unsuccessful":
        for i in range(5):
            line = file.readline()
        arret= True
        while arret:
            line=file.readline()
            line=line.split()
            if len(line)==0:
                break
            listip.append(line[0])

    else:
        fileastable= []   
        while line:
            line= file.readline()
            fileastable.append(line)
            a=0
        for i in range(len(fileastable)):
            ll=fileastable[i]
            if ll=='\t)\n':
                a=i
        a=a+1
        while a != len(fileastable)-2:
            aa=fileastable[a].split()
            if aa[3]=="CNAME":
                a=a+1
            else:    
                listip.append(aa[4])
                a=a+1
    file.close()

    os.system('rm -rf  fierce_recon.txt')
    file= open("result_fierce" , "w")
    i=0
    while i != len(listip):
        file.write(str(listip[i])+'\n')
        i=i+1
    file.close()
recon()