import asyncio
import time

import jmespath
import json
import websockets
from websocket import create_connection

# timeout = time.time() + 20
# ws = create_connection("ws://192.168.225.2")
# while True:
#     if time.time() > timeout:
#         print('exit')
#         break
#     # open socket
#     ws.send(
#         '{"headers":{"X-ApiKey":"171555a8fe71148a165392904"},"method":"subscribe", "resource":"/feeds/"}')  # send to socket
#     # ws.recv()  # receive from socket
#     response = ws.recv()
#     # ws.close()  # close socket
#     # await websocket.send(
#     #     '{"headers":{"X-ApiKey":"171555a8fe71148a165392904"},"method":"subscribe", "resource":"/feeds/"}')
#     # response = await websocket.recv()
#     data = json.loads(response)
#     # print(data)
#
#     try:
#         data = jmespath.search(
#             "body.[id ,(datastreams[?id=='posX'].current_value | [0]), (datastreams[?id=='posY'].current_value | [0])]",
#             data)
#         data[0], data[1], data[2] = int(data[0]), float(data[1]), float(data[2])
#     except Exception:
#         print ('None')
#     print (data)
#     time.sleep(0.5)
# ws.close()

async def hello():
    # async with websockets.connect("ws://192.168.225.2") as websocket:
    timeout = time.time() + 20
    ws = create_connection("ws://192.168.225.2")
    while time.time() < timeout:
          # open socket
        ws.send('{"headers":{"X-ApiKey":"171555a8fe71148a165392904"},"method":"subscribe", "resource":"/feeds/"}')  # send to socket
        # ws.recv()  # receive from socket
        response = await ws.recv()
        # ws.close()  # close socket
        # await websocket.send(
        #     '{"headers":{"X-ApiKey":"171555a8fe71148a165392904"},"method":"subscribe", "resource":"/feeds/"}')
        # response = await websocket.recv()
        data = json.loads(response)

        allTag = {}
        print(data)
        try:
            data = jmespath.search(
                "body.[id ,(datastreams[?id=='posX'].current_value | [0]), (datastreams[?id=='posY'].current_value | [0])]",
                data)
            data[0], data[1], data[2] = int(data[0]), float(data[1]), float(data[2])
        except Exception:
            return None
        return data
    ws.close()
#
data = asyncio.run(hello())

# while True:
#     data = asyncio.get_event_loop().run_until_complete(hello())
asyncio.close()
if data != None:
    print(data)