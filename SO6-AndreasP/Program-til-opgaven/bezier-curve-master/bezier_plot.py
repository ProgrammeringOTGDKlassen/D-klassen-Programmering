'''
Bezier curve python implementation by TimeTraveller.
(https://github.com/TimeTraveller-San)
Bezier curve was discovered by the French engineer Pierre Bézier.

>> Parameters:
    NONE

Course of action:
1. run bezier_plot.py
2. see the curve
3. change control points in points.txt
4. run bezier_calculate (change Parameters such as speed and resolution here)
5. see the curve being plotted livez
6. either go back to step 3 or exit

(Better interactive implementation coming soon, this stupid hack is cheezy)
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import scipy.interpolate as interpolate
import numpy as np
import pandas as pd
style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def points():
    control_points = pd.read_csv('points.txt', header=None)
    return (
            int(control_points.max().max()+1),
            int(control_points.min().min()-1),
            control_points,
            )

def animate(i):
    lines = open("bpoints.txt",'r').readlines()
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    axes = plt.gca()
    max, min, control_points = points()
    axes.set_xlim([min,max])
    axes.set_ylim([min,max])
    color =  np.array([0.7,0,0.5])
    ax1.plot(xs, ys, c=color, linewidth=1)
    ax1.scatter(control_points[0], control_points[1], c="b")
    for i in range(control_points.shape[0]):
        ax1.annotate(f"P{i}", (control_points[0][i], control_points[1][i]))

an1 = animation.FuncAnimation(fig, animate, interval=1)
plt.show()
