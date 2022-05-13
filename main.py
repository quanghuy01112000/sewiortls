import numpy as np
import asyncio
import jmespath
import json
import websockets
import time
import array as arr
from matplotlib import pyplot as plt, cm
from matplotlib.widgets import Button, RadioButtons
from scipy.ndimage import gaussian_filter
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
    a[0].clear()
    print("yolo")
    a[0].scatter(x, y, label='anchor', color='g')
    readTag()
    a[0].invert_yaxis()
    a[0].legend()
    a[1].invert_yaxis()
    # ax.draw()


def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent


def readTag():
    timeout = time.time() + 10
    loop = asyncio.get_event_loop()

    headmapid = 12
    xheadmap = arr.array('d',[])
    yheadmap = arr.array('d',[])
    h = 0
    for anchor in arrayAnchor:
        if not anchor.getIsMaster():
            h = h + 1
            print('not master', anchor.getCurrentValuePosX(), anchor.getCurrentValuePosY())
            xheadmap.append(float(anchor.getCurrentValuePosX()))
            yheadmap.append(float(anchor.getCurrentValuePosY()))
        # if h == 5:
            # break

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
                    a[0].scatter(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor())
                    a[0].plot(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor(),
                              label=str(tag.getID()))
                    print(tag.getID())
                    print(arrayTag[0].getID())
                    xheadmap.append(data[1])
                    yheadmap.append(data[2])
                    img, extent = myplot(xheadmap, yheadmap, 64)
                    a[1].imshow(img, extent=extent, origin='lower', cmap=cm.jet)
                elif str(data[0]) == str(tag.getID()):
                    tag.addXCoordinates(data[1])
                    tag.addYCoordinates(data[2])
                    a[0].scatter(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor())
                    a[0].plot(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), color=tag.getColor())
                    print(tag.getID())
                    print(arrayTag[0].getID())
                    xheadmap.append(data[1])
                    yheadmap.append(data[2])
                    img, extent = myplot(xheadmap, yheadmap, 64)
                    a[1].imshow(img, extent=extent, origin='lower', cmap=cm.jet)
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
    arrayTag[i].setColor(color[indexColor - 1])
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
fig, ax = plt.subplots(2, 1)
# ax.invert_yaxis()
plt.subplots_adjust(left=0.3)
a = ax.flatten()
# ax.scatter(x, y, label='anchor', color='g')
axcut_show_anchor = plt.axes([0.05, 0.7, 0.15, 0.10])
bcut_show_anchor = Button(axcut_show_anchor, 'Show', color='g', hovercolor='y')
bcut_show_anchor.on_clicked(show)

# adjust radio buttons
axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.2, 0.15, 0.50],
               facecolor=axcolor)
arrayid = []
for tag in arrayTag:
    arrayid.append(tag.getID())
radio = RadioButtons(rax, arrayid,
                     [True, False, False, False],
                     activecolor='r')


def colorChange(labels):
    print(labels)
    for tag in arrayTag:
        if labels == tag.getID():
            print(tag.getTitle())
            # a[1].scatter(x, y, color='r')
            img, extent = myplot(tag.getList_X_coordinates(), tag.getList_Y_coordinates(), 64)
            a[1].imshow(img, extent=extent, origin='lower', cmap=cm.jet)




radio.on_clicked(colorChange)

# ax.set_title('huy')
# ax.invert_xaxis()
# ax.invert_yaxis()
# ax.legend()
plt.show()
