import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


# creating an array starting from
# 0 to 1 with step size 0.01
t = np.arange(0.0, 1.0, 0.01)

# the values of sin values of t
s0 = np.sin(2*np.pi*t)

# depict visualization
fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color='red')
plt.subplots_adjust(left=0.3)

# adjust radio buttons
axcolor = 'lightgoldenrodyellow'
rax = plt.axes([0.05, 0.4, 0.15, 0.30],
			facecolor=axcolor)

radio = RadioButtons(rax, ['red', 'blue', 'green'],
					[True,False,False,False],
					activecolor='r')

def colorChange(labels):
	l.set_color(labels)
	fig.canvas.draw()

radio.on_clicked(color)

plt.show()
