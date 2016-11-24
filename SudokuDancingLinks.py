# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:33:57 2016

@author: Graham Cooke
"""

#PS Future self: remember to comment (;

import random
import logging
import copy
import sys
import time
start1 = time.time()
logger = logging.getLogger()

logger.setLevel(logging.ERROR)

def row(k):
    m = mult(indexes,k[1])
    out = []
    for e in m:
        if e != k:
            out.append(e)
    return out

def col(k):
    m = mult(k[0],indexes)
    out = []
    for e in m:
        if e != k:
            out.append(e)
    return out

def cel(k):
    m = checkCell(k)
    out = []
    for e in m:
        if e != k:
            out.append(e)
    return out
    
def fRow(k):
    return mult(indexes,k)

def fCol(k):
    return mult(k,indexes)

def fCel(k):
    y = str((int(k) // 3)*3)
    x = str((int(k) % 3)*3)
    k = x+y
    return (checkCell(k))

def mult(list1,list2):
    out = []
    for a in list1:
        for b in list2:
            out.append(a+b)
    return out
    
def checkSpace(n,k,table):
    neighbors = []
    for i in related[k]:
        if i not in empty:
            neighbors.append(table[i])
    if n in neighbors:
        return False
    else:
        return True

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

def poss(table):
    for k in empty:
        for n in numbers:
            if checkSpace(n,k,table):
                table[k] = table[k] + n

def search(table):
    reduced = False
    #logger.debug(empty)
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
    
def wipe(table):
    for k in full:
        table[k] = ""

def getChosen(table):
    chosen.clear()
    for k in table:
        if len(table[k]) == 1:
            chosen.append(k)

def choose(table,k):
    i = 0
    n = 0
    l = table[k]
    table[k] = l[0]
    while(solve(table) == False):
        i += 1
        try:
            table[k] = l[i]
        except:
            logger.debug("No Solution")
            return False
    return True

def solve(table):
    while(search(table)):
        logger.debug("Searching...")
    for k in grid:
        if grid[k] == "":
            logger.debug("No Solution")
            return False
        if len(grid[k]) > 1:
            if choose(table, k) == False:
                return False
    return True

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

indexes = "012345678"
indexC1 = "012"
indexC2 = "345"
indexC3 = "678"
numbers = "123456789"
full = mult(indexes,indexes)
empty = []
chosen = []

#Define the sudoku grid
grid = {k : "" for k in mult(indexes,indexes)}
# grid.update({"r"+k : fRow(k) for k in indexes})
# grid.update({"c"+k : fCol(k) for k in indexes})
# grid.update({"s"+k : fCel(k) for k in indexes})
related = {k : (row(k) + col(k) + cel(k)) for k in mult(indexes,indexes)}
n = 0
getEmpty(grid)
numberEmpty = 0
times = 0
l = 0
while len(empty) > 0:
    k = random.choice(empty)
    logger.debug(k)
    n = random.choice(grid[k])
    backup = copy.deepcopy(grid)
    logger.debug(n)
    grid[k] = n
    t = 0
    loading()
    while(search(grid)):
        t += 1
        logger.debug(str(t) + " Ticks")
    for e in grid:
        if grid[e] == '':
            if times > 3:
                logger.debug("Restarted")
                wipe(grid)
                getEmpty(grid)
                break
            if len(empty) == numberEmpty:
                times += 1
                logger.debug("Repeat")
            numberEmpty = len(empty)
            logger.debug("Backtracked")
            grid = copy.deepcopy(backup)
            getEmpty(grid)
            poss(grid)
            logger.debug(str(len(empty)) + " are Empty")
            break
#==============================================================================
#             logger.debug("Restarted")
#             wipe(grid)
#             getEmpty(grid)
#             break
#==============================================================================
#==============================================================================
#     if(solve(grid) == False):
#              logger.debug("Backtracked")
#              grid = copy.deepcopy(backup)
#              getEmpty(grid)
#              poss(grid)
#              break
#==============================================================================
        
logger.debug("Grid")
logger.debug(grid)
line = 0
for x in indexes:
    numbers = ()
    for y in indexes:
        numbers = numbers + (grid[x+y],)
    logger.info("{0:9} {1:9} {2:9} | {3:9} {4:9} {5:9} | {6:9} {7:9} {8:9}".format(*numbers))
    line += 1
    if (line % 3) == 0:
        logger.info("")

unsolved = copy.deepcopy(grid)
template = copy.deepcopy(grid)
logger.debug(isSolvable(unsolved))
if isSolvable(grid) == False:
    sys.exit()
    
remove = 0

end1 = time.time()

while(remove < 30):
    remove = int(input("Number of given numbers:"))
    
start2 = time.time()    
    
remove = 81 - remove
r = 0
while r < remove:
    getChosen(unsolved)
    k = random.choice(chosen)
    n = template[k]
    template[k] = ""
    unsolved = copy.deepcopy(template)
    loading()
    if(isSolvable(unsolved)):
        logger.debug(True)
        chosen.pop(chosen.index(k))
        r += 1
        logger.debug("R = " + str(r))
    else:
        logger.debug(False)
        template[k] = n

for x in indexes:
    numbers = ()
    for y in indexes:
        numbers = numbers + (unsolved[x+y],)
    print("{0:1} {1:1} {2:1} | {3:1} {4:1} {5:1} | {6:1} {7:1} {8:1}".format(*numbers))
    line += 1
    if ((line % 3) == 0):
        print("------+-------+------")
        
end2 = time.time()
first = str(end1 - start1)
last = str(end2 - start2)
elapsed = float(first) + float(last)
minutes = str(elapsed // 60)
rseconds = str(elapsed % 60)
logger.debug(elapsed)
logger.debug('Took ' + minutes + ' minutes and ' + rseconds + ' seconds')
logger.debug('First: ' + first)
logger.debug('Last: ' + last)