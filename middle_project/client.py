from socket import *

serverName = '127.0.0.1'
serverPort = 8080

def create_socket_and_send_message(request_message):
  clienntSocket = socket(AF_INET, SOCK_STREAM)
  clienntSocket.connect((serverName, serverPort))
  clienntSocket.send(request_message.encode('utf-8'))

  receive_message = clienntSocket.recv(65535)
  print(receive_message.decode())

  clienntSocket.close()

# GET (show index.txt)
request_message = 'GET /index.txt HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)

# GET Error(wrong address)
request_message = 'GET /index.html HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)  

# POST (no data)
request_message = 'POST / HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\r\n'
create_socket_and_send_message(request_message)

# POST (make new file)
request_message = 'POST / HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\r\n'
request_message += 'Data: Filename: new_file Content: New_Content\n\n'
create_socket_and_send_message(request_message)

# PATCH (modify index.txt)
request_message = 'PATCH /index.txt HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\r\n'
request_message += 'Data: Hello_Sehee!\n\n'
create_socket_and_send_message(request_message)

# PUT (update index.txt)
request_message = 'PUT /index.txt HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\r\n'
request_message += 'Data: Information_is_updated.\n\n'
create_socket_and_send_message(request_message)

# Error (Other Method)
request_message = 'DELETE / HTTP/1.1\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\r\n'
request_message += 'Data: data....\n\n'
create_socket_and_send_message(request_message)

# Error (Other HTTP version)
request_message = 'PATCH / HTTP/2\r\n'
request_message += 'Host: ' + serverName + '\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)