from cgitb import html
import sys
from socket import *
from datetime import datetime
from urllib import request, response

# Make TCP server socket
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort)) 

# Start receive request
serverSocket.listen(1)
print('The server is running...\n')

while True:
    # Make connection if request come.
    client_socket, addr = serverSocket.accept()  

    # receive
    data = client_socket.recv(65535)

    # Show HTTP Request message
    print(data.decode())

    request_data = data.decode().split() 
    request_method = request_data[0] 
    request_item = request_data[1] 
    request_version = request_data[2] 
    # if request has body
    if len(request_data) > 7:
        request_body = request_data[8:]
    else: 
        request_body = []

    server_name = addr[0]
    
    if request_version == "HTTP/1.1":
        # GET(Server send Data)
        if request_method == "GET": 
            # Valid address
            if request_item == "/index.txt": 
                response_data = "{0} 200 OK\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
                # read file
                with open ('index.txt', 'r') as txt:
                        while True:
                            body = txt.readline()
                            if not body:
                                break
                            response_data += body

            else: # Invalid address(Send Data)
                response_data = "{0} 404 Error\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)                
        
        # POST(Client send Data for generate)
        elif request_method == "POST" : 
                # If client has the data to post
            if len(request_body) > 0: 
                response_data = "{0} 200 OK\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
                # create new file
                fliename = request_body[1]
                content = request_body[3]
                with open('{0}.txt'.format(fliename), 'w') as f:
                    f.write(content + "\n")
                    f.close()
                # read file
                with open ('{0}.txt'.format(fliename), 'r') as txt:
                        while True:
                            body = txt.readline()
                            if not body:
                                break
                            response_data += body
            
            else: # no data to modify
                response_data = "{0} 204 No content\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
            
        # PUT(Client send Data for Update)
        elif request_method == "PUT" : 
            if request_item == "/index.txt": 
                # If client has the data to put
                if len(request_body) > 0: 
                    response_data = "{0} 200 OK\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                    datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
                    # update file
                    content = request_body[0]
                    with open('index.txt', 'w') as f:
                        f.write(content + "\n")
                        f.close()
                    # read file
                    with open ('index.txt', 'r') as txt:
                            while True:
                                body = txt.readline()
                                if not body:
                                    break
                                response_data += body
                        
                else: # no data to modify
                    response_data = "{0} 204 No content\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                    datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
            
            else: # Invalid address(Send Data)
                response_data = "{0} 404 Error\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)   

        # PATCH(Client send Data for Modify)
        elif request_method == "PATCH" : 
            if request_item == "/index.txt": 
                # If client has the data to patch
                if len(request_body) > 0: 
                    response_data = "{0} 200 OK\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                    datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
                    append = request_body[0]
                    # update file
                    with open('index.txt', 'a') as f:
                        f.write(append + "\n")
                        f.close()
                    # modify file
                    with open ('index.txt', 'r') as txt:
                        while True:
                            body = txt.readline()
                            if not body:
                                break
                            response_data += body
                                
                else: # no data to modify
                    response_data = "{0} 204 No content\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                    datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)

            else: # Invalid address(Send Data)
                response_data = "{0} 404 Error\nDate: {1}\nServer: {2}\n\n".format(request_version, 
                datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)   
            
        # Other method    
        else: 
            response_data = "{0} 405 Method Not Allowed\nDate: {1}\nServer: {2}\n\n".format(request_version,
            datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
    
    # Other HTTP version
    else: 
        response_data = "{0} 505  HTTP version not supported\nDate: {1}\nServer: {2}\n\n".format(request_version,
        datetime.now().strftime('%a, %d %b %Y %H:%M:%S KST'), server_name)
            

    client_socket.send(response_data.encode())
    client_socket.close()