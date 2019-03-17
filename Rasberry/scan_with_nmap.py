#!/usr/bin/python3.7
#import getip
import nmap


def scanwithnamp():
    nm = nmap.PortScanner()
    nm.scan(hosts="192.168.43.0/24", arguments='-sS -sV -Pn')
    file = open("result_nmap.txt", "w")
    for host in nm.all_hosts():
        file.write('ip of Host :  ' + str(host) + '\n')
        file.write('State  of host: ' + str(nm[host].state()) + '\n')
        for protocol in nm[host].all_protocols():
            file.write('Protocol : ' + str(protocol) + '\n')
            listofport = nm[host][protocol].keys()
            for port in listofport:
                file.write('\tport : '+ str(port) +\
                    '\t\tstate : '+ str(nm[host][protocol][port]['state']) +\
                    '\t\tservice : '+ str(nm[host][protocol][port]['name'])+\
                    '\t\tproduct : ' + str(nm[host][protocol][port]['product'])+ \
                    '\t\tversion : '+ str(nm[host][protocol][port]['version']) + '\n')
        file.write('\n\n')
    file.close()


scanwithnamp()
