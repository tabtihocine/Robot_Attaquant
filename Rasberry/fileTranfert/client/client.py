import socket
import os

s = socket.socket()
host = "AZRARA"
#host = "192.168.1.43"
port = 6677
s.connect((host, port))
print("Connected ...")

fileName =  "FILE.txt"
file = open(fileName, "wb")
fileData = s.recv(1024)
file.write(fileData)
file.close()
print("File has been received successfully")
os.system("lsof -i :6677")
