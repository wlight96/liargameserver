import os 
import json
from flask import Flask 
from flask_socketio import SocketIO, emit
app = Flask(__name__) 
app.secret_key = "secret" 
socketio = SocketIO(app) 

@socketio.on('chat')
def handlechating(json):
    print('received chating: ' + str(json))
    data = json.loads(json)
    socketio.emit('chat',{
        state: 'chat',
        name: json.dumps("문상혁 바보",ensure_ascii=false),
        text: data.get("text")
        },broadcast = True)

#@app.before_request 
#def before_request(): 
#    global user_no 
#    if 'session' in session and 'user-id' in session: 
#        pass 
#    else: 
#        session['session'] = os.urandom(24) 
#        session['username'] = 'user'+str(user_no) 
#        user_no += 1

#
#@socketio.on("chat") 
#def request(message): 
#    emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
#       
#        socket.emit('chat', {
#            state: 'chat',
#            name: nickname,
#            text: inputMessage
#        })

if __name__ == '__main__': 
    #socketio.run(app)
    socketio.run(app, host = "54.180.113.181", port=5000)
