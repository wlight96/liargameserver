import json
# socket lib 사용
from socket import *

# socket port 번호
serverPort = 3000
# server socket (제어 소캣)
serverSocket = socket(AF_INET,SOCK_STREAM)
# server socket 서버 주소와 port 번호 바인딩
serverSocket.bind(('',serverPort)) 
# 연결 가능한 소캣 수 4개.
serverSocket.listen(4)
print ('The server is ready to receive')

while 1:
    # 제어 소캣에 연결이 확인 되면 data 소캣을 할당한다.
    connectionSocket, addr = serverSocket.accept()

    # data소캣으로 부터 client가 보낸 msg를 recv API로 받는다.
    jsonsentence = connectionSocket.recv(1024)

    json_data = json.loads(jsonsentence)
    state = json_data["state"]
    # 처음 연결
    if state == "enter" :
        playername = json_data["player"]
    # 채팅 주고 받기
    elif state == "chat"
        chat = 
    # 대문자로 받은 문자열 변형
    capitalizedSentence = sentence.upper() 
    # send API를 통해 clientsocket으로 전송
    connectionSocket.send(capitalizedSentence)
    
    
    # 게임 종료
    # data socket을 닫아준다.
    connectionSocket.close()
