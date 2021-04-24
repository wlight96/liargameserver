from socket import *
import json
serverName = '3.35.24.169'
serverPort = 3000
#client socket 생성
clientSocket = socket(AF_INET, SOCK_STREAM)
# server socket에 연결 요청
clientSocket.connect((serverName,serverPort))
ok = 1

while ok != 0:
    ok = input('오케이값 : ')
    sentence = input ('Input lowercase sentence:')
    
    data = str(ok) + ',' + sentence
    j_item ={
        "ok" : int(ok),
        "Bdate" : json.dumps(ok),
        }
    # 입력받은 msg를 byte type으로 변환 후 datasocket으로 전송
    clientSocket.send(data.encode())
    # 대문자로 변형된 msg를 recv API로 받아옴.
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server: ', modifiedSentence.decode())

# 사용한 client socket 닫기.
clientSocket.close()