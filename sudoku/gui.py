# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:26:21 2016

@author: Graham Cooke
"""

import tkinter
import solver
import logging
from PIL import Image,ImageDraw
from tkinter import filedialog as fd
import os
import copy

#Create a logging mechanism
logger = logging.getLogger("Gui")
logger.setLevel(logging.DEBUG)

puzzle = {}
empty = []
solved = []

#Has the solver create a solved sudoku problem and cleans the canvas
def getProblem():
    #Clear the canvas
    d.delete("all")
    
    draw.rectangle([(0, 0), (300, 300)], fill = "white")
    #Create the box lines
    d.create_line(100, 0, 100, 300)
    d.create_line(200, 0, 200, 300)
    d.create_line(0, 100, 300, 100)
    d.create_line(0, 200, 300, 200)
    
    draw.line([(100, 0), (100, 300)], width = 1, fill = "black")
    draw.line([(200, 0), (200, 300)], width = 1, fill = "black")
    draw.line([(0, 100), (300, 100)], width = 1, fill = "black")
    draw.line([(0, 200), (300, 200)], width = 1, fill = "black")
    
    e.delete(0, 'end')
    
    #Reset the solver
    solver.wipe()
    #Create a new solved puzzle
    solver.generate()
    #Reveal the create Button
    b.grid()
    #Ask the user
    t["text"] = "Please enter the number of given clues you would like"

#Retreives the number of givens from the user
def getValue():
    global puzzle
    value = 0
    try:
        value = int(e.get())
        #If the entered number exceeds reasonable bounds, tell them
        if value < 30 or value > 80:
            t["text"] = "Please enter a number between 30 and 81"
        #Otherwise, 'unsolve' the before created problem and display it
        else:
            unsolved = solver.unsolve(value)
            logger.debug("Returned")
            display(unsolved)
            puzzle = unsolved
            t["text"] = ""
    #If the user entered a non-number, tell them
    except:
        t["text"] = "Please Enter a number"
    return

#Display the unsolved problem on the canvas
def display(u):
    logger.debug(u)
    #Iterates through the unsolved puzzle, drawing text on the canvas to match
    for x in solver.indexes:
        logger.debug("x:" + x)
        for y in solver.indexes:
            logger.debug("y:" + y)
            d.create_text((int(x)+1)*30, (int(y)+1)*30, text = u[x+y])
            draw.text(((int(x)+1)*30, (int(y)+1)*30),text = u[x+y], fill = "black")
            logger.debug(u[x+y])
    #Hides the create button again
    b.grid_remove()
    s.grid()
    p.grid()
    
def savePuzzle():

    usrPath = fd.askdirectory()
    index = 00000
    while(os.path.isfile(usrPath + "/Puzzle" + str(index) + ".jpg")):
        index += 1
        
    image.save(usrPath + "/Puzzle" + str(index) + ".jpg")
    s.grid_remove()

def getNumber():
    value = 0
    try:
        value = int(e.get())
        #If the entered number exceeds reasonable bounds, tell them
        if value < 30 or value > 80:
            t["text"] = "Please enter a number between 30 and 81"
        #Otherwise, 'Ready teh Button for a second Input
        else:
            
            m["command"] = lambda :buildMultiple(value)
            t["text"] = "Please Enter the number of Puzzles"
    #If the user entered a non-number, tell them
    except:
        t["text"] = "Please Enter a number"
    return
    
def buildMultiple(given):
    value = 0
    try:
        value = int(e.get())
        
        if value > 20:
            t["text"] = "Please Enter a smaller value"
        
        usrPath = fd.askdirectory()
        for x in range(value):
            solver.wipe()
            solver.generate()
            unsolved = solver.unsolve(given)
            logger.debug("Returned")

            for x in solver.indexes:
                logger.debug("x:" + x)
                for y in solver.indexes:
                    logger.debug("y:" + y)
                    draw.text(((int(x)+1)*30, (int(y)+1)*30),text = unsolved[x+y], fill = "black")
            index = 0
            while(os.path.isfile(usrPath + "/Puzzle" + str(index) + ".jpg")):
                index += 1

            image.save(usrPath + "/Puzzle" + str(index) + ".jpg")
            
            draw.rectangle([(0, 0), (300, 300)], fill = "white")
            draw.line([(100, 0), (100, 300)], width = 1, fill = "black")
            draw.line([(200, 0), (200, 300)], width = 1, fill = "black")
            draw.line([(0, 100), (300, 100)], width = 1, fill = "black")
            draw.line([(0, 200), (300, 200)], width = 1, fill = "black")
    except:
        t["text"] = "Please enter a Number"
    return
    
def solve():
    global puzzle
    global empty
    global solved
    d.grid_remove()
    b.grid_remove()
    s.grid_remove()
    for x in solver.indexes:
        for y in solver.indexes:
            g[x+y].grid()
            g[x+y].insert(0, puzzle[x+y])
            if g[x+y].get() != "":
                g[x+y].grid_remove()
                f[x+y].grid()
                f[x+y]["text"] = str(puzzle[x+y])
    solved.clear()
    empty = solver.mult(solver.indexes, solver.indexes)
    for i,v in puzzle.items():
        if v != "":
            solved.append(i)
    for i in solved:
        empty.pop(empty.index(i))
    k.grid()
    return
    
def check():
    global empty
    global solved
    for k in empty:
        i = g[k].get()
        if i == solver.grid[k]:
            g[k].grid_remove()
            f[k].grid()
            f[k]["text"] = solver.grid[k]
            solved.append(k)
            empty.pop(empty.index(k))
        else:
            g[k].delete(0, 'end')
    if len(empty) == 0:
        t["text"] = "Solved!"
        k.grid_remove()
    
#Create a master window for the GUI
root = tkinter.Tk()

#Create a Create Puzzle button and bind it to the getProblem function
c = tkinter.Button(root, text = "Create a Puzzle", command = getProblem, width = 15)
c.grid(columnspan = 13)

m = tkinter.Button(root, text = "Create Multiple Puzzles", command = getNumber)
m.grid(columnspan = 13)

#Create an empty text space for later
t = tkinter.Label(root)
t.grid(columnspan = 13)

#Create an entery box
e = tkinter.Entry(root)
e.grid(columnspan = 13)

#Create a quit button to close the window
q = tkinter.Button(root, text = "Quit", command = root.destroy)
q.grid(columnspan = 13)

#Create a canvas to draw the unsolved puzzle on
d = tkinter.Canvas(root, width = 300, height = 300)
d.grid(columnspan = 13)

image = Image.new("RGB", (300, 300), color = "white")
draw = ImageDraw.Draw(image)

#Create the box lines for the puzzle
d.create_line(100, 0, 100, 300)
d.create_line(200, 0, 200, 300)
d.create_line(0, 100, 300, 100)
d.create_line(0, 200, 300, 200)
    
draw.line([(100, 0), (100, 300)], width = 1, fill = "black")
draw.line([(200, 0), (200, 300)], width = 1, fill = "black")
draw.line([(0, 100), (300, 100)], width = 1, fill = "black")
draw.line([(0, 200), (300, 200)], width = 1, fill = "black")

g = {i : tkinter.Entry(root, width = 1) for i in solver.mult(solver.indexes, solver.indexes)}

for y in solver.indexes:
    for x in solver.indexes:
        g[x+y].grid(column = int(x), row = int(y)+8)
        g[x+y].grid_remove()
        
f = {i : tkinter.Label(root, width = 1) for i in solver.mult(solver.indexes, solver.indexes)}

for y in solver.indexes:
    for x in solver.indexes:
        f[x+y].grid(column = int(x), row = int(y)+8)
        f[x+y].grid_remove()
        
#Create and hide the create button
b = tkinter.Button(root,text = "Create")
b["command"] = getValue
b.grid(columnspan = 13)
b.grid_remove()

s = tkinter.Button(root,text = "Save")
s["command"] = savePuzzle
s.grid(columnspan = 13)
s.grid_remove()

p = tkinter.Button(root, text = "Solve")
p["command"] = solve
p.grid(columnspan = 13)
p.grid_remove()

k = tkinter.Button(root, text = "Check")
k["command"] = check
k.grid(columnspan = 13)
k.grid_remove()

#Run the GUI
root.mainloop()
