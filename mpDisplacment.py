# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:08:11 2016

@author: Graham Cooke
"""

import matplotlib.pyplot as pyt

import random

pt = [(-1,0), (1,0)]

def displace(points, d):
    newPoints = []
    for x in range(len(points)-1):
        newPoints.append(points[x])
        
        rand = random.uniform(-d,d)
        
        nPoint = ((points[x][0]+points[x+1][0])/2, ((points[x][1]+points[x+1][1])/2) + rand)
        
        newPoints.append(nPoint)
    newPoints.append(points[-1])
    return newPoints

for n in range(8):
    pt = displace(pt, 1/((n+1)**3))

print(pt)

xVals = []
yVals = []

for x in range(len(pt)):
    xVals.append(pt[x][0])
    yVals.append(pt[x][1])
    
pyt.plot(xVals, yVals)
pyt.axes([-1,1,-1,1])
pyt.show



