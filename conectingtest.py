import asyncio;
# 웹 소켓 모듈을 선언한다.
import websockets;
# 클라이언트 접속이 되면 호출된다.

async def accept(websocket, path):
    print("conecting...")
    while True:
        # 클라이언트로부터 메시지를 대기한다.
        data = await websocket.recv();
        # 돌아가는지만 확인해보자 ㅠㅠ 어디서 오니 정보야 ㅠㅠㅠ
        json_data = json.loads(data)
        playername = json_data["player"]
        print(playername)
        
        # 클라인언트로 echo를 붙여서 재 전송한다.
        await websocket.send(data);

# 웹 소켓 서버 생성.호스트는 3.35.24.169에 port는 3000로 생성한다.
start_server = websockets.serve(accept, "3.35.24.169", 3000);

# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();
