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
logging.basicConfig(level=logging.INFO)
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

#Fills up the table with all possible, valid answers for each yet unsolved space
def poss(table):
    for k in empty:
        for n in numbers:
            if checkSpace(n,k,table):
                table[k] = table[k] + n

#Looks through the table for any solutions
def search(table):
    reduced = False
    #Goes through all the empty or unsolved spaces
    for k in empty:
        #If an 'unsolved' space currently has only one possible option
        if len(table[k]) is 1:
            reduced = True
            #Update all it's neighbors possibilities
            reduce(table[k],k,table)
            #Remove it from the list of unsolved spaces
            empty.pop(empty.index(k))
        #Look through the other possible solutions of neighbor spaces
        #If this space has the only instance of a particular number in its possible solutions,
        #That number must be its solution
        for n in table[k]:
            #First, assume this number is a unique instance
            isolated = True
            #Search through this space's row for other instances
            for r in row(k):
                #When we find one, mark that it's not unique
                if n in table[r]:
                    isolated = False
                    break
            #If we found no other instances
            if isolated:
                #Use that number as this space's solution
                reduced = True
                table[k] = n
                reduce(n,k,table)
                break
            #Reset and repeat for the column
            isolated = True
            for c in col(k):
                if n in table[c]:
                    isolated = False
                    break
            if isolated:
                reduced = True
                table[k] = n
                reduce(n,k,table)
                break
            #And the cell
            isolated = True
            for c in cel(k):
                if n in table[c]:
                    isolated = False
                    break
            if isolated:
                reduced = True
                table[k] = n
                empty.pop(empty.index(k))
                reduce(n,k,table)
                break
    #Return whether or not we were able to solve at least one space
    return reduced

#Eliminate possibilities from a space's neighbors based on a found solution
def reduce(n,k,table):
    for s in related[k]:
        table[s] = table[s].replace(n,"")

#Wipes the list of empty, or unsolved, spaces and compliles a new one based off of the current table
def getEmpty(table):
    empty.clear()
    for k in full:
        if (table[k] == "") or len(table[k]) > 1:
            empty.append(k)
    poss(table)

#Clears the table
def wipe():
    for k in full:
        grid[k] = ""

#Wipes the list of chosen, or solved, spaces and complies a new one based off of the current table
def getChosen(table):
    chosen.clear()
    for k in table:
        if len(table[k]) == 1:
            chosen.append(k)

#Solves the imput table to determine whether or not it has exactly one solution
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
        logger.debug("{0:9} {1:9} {2:9} | {3:9} {4:9} {5:9} | {6:9} {7:9} {8:9}".format(*numbers))
        line += 1
        if (line % 3) == 0:
            logger.debug("")
    
    end1 = time.time()

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
          
    #Debug code to track the time the program takes to run
    end2 = time.time()
    return unsolved

#Prints out the latest runtime stats to the debug console
def stats():
    
    first = str(end1 - start1)
    last = str(end2 - start2)
    elapsed = float(first) + float(last)
    minutes = str(elapsed // 60)
    rseconds = str(elapsed % 60)
    logger.info(elapsed)
    logger.info('Took ' + minutes + ' minutes and ' + rseconds + ' seconds')
    logger.info('Creating: ' + first)
    logger.info('Unsolving: ' + last)