import numpy as np
import bezier
import matplotlib.pyplot as plt
import seaborn


nodes1 = np.asfortranarray([[0.0, 0.5, 1.0], [0.0, 1.0, 0.0]])
curve1 = bezier.Curve(nodes1, degree=2)

nodes2 = np.asfortranarray([[0.0, 0.25,  0.5, 0.75, 1.0], [0.0, 2.0 , -2.0, 2.0 , 0.0]])
curve2 = bezier.Curve.from_nodes(nodes2)
intersections = curve1.intersect(curve2)
# print(intersections)

s_vals = np.asfortranarray(intersections[0, :])
points = curve1.evaluate_multi(s_vals)
# print(points)

seaborn.set()

ax = curve1.plot(num_pts=256)
_ = curve2.plot(num_pts=256, ax=ax)
lines = ax.plot(points[0, :], points[1, :], marker="o", linestyle="None", color="black")
_ = ax.axis("scaled")
_ = ax.set_xlim(-0.125, 1.125)
_ = ax.set_ylim(-0.0625, 0.625)
plt.show()