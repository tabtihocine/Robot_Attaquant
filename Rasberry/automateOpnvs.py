#!/usr/bin/env python

import os
from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole


#os.system('msfrpcd -P ouss1980 -n -f -a 127.0.0.1')

global global_positive_out
global_positive_out = list ()

global global_console_status
global_console_status = False

def read_console(console_data):
	global global_console_status
	global_console_status = console_data['busy']
	print global_console_status
	if '[+]' in console_data['data']:
		sigdata = console_data['data'].rstrip().split('\n')
		for line in sigdata:
			if '[+]' in line:
				global_positive_out.append(line)
	print console_data['data']

client = MsfRpcClient('ouss1980')
console = MsfRpcConsole(client, cb = read_console)

console.execute ('load openvas')
console.execute ('openvas_connect admin ouss1980 127.0.0.1 9390 ok')

