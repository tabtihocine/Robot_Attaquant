#!/usr/bin/env python

"""
Veuillez installer d'abord obenvas-lib avec la commande:
pip install openvas-lib
et pour convertir le rapport de xml a csv, installer xml2csv:
pip install xmlutils
"""
from openvas_lib import VulnscanManager, VulnscanException
from threading import Semaphore
from functools import partial
from xml.etree import ElementTree
import base64
import os,sys
import argparse

#Afficher la progression du scan
def progression(i):
	print(str(i)),
	sys.stdout.flush()

#Generer le rapport du scan
def get_report(manager, report_id, ip):
	result_dir = os.path.dirname(os.path.abspath(__file__)) + "/results"
	if not os.path.exists(result_dir):
		os.makedirs(result_dir)

	try:
		report = manager.get_report_xml(report_id)
	except Exception as e:
		print(e)
		return
	else:
		fout_path = result_dir + "/xml/"
		if not os.path.exists(fout_path):
			os.makedirs(fout_path)

		fout = open(fout_path + ip + ".xml", "wb")
		fout.write(ElementTree.tostring(report, encoding='utf-8', method='xml'))
		fout.close()


def run(manager, ip):
	Sem = Semaphore(0)
	scan_id, target_id = manager.launch_scan(
		target=ip,
		profile="Full and fast",
		callback_end=partial(lambda x: x.release(), Sem),
		callback_progress=progression
	)
	Sem.acquire()
	report_id = manager.get_report_id(scan_id)

	get_report(manager, report_id, ip)
	manager.delete_scan(scan_id)
	manager.delete_target(target_id)

#Configurer la connexion vers openvas manager
manager = VulnscanManager("localhost", "admin", "ouss1980")

#Lancer le scan en entrant  une cible
run(manager, "192.168.43.1")

#Convertir le fichier xml en csv
os.system("xml2csv --input results/xml/192.168.43.1.xml --output result.csv --tag port")
