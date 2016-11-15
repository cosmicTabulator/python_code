# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:33:57 2016

@author: Graham Cooke
"""

#PS Future self: remember to comment (;

import random
import logging
logger = logging.getLogger()

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
    
def checkSpace(n,k):
    neighbors = []
    for i in related[k]:
        if i not in empty:
            neighbors.append(grid[i])
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

def poss():
    for k in open:
        for n in numbers:
            if checkSpace(n,k):
                grid[k] = grid[k] + n

def search():
    for k in empty:
        if len(grid[k]) is 1:
            reduce(grid[k],k)
            empty.pop(empty.index(k))
        for n in grid[k]:
            isolated = True
            for r in row(k):
                if n in grid[r]:
                    isolated = False
            if isolated:
                grid[k] = n
                reduce(n,k)
                break
            isolated = True
            for c in col(k):
                if n in grid[c]:
                    isolated = False
            if isolated:
                grid[k] = n
                reduce(n,k)
                break
            isolated = True
            for c in cel(k):
                if n in grid[c]:
                    isolated = False
            if isolated:
                grid[k] = n
                empty.pop(empty.index(k))
                reduce(n,k)
                break

def reduce(n,k):
    for s in related[k]:
        grid[s] = grid[s].replace(n,"")
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
indexes = "012345678"
indexC1 = "012"
indexC2 = "345"
indexC3 = "678"
numbers = "123456789"
full = mult(indexes,indexes)

#Define the sudoku grid
grid = {k : 0 for k in mult(indexes,indexes)}
grid.update({"r"+k : fRow(k) for k in indexes})
grid.update({"c"+k : fCol(k) for k in indexes})
grid.update({"s"+k : fCel(k) for k in indexes})
related = {k : (row(k) + col(k) + cel(k)) for k in mult(indexes,indexes)}
logging.debug(related)
logging.debug(grid)
empty = []
for n in indexes:
    numbers = ()
    for i in grid["r"+n]:
        numbers = numbers + (i,)
    logger.debug(numbers)
    logger.info("{0} {1} {2} | {3} {4} {5} | {6} {7} {8}".format(numbers))
