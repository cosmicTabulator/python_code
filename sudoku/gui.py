# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:26:21 2016

@author: Graham Cooke
"""

import tkinter
import solver
import logging

logger = logging.getLogger("Gui")
logger.setLevel(logging.DEBUG)

def getProblem():
    solver.wipe()
    solver.generate()
    make()

def make():
    b = tkinter.Button(root,text = "Create")
    b["command"] = getValue
    b.pack(side = "bottom")
    
def getValue():
    value = 0
    try:
        value = int(e.get())
        if( value < 30 or value > 80):
            t["text"] = "Please enter a number between 30 and 81"
        else:
            unsolved = solver.unsolve(value)
            logger.debug("Returned")
            display(unsolved)
    except:
        t["text"] = "Please Enter a number"
    return   

def ask():
    value = 0
    while value < 30 or value > 80:
        t["text"] = "Please enter a value between 30 and 81"
        try:
            value = int(e.get())
        except:
            t["text"] = "Please enter a number"
    return value
    
def display(u):
    d = []
    line = 0
    l = 0
    logger.debug("Entered")
    logger.debug(u)
    print(" ------- ------- -------")
    for x in solver.indexes:
        logger.debug("Line " + str(x))
        numbers = ()
        for y in solver.indexes:
            numbers = numbers + (u[x+y],)
            logger.debug("Y " + str(y))
        logger.debug(numbers)
        d[l]["text"] = ("| {0:1} {1:1} {2:1} | {3:1} {4:1} {5:1} | {6:1} {7:1} {8:1} |".format(*numbers))
        logger.debug("Printed Line " + str(x))
        line += 1
        l += 1
        if ((line % 3) == 0 and line != 9):
            d[l]["text"] = " -------+-------+-------"
    logger.debug("Printed?")
    d[l]["text"] = " ------- ------- -------"
    for l in range(len(d)):
        d[l].pack()
        logger.debug(d[l])

root = tkinter.Tk()

root.wm_minsize(width = 500, height = 400)
root.wm_maxsize(width = 500, height = 600)

c = tkinter.Button(root, text = "Create a Puzzle", command = getProblem, width = 15)
c.pack(side = "top")
s = tkinter.Button(root, text = "Solve a Puzzle", command = root.destroy, width = 15)
s.pack(side = "top")

t = tkinter.Label(root)
t.pack()

p = tkinter.Label(root, text = "123|456|789")
p.pack()

e = tkinter.Entry(root)
e.pack()

q = tkinter.Button(root, text = "Quit", command = root.destroy)
q.pack()

d = [tkinter.Label(root, text = "|") for x in range(13)]
for l in range(len(d)):
    d[l]["text"] = "{}".format("1")
    d[l].pack()
    logger.debug(d[l])

while True:
    root.mainloop()