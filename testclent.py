from socket import *

# Colab에서 실해시는 Sever는 이더넷 연결, Colab은 Client로 연결
#serverName = '219.254.56.176'
serverName = '127.0.0.1'
serverPort = 8080

def create_socket_and_send_message(request_message):
  # 클라이언트 소켓 만들기
  clienntSocket = socket(AF_INET, SOCK_STREAM)
  clienntSocket.connect((serverName, serverPort))
  clienntSocket.send(request_message.encode('utf-8'))

  # 응답확인
  receive_message = clienntSocket.recv(65535)
  print(receive_message.decode())

  clienntSocket.close()

request_message = 'GET /index.html HTTP/1.1\r\n'
#request_message += 'Host: 219.254.56.176:12000\r\n'
request_message += 'Host: 127.0.0.1:8080\r\n'
request_message += 'Connection: Keep-Alive\n\n'
create_socket_and_send_message(request_message)