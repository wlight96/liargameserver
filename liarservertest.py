import json
# socket lib ���
from socket import *

# socket port ��ȣ
serverPort = 3000
# server socket (���� ��Ĺ)
serverSocket = socket(AF_INET,SOCK_STREAM)
# server socket ���� �ּҿ� port ��ȣ ���ε�
serverSocket.bind(('',serverPort)) 
# ���� ������ ��Ĺ �� 4��.
serverSocket.listen(4)
print ('The server is ready to receive')

while 1:
    # ���� ��Ĺ�� ������ Ȯ�� �Ǹ� data ��Ĺ�� �Ҵ��Ѵ�.
    connectionSocket, addr = serverSocket.accept()

    # data��Ĺ���� ���� client�� ���� msg�� recv API�� �޴´�.
    jsonsentence = connectionSocket.recv(1024)

    json_data = json.loads(jsonsentence)
    state = json_data["state"]
    # ó�� ����
    if state == "enter" :
        playername = json_data["player"]
    # ä�� �ְ� �ޱ�
    elif state == "chat"
        chat = 
    # �빮�ڷ� ���� ���ڿ� ����
    capitalizedSentence = sentence.upper() 
    # send API�� ���� clientsocket���� ����
    connectionSocket.send(capitalizedSentence)
    
    
    # ���� ����
    # data socket�� �ݾ��ش�.
    connectionSocket.close()
