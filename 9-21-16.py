# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:48:33 2016

@author: Graham Cooke
"""

from turtle import *

screen = Screen()

screen.bgcolor("blue")

t = Turtle()

for i in range(3):
    
    t.forward(50)
    t.left(60)
    t.forward(50)
    t.left(150)
    t.forward(86.6)
    t.right(180)
    t.forward(86.6)
    t.left(90)


t.right(90)
t.forward(43.3)

t.right(120)

t.forward(43.3)
t.left(120)
t.forward(43.3)
t.left(120)
t.forward(43.3)



t.hideturtle()

screen.exitonclick()