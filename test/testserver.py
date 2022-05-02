from socket import *
from datetime import datetime
import sys

serverPort = 80
# Make TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.3.120', serverPort))

serverSocket.listen()
print('The server is running...')

while True:
    client_socket, addr = serverSocket.accept()
    data = client_socket.recv(65535)

    request_data = data.decode().split()
    print(data.decode())
    request_method = request_data[0]
    request_version = request_data[2]

    server_name = "Test Server"

    if request_method == "GET":
        response_data = "{0} 200 OK\nServer: {1}\nDate: {2}\n".format(request_version, server_name, 
        datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))
    else:
        response_data = "{0} 405 Method Not Allowed\nServer: {1}\nDate: {2}\n".format(request_version, server_name, 
        datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'))


    client_socket.send(response_data.encode())
    client_socket.close()
                    