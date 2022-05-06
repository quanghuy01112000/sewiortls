import asyncio
import time

import jmespath
import json

import numpy as np
import websockets
from matplotlib import pyplot as plt, cm
from matplotlib.widgets import Button
from scipy.ndimage import gaussian_filter
from websocket import create_connection

from Models.Tag import Tag


async def runTag():
    async with websockets.connect("ws://demo.sewio.net") as websocket:
        await websocket.send(
            '{"headers":{"X-ApiKey":"171555a8fe71148a165392904"},"method":"subscribe", "resource":"/feeds/14"}')
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

def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

# plt.connect('button_press_event', start)
fig, ax = plt.subplots(2, 1)
# ax.invert_yaxis()
plt.subplots_adjust(left=0.3)
x,y = [], []
def read():
    while True:
        data = asyncio.get_event_loop().run_until_complete(runTag())
        timeout = time.time() + 10
        # asyncio.close()
        if data != None:
            print(data)
            # for tag in arrayTag:
                # print(data[0], tag.getID())
            tag = Tag()


            x.append(data[1])
            y.append(data[2])
            a = ax.flatten()
            a[0].scatter(x, y, color='r')
            a[0].plot(x, y, color='r',
                    label=str(tag.getID()))

            img, extent = myplot(x, y, 64)
            a[0].imshow(img, extent=extent, origin='lower', cmap=cm.jet)
            if time.time() > timeout:
                # loop.stop()
                # loop.

                print('break')
                return
            plt.pause(0.5)

def show(event):
    read()
axcut_show_anchor = plt.axes([0.05, 0.7, 0.15, 0.10])
bcut_show_anchor = Button(axcut_show_anchor, 'Show Anchor', color='g', hovercolor='y')
bcut_show_anchor.on_clicked(show)

plt.show()