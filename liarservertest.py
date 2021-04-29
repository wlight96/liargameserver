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

def connect():
    connectionSocket, addr = serverSocket.accept()
    jsonsentence = connectionSocket.recv(1024)
    
def liargame():
    return 0

while 1:
    # 제어 소캣에 연결이 확인 되면 data 소캣을 할당한다.
    connectionSocket, addr = serverSocket.accept()

    # data소캣으로 부터 client가 보낸 msg를 recv API로 받는다.
    data = connectionSocket.recv(1024)
    json_data = json.loads(data.decode("utf-8"))
    state = json_data["state"]
    # 처음 연결
    if state == "enter" :
        playername = json_data["player"]
        player_json = {
            "state": "enter",
            "plyer":players
        }
        connectionSocket.send(bytes(player_json,encoding="utf-8"))
        continue

    # 채팅 주고 받기
    elif state == "chat":
        if players in json_data["nick"]:
            nickName = json.loads(json_data["nick"])
            chat_json ={
                nickName : ""
            }
        chat
    # 대문자로 받은 문자열 변형
    capitalizedSentence = sentence.upper() 
    
    # send API를 통해 clientsocket으로 전송
    connectionSocket.send(capitalizedSentence)
    
    
    # 게임 종료
    # data socket을 닫아준다.
    connectionSocket.close()
