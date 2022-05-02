from socket import *
from datetime import datetime
import sys
from urllib import response

serverPort = 80
# Make TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))

# Start receive request
serverSocket.listen()
print('The server is running')

while True:
    # Make connection if request come.
    connectionSocket, addr = serverSocket.accept()

    # receive
    message = connectionSocket.recv(65535).decode()
    request_headers = message.split()
    if request_headers[2] == 'HTTP/1.1' and request_headers[0] in ['GET','HEAD']:
        # if addr is correct
        if request_headers[1] in ['/','/index.html','./index.html']:
            response_data = 
