# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:33:57 2016

@author: Graham Cooke
"""

#PS Future self remember to comment (;

import random
import sys
import copy

def row(k):
    return (mult(k[1],indexes) - k)

def col(k):
    return (mult(k[0],indexes) - k)

def cel(k):
    return (checkCell(k) - k)

def mult(list1,list2):
    out = []
    for a in list1:
        for b in list2:
            out.append(a+b)
    return out
    
def checkSpace(n,k):
        if n in (grid[i] for i in related[k]):
            return False
        else:
            return True
    
def checkCell(k):
    cellPoints = []
    xC = ((k[0]-1) // 3)
    yC = ((k[1]-1) // 3)

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

    cellPoints.append(mult(xC,yC))

    return (cellPoints)

def poss():
    for k in open:
        for n in numbers:
            if checkSpace(n,k):
                grid[k] = grid[k] + n

def search():
    for k in open:
        if len(grid[k]) is 1:
            reduce(grid[k],k)
            open.pop(open.index(k))

def reduce(n,k):
    for s in related[k]:
        grid[s] = grid[s].replace(n,"")

# def generate(x,y):
#
#     l = [1,2,3,4,5,6,7,8,9]
#     c = findCell(x,y)
#     for n in range(9):
#         if(n+1 in column[x] or n+1 in row[y] or n+1 in cell[c]):
#             i = l.index(n+1)
#             l.pop(i)
#     if(l != []):
#         grid[y][x] = random.choice(l)
#     else:
#         print("error on {},{}; no possible number".format(x,y))
#         for i in range(9):
#             print(row[i])
#         sys.exit()
#     return
    
# def possible(x,y):
#     l = [1,2,3,4,5,6,7,8,9]
#     c = findCell(x,y)
#     for n in range(9):
#         if(n+1 in column[x] or n+1 in row[y] or n+1 in cell[c]):
#             i = l.index(n+1)
#             l.pop(i)
#     return len(l)

# def getUnsolved():
#     unsolved = []
#     for x in range(9):
#         for y in range(9):
#             if solvedGrid[y][x] == 0:
#                 unsolved.append([x,y])
#     return unsolved

# def solve():
#     global solvedGrid
#     solved = []
#     solvedGrid = copy.deepcopy(grid)
#     unsolved = getUnsolved()
#     updateSolved()
#     cycles = 0
#     while(unsolved):
#         cycles += 1
#         x = unsolved[0][0]
#         y = unsolved[0][1]
#         c = findCell(x,y)
#         n = solvedGrid[y][x]
#         n += 1
#         while((n in sColumn[x] or n in sRow[y] or n in sCell[c]) and n <= 9):
#             n += 1
#         if(n > 9):
#             try:
#                 wipe = solved[-1]
#             except:
#                 return False
#             unsolved.insert(0, wipe)
#             del solved[-1]
#             solvedGrid[y][x] = 0
#         else:
#             solvedGrid[y][x] = n
#             del unsolved[0]
#             solved.append([x,y])
#         updateSolved()
#     print(cycles)
#     return True
                

indexes = "012345678"
indexC1 = "012"
indexC2 = "345"
indexC3 = "678"
numbers = "123456789"
all = mult(indexes,indexes)

#Define the sudoku grid
grid = {k : 0 for k in mult(indexes,indexes)}
related = {k : (row(k) + col(k) + cel(k)) for k in mult(indexes,indexes)}

open = []



# while(len(generated) < givens):
#     loc = random.choice(spaces)
#     x = loc[0]
#     y = loc[1]
#     print(x,y)
#     if(possible(x,y) > 0):
#         generate(x,y)
#         if(solve()):
#             generated.append(loc)
#             i = spaces.index(loc)
#             spaces.pop(i)
#             print(len(generated))
#         else:
#             grid[y][x] = 0
#             print("tick")
