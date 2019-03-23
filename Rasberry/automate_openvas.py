#!/usr/bin/env python

#import getip
import re
import time
import utile
import os

network_to_scan = "192.168.43.0/24"
name_of_scan="host_scan"
name_of_task="sacn_network"

#creat target 
openvas_target_creat = "omp -u admin -w admin  -X '<create_target> <name>"+name_of_scan+"</name> <hosts>"+network_to_scan+"</hosts> </create_target>' > temp.target"
os.system(openvas_target_creat)
result_of_command = open("temp.target" , "r")
list_of_lines = result_of_command.readlines()
print " end of creat target"

## get target id 
for line in list_of_lines:
    searche = re.compile('create_target_response id="(.*?)"')
    yes_i_found = re.search(searche , line)
    if yes_i_found:
        id_of_target= yes_i_found.group(1)
print " end of get target id "

## id of configuration 
id_of_config_scan = "74db13d6-7489-11df-91b9-002264764cea"

## creat task
openvas_task_creat ="omp -u admin -w admin -X '<create_task> <name></name> <comment>"+name_of_task+"</comment> <config id=\""+ id_of_config_scan +"\"/> <target id=\""+id_of_target+"\"/> </create_task>' > temps.task"
os.system(openvas_task_creat)
result_of_command2=open("temps.task","r")
list_of_lines= result_of_command2.readlines()
print " end of creat task"

### get task id 
for line in list_of_lines:
    searche = re.compile('create_task_response id="(.*?)"')
    yes_i_found = re.search(searche , line)
    if yes_i_found:
        id_of_task= yes_i_found.group(1)
print " end of get task id "

## start task scanning
openvas_task_start="omp -u admin -w admin -X '<start_task task_id=\""+id_of_task+"\"/>' > temp.Stask"
os.system(openvas_task_start)
time.sleep(5)
print " end of start task "

# whait for the end of scan 
get_status_of_task="omp -u admin -w admin -G  > hahaha.txt" 
os.system(get_status_of_task)
while 'Done' not in open("hahaha.txt","r").read():
    utile.wait_result()
    os.system(get_status_of_task)
print " end task "

# get report on CSv format 
get_rep="omp -u admin -w admin -X '<get_reports/> <report id><task id=\""+ str(id_of_task) +"\"/>' > repor.xml"
os.system(get_rep)
rep_xml =open("repor.xml","r")
line_xml = rep_xml.readlines()
searche_this = '<report id="(.*?)" format_id="(.*?)<task id="' + str(id_of_task) + '"'
for line in line_xml:
    is_it = re.compile(searche_this)
    yes_i_found =re.search(is_it,line)
    if yes_i_found:
        id_of_report = yes_i_found.group(1)

        name_of_report="result_of_scannig.csv"            
        openvas_report_dowland= ("omp -u admin -w admin --get-report "+id_of_report+" --format c1645568-627a-11e3-a660-406186ea4fc5 > "+name_of_report+"") % (id_of_report, name_of_report)
        os.system(openvas_report_dowland)

print "================================="
print '\t\t'"finish scannig"
print "================================="

