import json
# socket lib 사용
from socket import *
# socket port 번호
serverPort = 3000
# server socket (제어 소캣)
serverSocket = socket(AF_INET,SOCK_STREAM)
# server socket 서버 주소와 port 번호 바인딩
serverSocket.bind(('',serverPort)) 

# 연결 가능한 소캣 수 1개.
serverSocket.listen(4)
print ('The server is ready to receive')
# 제어 소캣에 연결이 확인 되면 data 소캣을 할당한다.
connectionSocket, addr = serverSocket.accept()
ok = 1

while ok != 0:
    # data소캣으로 부터 client가 보낸 msg를 recv API로 받는다.
    data = connectionSocket.recv(1024)
    decode_data = data.decode()
    json_data = json.loads(decode_data.encode("utf-8")) 
    ok = int(json_data["ok"])
    if ok == 0:
        # data socket을 닫아준다.
        connectionSocket.close()
        break
    sentence = json_data["sentence"]
    print(sentence)

    # 대문자로 받은 문자열 변형
    #capitalizedSentence = data.upper() 
    capitalizedSentence = sentence.upper()

    send_data = {
        "sentence" : capitalizedSentence
    }
    msg = json.dumps(send_data)
    # send API를 통해 clientsocket으로 전송
    #connectionSocket.send(bytes(capitalizedSentence,encoding="utf-8"))
    connectionSocket.send(msg.encode())