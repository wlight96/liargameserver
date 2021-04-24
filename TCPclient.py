from socket import *
serverName = '52.78.106.57'
serverPort = 3000
#client socket 생성
clientSocket = socket(AF_INET, SOCK_STREAM)
# server socket에 연결 요청
clientSocket.connect((serverName,serverPort))

sentence = input ('Input lowercase sentence:')
# 입력받은 msg를 byte type으로 변환 후 datasocket으로 전송
clientSocket.send(sentence.encode())
# 대문자로 변형된 msg를 recv API로 받아옴.
modifiedSentence = clientSocket.recv(1024)

print ('From Server: ', modifiedSentence.decode())
# 사용한 client socket 닫기.
clientSocket.close()