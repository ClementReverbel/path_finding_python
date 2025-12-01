#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 08:27:56 2021

@author: fehrenbach

TEST DU FAST MARCHING

"""

import matplotlib.pyplot as plt
import numpy as np
import lib_trajectoires as traj
import time
import imageio



nx = 200
ny = 250


### test 1
#W = np.ones((nx,ny))
x0=[100,10]
target = [100,190]
##
# test 2
x = np.arange(nx)-0.5*nx
y = np.arange(ny)-0.5*nx
sigma = 10
xg, yg = np.meshgrid(x,y)
## cas 1
W = np.ones((nx,ny))
## cas 2
#W = np.ones((nx,ny))
W[np.where(xg**2+yg**2<20**2)] = 10
## cas 3 labyrinthe
u = imageio.imread('labyrinthe002.jpg')
uu = np.sum(u,axis=2)
nx = np.shape(uu)[0]
ny = np.shape(uu)[1]
W = np.ones((nx,ny))
W[np.where(uu<300)] = 500
x0=[45,10]
target = [208,270]




plt.figure(2)
plt.imshow(W)
#%%
t1 = time.time()
d,px,py,t = traj.dijkstra_grille(W,x0[0],x0[1])
t2 = time.time()
chrono = t2-t1
print(' --- temps : ',chrono)

plt.figure(1)
plt.contourf(d,20,cmap='jet')
plt.colorbar()
plt.contour(d,20,colors='k')
#%%

plt.figure(3)
plt.imshow(W)
### descente
scourant = target
while not(scourant==x0):
    plt.plot(scourant[1],scourant[0],'r.')
    scourant = [px[scourant[0],scourant[1]],py[scourant[0],scourant[1]]]

