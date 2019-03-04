#!/usr/bin/env python3
import json
import nmap 
import netifaces as ni

#CAAAA MARRCHEEEEEE OURAAAA

ipBrut = str(ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr'])
adressSplit = ipBrut.split(".")
adressSplit[3] = '0'
adressJoin = ".".join(adressSplit)
finalIp = adressJoin+'/24'

file = open('result.html','w')

ports_list = ['80','443','22','29081','43176','63753','19081','81','8080','8081','8433','8031']

ports = ','.join(str(x) for x in ports_list)

npy = nmap.PortScanner()
npy.scan(hosts=finalIp, arguments='-sS -p'+ ports)

file.write("<html><body><table border='1'>")
file.write ("<tr>")
file.write ("<th>IP</th>")
file.write ("<th>STATE</th>")

for x in ports_list:
     file.write ("<th>TCP " + x + "</th>")
file.write ("</tr>") 

for host in npy.all_hosts():
     file.write ("<tr>")
     file.write ("<td>"+ host +"</td>")
     file.write ("<td>"+ npy[host].state() +"</td>")

for x in ports_list:
     tmp = json.loads( str(npy[host]['tcp'][int(x)]).replace('\'', '"').replace('u"', '"') )
     status = str(tmp['state'])
     if status == "open":
          color = "green"
     elif status == "closed":
          color = "red"
     else:
          color = "yellow"

     file.write ("<td style='background-color: " + color +"'>"+ status +"</td>")

file.write ("</tr>")
file.write ("</table></body></html>")
file.close()
