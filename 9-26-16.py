# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:23:38 2016

@author: Graham Cooke
"""

from turtle import *

directionsOut = ''
directionsBase = 'FA'
n = 8
l = 5

def iterate(n):
    global directionsOut
    global directionsBase
    for n in range(n):
        for letter in directionsBase:
            if(letter == 'F'):
                directionsOut = directionsOut + 'F'
            elif(letter == 'R'):
                directionsOut = directionsOut + 'R'
            elif(letter == 'L'):
                directionsOut = directionsOut + 'L'
            elif(letter == 'A'):
                directionsOut = directionsOut + 'ARBF'
            elif(letter == 'B'):
                directionsOut = directionsOut + 'FALB'
        directionsBase = directionsOut
        directionsOut = ''

def draw():
    global directionsBase
    global l
    for letter in directionsBase:
        if(letter == 'F'):
            t.forward(l)
        elif(letter == 'R'):
            t.right(90)
        elif(letter == 'L'):
            t.left(90)

screen = Screen()
t = Turtle()
t.speed(100)
iterate(n)
draw()
t.hideturtle()
t.done()
screen.exitonclick()
print(directionsBase)

