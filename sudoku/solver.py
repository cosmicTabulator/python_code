# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:33:57 2016

@author: Graham Cooke
"""

#PS Future self: remember to comment (;
import random
import logging
import copy
import time
#import gui

#Algebraicly multiply two lists together
def mult(list1,list2):
    out = []
    for a in list1:
        for b in list2:
            out.append(a+b)
    return out

start1 = time.time()
start2 = 0
logger = logging.getLogger("Solver")
logging.basicConfig(level=logging.DEBUG)
## Start Main Code ##
#Establish indexes for the sudoku grid and create the grid using these
#Define lists to contain empty spaces and completed spaces
indexes = "012345678"
indexC1 = "012"
indexC2 = "345"
indexC3 = "678"
numbers = "123456789"
full = mult(indexes,indexes)
empty = []
chosen = []
end1 = 0
end2 = 0
unsolved = 0

#Return a list of spaces in a row given a space in that row, excluding the given space
def row(k):
    m = mult(indexes,k[1])
    out = []
    for e in m:
        if e != k:
            out.append(e)
    return out

#Same as above, with columns
def col(k):
    m = mult(k[0],indexes)
    out = []
    for e in m:
        if e != k:
            out.append(e)
    return out

#Same as above, with cells
def cel(k):
    m = checkCell(k)
    out = []
    for e in m:
        if e != k:
            out.append(e)
    return out

def checkCell(k):
      xC = (int(k[0]) // 3)
      yC = (int(k[1]) // 3)
  
      if(xC is 0):
          xC = indexC1
      elif(xC is 1):
          xC = indexC2
      else:
          xC = indexC3
      if(yC is 0):
          yC = indexC1
      elif(yC is 1):
          yC = indexC2
      else:
          yC = indexC3
  
      return (mult(xC,yC))

#Define a dictionary mapping coordinates of each space to all possible values at that space
grid = {k : "" for k in mult(indexes,indexes)}
#Define a dictionary mapping a space to all spaces that effect it (are in the same row column or cell as it)
related = {k : (row(k) + col(k) + cel(k)) for k in mult(indexes,indexes)}
n = 0
l = 0
    
#Chech all the spaces related to the given space to see if they also have the same number as k
def checkSpace(n,k,table):
    neighbors = []
    for i in related[k]:
        if i not in empty:
            neighbors.append(table[i])
    if n in neighbors:
        return False
    else:
        return True

def poss(table):
    for k in empty:
        for n in numbers:
            if checkSpace(n,k,table):
                table[k] = table[k] + n

def search(table):
    reduced = False
    for k in empty:
        if len(table[k]) is 1:
            reduced = True
            reduce(table[k],k,table)
            empty.pop(empty.index(k))
        for n in table[k]:
            isolated = True
            for r in row(k):
                if n in table[r]:
                    isolated = False
            if isolated:
                reduced = True
                table[k] = n
                reduce(n,k,table)
                break
            isolated = True
            for c in col(k):
                if n in table[c]:
                    isolated = False
            if isolated:
                reduced = True
                table[k] = n
                reduce(n,k,table)
                break
            isolated = True
            for c in cel(k):
                if n in table[c]:
                    isolated = False
            if isolated:
                reduced = True
                table[k] = n
                empty.pop(empty.index(k))
                reduce(n,k,table)
                break
    return reduced

def reduce(n,k,table):
    for s in related[k]:
        table[s] = table[s].replace(n,"")
        
def getEmpty(table):
    empty.clear()
    for k in full:
        if (table[k] == "") or len(table[k]) > 1:
            empty.append(k)
    poss(table)
    
def wipe():
    for k in full:
        grid[k] = ""

def getChosen(table):
    chosen.clear()
    for k in table:
        if len(table[k]) == 1:
            chosen.append(k)

def isSolvable(tableIn):
    table = copy.deepcopy(tableIn)
    getEmpty(table)
    poss(table)
    ticks = 0
    while(search(table)):
        ticks += 1
    logger.debug("Took " + str(ticks) + " ticks")
    for k in table:
        if k[0] is not ('r' or 'c' or 's'):
            if table[k] == "":
                logger.debug("No Poss on " + k)
                return False
            if len(table[k]) > 1:
                logger.debug("Still Left on" + k)
                return False
    return True

def loading():
    global l
    l+=1
    if l > 4:
        l = 1
    if l == 1:
        print('|')
        return
    if l == 2:
        print('/')
        return
    if l == 3:
        print('-')
        return
    if l == 4:
        print('\\')
        return

#Fill the list of empty spaces from the current sudoku grid
def generate():
    global grid
    getEmpty(grid)
    #While there are still empty spaces in the grid
    times = 0
    numberEmpty = 0
    while len(empty) > 0:
        #Pick a random empty space
        k = random.choice(empty)
        logger.debug(k)
        #Fill the space with a random number from its list of possible numbers
        n = random.choice(grid[k])
        #Create a "backup copy" of the sudoku grid
        backup = copy.deepcopy(grid)
        logger.debug(n)
        grid[k] = n
        t = 0
        loading()
        #Solve the grid as much as possible based on the new number
        while(search(grid)):
            t += 1
            logger.debug(str(t) + " Ticks")
        #Go through the grid looking for empty spaces with no possible number
        for e in grid:
            #If we find a space with no possible numbers...
            if grid[e] == '':
                #If we've failed to fill in a new number 2 times in a row
                if times > 1:
                    #Clear the grid and start over
                    logger.debug("Restarted")
                    wipe()
                    getEmpty(grid)
                    times = 0
                    break
                #If we tried and failed to fill in a number last time...
                if len(empty) == numberEmpty:
                    #Keep track
                    times += 1
                    logger.debug("Repeat")
                else:
                    times = 0
                numberEmpty = len(empty)
                #Go back to how the grid was before and try again
                logger.debug("Backtracked")
                grid = copy.deepcopy(backup)
                logger.debug(str(len(empty)) + " are Empty")
                logger.debug("Number Empty: " + str(numberEmpty))
                logger.debug(times)
                getEmpty(grid)
                poss(grid)
                break
            
    logger.debug("Grid")
    logger.debug(grid)
    line = 0
    #Print out the solved grid to the debug console
    for x in indexes:
        numbers = ()
        for y in indexes:
            numbers = numbers + (grid[x+y],)
        logger.info("{0:9} {1:9} {2:9} | {3:9} {4:9} {5:9} | {6:9} {7:9} {8:9}".format(*numbers))
        line += 1
        if (line % 3) == 0:
            logger.info("")
    
    end1 = time.time()
    
    #Ask for the number of provided spaces, make sure they're between 30 and 81
def unsolve(remove):
        
    start2 = time.time() 
    
    #Create unsolved and template copies of the grid to work with
    unsolved = copy.deepcopy(grid)
    template = copy.deepcopy(grid)
    logger.debug(isSolvable(unsolved))
        
    remove = 81 - remove
    r = 0
    #While we haven't cleared the number of spaces we need to...
    while r < remove:
        #Find our solved spaces
        getChosen(unsolved)
        #Pick a filled space randomly and clear it
        k = random.choice(chosen)
        n = template[k]
        template[k] = ""
        unsolved = copy.deepcopy(template)
        loading()
        #If the puzzle still has a solution (that can be arrived at without guessing)
        if(isSolvable(unsolved)):
            #Increment our counter
            logger.debug(True)
            r += 1
            logger.debug("R = " + str(r))
        #If the puzzle doesn't have a solution anymore
        else:
            #Reset the space
            logger.debug(False)
            logger.debug("R = " + str(r))
            template[k] = n
            
    #Print the new, unsolved puzzle to the console
    line = 0
    print(" ------- ------- -------")
    for x in indexes:
        numbers = ()
        for y in indexes:
            numbers = numbers + (unsolved[x+y],)
        print("| {0:1} {1:1} {2:1} | {3:1} {4:1} {5:1} | {6:1} {7:1} {8:1} |".format(*numbers))
        line += 1
        if ((line % 3) == 0 and line != 9):
            print(" -------+-------+-------")
    print(" ------- ------- -------")
          
    #Debug code to track the time the program takes to run
    end2 = time.time()
    return unsolved

def stats():
    
    first = str(end1 - start1)
    last = str(end2 - start2)
    elapsed = float(first) + float(last)
    minutes = str(elapsed // 60)
    rseconds = str(elapsed % 60)
    logger.debug(elapsed)
    logger.debug('Took ' + minutes + ' minutes and ' + rseconds + ' seconds')
    logger.debug('First: ' + first)
    logger.debug('Last: ' + last)