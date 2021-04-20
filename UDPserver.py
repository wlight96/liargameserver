from socket import * # socket lib 사용

serverPort = 12000 # 소캣 port 12000

serverSocket = socket(AF_INET, SOCK_DGRAM) # server socket 

# server binding
serverSocket.bind(('', serverPort)) # 서버 소캣이 연결될 주소를 부여
                                    # 서버 IP와 port 번호를 결합. 
print ("The server is ready to receive")

while 1:
    # server soket으로 부터 메세지가 올때 까지 recvform api를 사용해서 기다린다.
    message, clientAddress = serverSocket.recvfrom(2048)
    # 받은 문자열 대문자로 바꿔줌
    modifiedMessage = message.upper()
    # 메세지가 잘 변형 되었는지 확인.
    print (modifiedMessage)
    #client 소캣으로 메세지 sendto API 사용 전달
    serverSocket.sendto(modifiedMessage, clientAddress)
