import math
import numpy as np
from scipy import integrate
import scipy
import matplotlib.pyplot as plt

plainFunction = "5x"
f = lambda x : 5*x**2 # Remember to correct the definite integral title at sub plot 2
a = 1; b = 5; N = 2 # Grænser og inddelinger
decimals = 4 # Afrundingsfaktor

n = 10 # Use n*N+1 points to plot the function smoothly

def riemannSum(f, plainFunction, a, b, N, n, decimals):
    '''
    Printer venstre, midt og højresummen samt det eksakte integral approximeret som et riemann integral
    '''
    dx = (b-a)/N
    x_left = np.linspace(a,b-dx,N)
    x_midpoint = np.linspace(dx/2,b - dx/2,N)
    x_right = np.linspace(dx,b,N)

    print("Numerisk integration af funktionen", plainFunction, "fra", str(a), "til", str(b), "med",N,"inddelinger")
    left_riemann_sum = np.sum(f(x_left) * dx)
    print("Riemann venstresum:",left_riemann_sum)

    midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
    print("Riemann midtsum:",midpoint_riemann_sum)

    right_riemann_sum = np.sum(f(x_right) * dx)
    print("Riemann højresum",right_riemann_sum)

    i = scipy.integrate.quad(f, a, b)
    print("Eksakt integral:", str(round(i[0], decimals)))
 

    ''' 
    Plotter funtionen samt venstre, midt og højresummer som et riemann integral
    '''
    x = np.linspace(a,b,N+1)
    y = f(x)

    X = np.linspace(a,b,n*N+1)
    Y = f(X)

    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.plot(X,Y,'b')
    x_left = x[:-1] # Left endpoints
    y_left = y[:-1]
    plt.plot(x_left,y_left,'b.',markersize=10)
    plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    plt.title('Riemann venstresum, n = {}, sum = {}'.format(N, round(left_riemann_sum, decimals)))

    plt.subplot(1,3,2)
    plt.plot(X,Y,'b')
    x_mid = (x[:-1] + x[1:])/2 # Midpoints
    y_mid = f(x_mid)
    plt.plot(x_mid,y_mid,'b.',markersize=10)
    plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
    plt.title('{}\nRiemann midtsum, n = {}, sum = {}'.format("$\int_{" + str(round(a, decimals)) + "}^{" + str(round(b, decimals)) + "} " + plainFunction + "\,dx = " + str(round(i[0],decimals)) + "$", N, round(midpoint_riemann_sum, decimals)))

    plt.subplot(1,3,3)
    plt.plot(X,Y,'b')
    x_right = x[1:] # Left endpoints
    y_right = y[1:]
    plt.plot(x_right,y_right,'b.',markersize=10)
    plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
    plt.title('Riemann højresum, n = {}, sum = {}'.format(N, round(right_riemann_sum, decimals)))

    plt.savefig('Riemann plot.png')
    plt.show()

def trapezSum(f, plainFunction, a, b, N, n, decimals):

    i = scipy.integrate.quad(f, a, b)
    exact = str(round(i[0], 4))

    '''
    Plotter funktionen som en trapetz integration
    '''
    x = np.linspace(a, b, N + 1)
    y = f(x)
    X = np.linspace(a, b, n * N + 1)
    Y = f(X)

    plt.plot(X, Y)
    for i in range(N):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, f(x[i]), f(x[i + 1]), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)

    '''
    Summerer trapetz'ernes areal
    '''
    y = f(x)
    y_right = y[1:]  # Right endpoints
    y_left = y[:-1]  # Left endpoints
    dx = (b - a) / N
    A = (dx / 2) * np.sum(y_right + y_left)

    plt.title('{}\nTrapez sum, n = {}, sum = {}'.format("$\int_{" + str(round(a, decimals)) + "}^{" + str(round(b, decimals)) + "} " + plainFunction + "\,dx = " + exact + "$", str(N), str(A)))
    plt.savefig('Trapez plot.png')
    plt.show()

    print("Trapez integral:", str(round(A, decimals)))

trapezSum(f, plainFunction, a, b, N, n, decimals)
riemannSum(f, plainFunction, a, b, N, n, decimals)