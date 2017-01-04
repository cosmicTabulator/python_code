# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:26:21 2016

@author: Graham Cooke
"""

import tkinter
import solver
import logging

#Create a logging mechanism
logger = logging.getLogger("Gui")
logger.setLevel(logging.ERROR)

#Has the solver create a solved sudoku problem and cleans the canvas
def getProblem():
    #Clear the canvas
    d.delete("all")
    #Create the box lines
    d.create_line(100,0,100,300)
    d.create_line(200,0,200,300)
    d.create_line(0,100,300,100)
    d.create_line(0,200,300,200)
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
            logger.debug(u[x+y])
    #Hides the create button again
    b.grid_remove()

#Create a master window for the GUI
root = tkinter.Tk()

#Create a Create Puzzle button and bind it to the getProblem function
c = tkinter.Button(root, text = "Create a Puzzle", command = getProblem, width = 15)
c.grid(columnspan = 13)

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
#Create the box lines for the puzzle
d.create_line(100,0,100,300)
d.create_line(200,0,200,300)
d.create_line(0,100,300,100)
d.create_line(0,200,300,200)

#Create and hide the create button
b = tkinter.Button(root,text = "Create")
b["command"] = getValue
b.grid(columnspan = 13)
b.grid_remove()

#Run the GUI
root.mainloop()
