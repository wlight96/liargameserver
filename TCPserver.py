# socket lib 사용
from socket import *
# socket port 번호
serverPort = 3000
# server socket (제어 소캣)
serverSocket = socket(AF_INET,SOCK_STREAM)
# server socket 서버 주소와 port 번호 바인딩
serverSocket.bind(('52.78.106.57',serverPort)) 

# 연결 가능한 소캣 수 1개.
serverSocket.listen(1)
print ('The server is ready to receive')

while 1:
    # 제어 소캣에 연결이 확인 되면 data 소캣을 할당한다.
    connectionSocket, addr = serverSocket.accept()
    # data소캣으로 부터 client가 보낸 msg를 recv API로 받는다.
    sentence = connectionSocket.recv(1024)
    # 대문자로 받은 문자열 변형
    capitalizedSentence = sentence.upper() 
    # send API를 통해 clientsocket으로 전송
    connectionSocket.send(capitalizedSentence)
    # data socket을 닫아준다.
    connectionSocket.close()
