from socket import *
from datetime import datetime
import sys
from urllib import request

serverPort = 8080
# Make TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(0)

while True:
    client_socket, addr = serverSocket.accept()
    data = client_socket.recv(65535)

    request_data = data.decode().split()
    print(data.decode())
    request_method = request_data[0]
    request_version = request_data[2]

    server_name = "hi"

    if request_method == "GET":
        response_data = "{0} 200 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name, 
        datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
    else:
        response_data = "{0} 405 Method Not Allowed\nServer: {1}\nDate: {2}\n".format(request_version, server_name, 
        datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))


    client_socket.send(response_data.encode())
    client_socket.close()
                    