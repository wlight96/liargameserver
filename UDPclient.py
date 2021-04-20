
# socket API lib
from socket import * 
#ip addr
serverName = '****.****.***.**.**'
# port addr 
serverPort = 12000 
#  client socket API make 
clientSocket = socket(AF_INET,SOCK_DGRAM) # AF_INET과 datagram이 있는 소캣 오픈.
                                            
m = input('Input lowercase sentence:') 

# sendto API를 사용하여 서버에게 인코딩된 입력받은 문자열을 전달한다.
clientSocket.sendto(m.encode(),(serverName, serverPort)) 

# recvfrom API를 사용하여 대문자로 변형된 문자열을 받는다.
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# bytes type msg로 오기 때문에 decoding 과정을 해주어야 출력 시 이상이 없다.
print (modifiedMessage.decode())
# 사용한 소캣을 닫아준다.
clientSocket.close()
