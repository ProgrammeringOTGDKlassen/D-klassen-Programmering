'''
Bezier curve python implementation by TimeTraveller.
(https://github.com/TimeTraveller-San)
Bezier curve was discovered by the French engineer Pierre Bézier.

>> Set the control points by changing points.txt file

>> Parameters:
    - Speed: controls how fast will the plot be plotted
    - n: controls number of points we are plotting (higher the number, higher
      the resolution of the plot

>> Run mplot.py to actually plot the curve

>> Crude output points are stored in bpoints.txt. This is the file later read
   by matplot in mplot.py file to plot the curve

'''

import numpy as np
import pandas as pd
import math
import time

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def c(k, n, t):
    return nCr(n,k)*(t**k)*((1-t)**(n-k))

class BezeirPoints():
    def clear_file(self):
        with open("bpoints.txt",'w+') as handle:
            handle.write("")

    def __init__(self, interval, speed=200):
        self.speed = speed
        self.control_points = pd.read_csv('points.txt', header=None)
        if self.control_points.shape[1] != 2:
            print("\n!! These many dimensions not supported !!\n")
            return
        self.n = self.control_points.shape[0] - 1
        self.interval = interval
        self.clear_file()

    def write_file(self,point):
        with open('bpoints.txt', 'a') as f:
            spoint = f"{point[0]},{point[1]}\n"
            f.write(spoint)

    def generate(self):
        n = self.n
        df = pd.DataFrame()
        for t in range(self.interval+1):
            t = t/self.interval
            # print(t)
            bpoint = [0, 0]
            for k in range(n+1):
                pk = self.control_points.iloc[k]
                constant = c(k, n, t)
                bpoint[0] += pk[0]*constant
                bpoint[1] += pk[1]*constant
            bpoint[0] = "{:.2f}".format(bpoint[0])
            bpoint[1] = "{:.2f}".format(bpoint[1])
            self.write_file(bpoint)
            time.sleep(1/self.speed)

if __name__ == "__main__":
    n = 1000 #The
    speed = 300
    BezeirPoints(n, speed=speed).generate()
