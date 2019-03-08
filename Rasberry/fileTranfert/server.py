#!/usr/bin/python3.7
import socket


s = socket.socket()
#host = "192.168.1.43"
host = socket.gethostname()
port = 6677

s.bind((host, port))
s.listen(4)
print("Waiting for connections ...")
print(host)
connection, addr = s.accept()
print(addr, "Has connected to the server")

filename = "FILE.txt"
file = open(filename, "rb")
fileData = file.read(1024)
connection.send(fileData)
print("Data has been transmitted successfully")
