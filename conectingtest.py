import asyncio;
# �� ���� ����� �����Ѵ�.
import websockets;
# Ŭ���̾�Ʈ ������ �Ǹ� ȣ��ȴ�.

async def accept(websocket, path):
    while True:
        # Ŭ���̾�Ʈ�κ��� �޽����� ����Ѵ�.
        data = await websocket.recv();
        json_data = json.loads(data)
        playername = json_data["player"]
        print(playername)
        # Ŭ���ξ�Ʈ�� echo�� �ٿ��� �� �����Ѵ�.
        await websocket.send(data);

# �� ���� ���� ����.ȣ��Ʈ�� localhost�� port�� 3000�� �����Ѵ�.
start_server = websockets.serve(accept, "localhost", 3000);

# �񵿱�� ������ ����Ѵ�.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();
