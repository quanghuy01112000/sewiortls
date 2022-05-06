import random
import matplotlib.pyplot as plt
import numpy as np
import asyncio
import jmespath
import json
import websockets
import time
from matplotlib.widgets import Button
from numpy import mean
from asgiref.sync import sync_to_async
from Controller.ControllerRFID import ControllerRFID


async def runTag():
    async with websockets.connect("ws://demo.sewio.net") as websocket:
        await websocket.send(
            '{"headers":{"X-ApiKey":"171555a8fe71148a165392904"},"method":"subscribe", "resource":"/feeds/"}')
        response = await websocket.recv()
        data = json.loads(response)
        # allTag = {}
        # print(data)
        try:
            data = jmespath.search(
                "body.[id ,(datastreams[?id=='posX'].current_value | [0]), (datastreams[?id=='posY'].current_value | [0])]",
                data)
            data[0], data[1], data[2] = int(data[0]), float(data[1]), float(data[2])
        except Exception:
            return None
        return data



def show(event):
    # ax.clear()
    print("yolo")
    ax.scatter(x, y, label='anchor', color='g')
    readTag()
    ax.invert_yaxis()
    ax.legend()
    # ax.draw()

def readTag():
    timeout = time.time() + 10
    loop = asyncio.get_event_loop()
    while True:
        data = loop.run_until_complete(runTag())
        if data != None:
            print(data)
            for tag in arrayTag:
                # print(data[0], tag.getID())
                if [str(data[0]), tag.getCheck()] == [str(tag.getID()), True]:
                    # print('vo')
                    tag.setCheck(False)
                    tag.addXCoordinates(data[1])
                    tag.addYCoordinates(data[2])
                    ax.scatter(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor())
                    ax.plot(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor(),
                            label=str(tag.getID()))
                elif str(data[0]) == str(tag.getID()):
                    tag.addXCoordinates(data[1])
                    tag.addYCoordinates(data[2])
                    ax.scatter(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor())
                    ax.plot(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor())
        else:
            print('none')
        if time.time() > timeout:
            # loop.stop()
            # loop.
            for tag in arrayTag:
                tag.setCheck(True)
            print('break')
            return
        plt.pause(0.5)
    # ax.draw()


color = ['b', 'r', 'm', 'y', 'c', 'k', 'g']
arrayAnchor = ControllerRFID.getAllAnchorData()
arrayTag = ControllerRFID.getAllTagData()
indexColor = 1;
for i in range(len(arrayTag)):
    arrayTag[i].setColor(color[indexColor-1])
    if indexColor >= 7:
        indexColor = 0
    else:
        indexColor = indexColor + 1


for tag in arrayTag:
    tag.printData()

x = np.zeros((len(arrayAnchor),))
y = np.zeros_like(x)
for i in range(len(arrayAnchor)):
    x[i] = arrayAnchor[i].getCurrentValuePosX()
    y[i] = arrayAnchor[i].getCurrentValuePosY()
    # x.append(anchor.getCurrentValuePosX())
    # y.append(anchor.getCurrentValuePosY())

# plt.connect('button_press_event', start)
ax = plt.subplot(111)
# ax.invert_yaxis()
plt.subplots_adjust(left=0.3)

# ax.scatter(x, y, label='anchor', color='g')
axcut_show_anchor = plt.axes([0.05, 0.7, 0.15, 0.10])
bcut_show_anchor = Button(axcut_show_anchor, 'Show Anchor', color='g', hovercolor='y')
bcut_show_anchor.on_clicked(show)



# ax.set_title('huy')
# ax.invert_xaxis()
# ax.invert_yaxis()
# ax.legend()
plt.show()
