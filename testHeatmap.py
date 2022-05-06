import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage import gaussian_filter


def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent


fig, axs = plt.subplots(1, 1)

# Generate some test data
x = np.random.randn(1000)
y = np.random.randn(1000)

# sigmas = [0, 16, 32, 64]

# for ax in axs.flatten():
#     img, extent = myplot(x, y, 64)
#     ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
#     ax.set_title("Smoothing with  $\sigma$ = %d" % 64)
img, extent = myplot(x, y, 64)
axs.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
axs.set_title("Smoothing with  $\sigma$ = %d" % 64)
plt.show()