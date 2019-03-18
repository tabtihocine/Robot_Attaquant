#!/usr/bin/env python
import csv

file=open("result_of_scannig.csv" ,"r")
lines=csv.reader(file)
for line in lines:
    if (str(line[5])=="High"  and str(line[11])!="NOCVE") :
        print str(line[0])+">>>"+str(line[11])+ "\n\n"