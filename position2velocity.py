import numpy as np
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt

pos = np.loadtxt("src_plot_pos.dat", skiprows = 1)

x = pos[:, 0]; y = pos[:, 1]

plt.figure()
plt.plot(pos[:, 0], pos[:, 1])
plt.xlabel("X GPS coordinates")
plt.ylabel("Y GPS coordinates")
plt.show()

with open("src_plot_pos.dat") as f:
	dt = float(f.readline())
	vx = empty(len(pos))
	vy = empty(len(pos))
	vx[0] = vy[0] = 0

for k in range(1, len(pos)):
	vx[k] = (x[k] - x[k - 1]) / dt
	vy[k] = (y[k] - y[k - 1]) / dt

plt.plot(arange(len(pos)) * dt, vx)
plt.plot(arange(len(pos)) * dt, vy)

plt.show()