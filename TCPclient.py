from socket import *
serverName = '***.**.**'
serverPort = 12000
#client socket ����
clientSocket = socket(AF_INET, SOCK_STREAM)
# server socket�� ���� ��û
clientSocket.connect((serverName,serverPort))

sentence = input ('Input lowercase sentence:')
# �Է¹��� msg�� byte type���� ��ȯ �� datasocket���� ����
clientSocket.send(sentence.encode())
# �빮�ڷ� ������ msg�� recv API�� �޾ƿ�.
modifiedSentence = clientSocket.recv(1024)

print ('From Server: ', modifiedSentence.decode())
# ����� client socket �ݱ�.
clientSocket.close()