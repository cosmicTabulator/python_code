# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:33:57 2016

@author: Graham Cooke
"""

#PS Future self remember to comment (;

import random
import sys
import copy

def update():
    n = 0
    for a in range(3):
        for b in range(3):      
            
            #for y in range(3):
            cell[n] = grid[(a*3)][(b*3):((b*3)+3)] + grid[1+(a*3)][(b*3):((b*3)+3)] + grid[2+(a*3)][(b*3):((b*3)+3)]
            n += 1
          
    for y in range(9):
        row[y] = grid[y]
        
    for x in range(9):
        for y in range(9):
            column[x][y] = grid[y][x]
          
    return

def updateSolved():
    n = 0
    for a in range(3):
        for b in range(3):      
            
            #for y in range(3):
            sCell[n] = solvedGrid[(a*3)][(b*3):((b*3)+3)] + solvedGrid[1+(a*3)][(b*3):((b*3)+3)] + solvedGrid[2+(a*3)][(b*3):((b*3)+3)]
            n += 1
          
    for y in range(9):
        sRow[y] = solvedGrid[y]
        
    for x in range(9):
        for y in range(9):
            sColumn[x][y] = solvedGrid[y][x]
          
    return

def findCell(x,y):
    xC = x // 3
    yC = y // 3
    if(yC != 0):
        nC = xC + yC*3
    else:
        nC = xC
    return nC

def generate(x,y):
    
    l = [1,2,3,4,5,6,7,8,9]
    c = findCell(x,y)
    for n in range(9):
        if(n+1 in column[x] or n+1 in row[y] or n+1 in cell[c]):
            i = l.index(n+1)
            l.pop(i)
    if(l != []):
        grid[y][x] = random.choice(l)
    else:
        print("error on {},{}; no possible number".format(x,y))
        for i in range(9):
            print(row[i])
        sys.exit()
    update()
    return
    
def possible(x,y):
    l = [1,2,3,4,5,6,7,8,9]
    c = findCell(x,y)
    for n in range(9):
        if(n+1 in column[x] or n+1 in row[y] or n+1 in cell[c]):
            i = l.index(n+1)
            l.pop(i)
    return len(l)

def getUnsolved():
    unsolved = []
    for x in range(9):
        for y in range(9):
            if solvedGrid[y][x] == 0:
                unsolved.append([x,y])
    return unsolved

def solve():
    global solvedGrid
    global sRow
    global sColumn
    global sCell
    sColumn = copy.deepcopy(column)
    sRow = copy.deepcopy(row)
    sCell = copy.deepcopy(cell)
    solved = []
    solvedGrid = copy.deepcopy(grid)
    unsolved = getUnsolved()
    updateSolved()
    cycles = 0
    while(unsolved):
        cycles += 1
        x = unsolved[0][0]
        y = unsolved[0][1]
        c = findCell(x,y)
        n = solvedGrid[y][x]
        n += 1
        while((n in sColumn[x] or n in sRow[y] or n in sCell[c]) and n <= 9):
            n += 1
        if(n > 9):
            try:
                wipe = solved[-1]
            except:
                return False
            unsolved.insert(0, wipe)
            del solved[-1]
            solvedGrid[y][x] = 0
        else:
            solvedGrid[y][x] = n
            del unsolved[0]
            solved.append([x,y])
        updateSolved()
    print(cycles)
    return True
                

#Define the sudoku grid
grid = [[0 for x in range(9)] for y in range(9)]
cell = [[0 for x in range(9)] for y in range(9)]
row = [[0 for x in range(9)] for y in range(9)]
column = [[0 for x in range(9)] for y in range(9)]
solvedGrid = [[0 for x in range(9)] for y in range(9)]
sRow= [[0 for x in range(9)] for y in range(9)]
sColumn = [[0 for x in range(9)] for y in range(9)]
sCell = [[0 for x in range(9)] for y in range(9)]

givens = random.randint(20,40)

update()

generated = []
spaces = []

for x in range(9):
    for y in range(9):
        spaces.append((x,y))
        
while(len(generated) < givens):
    loc = random.choice(spaces)
    x = loc[0]
    y = loc[1]
    print(x,y)
    if(possible(x,y) > 0):
        generate(x,y)
        if(solve()):
            generated.append(loc)
            i = spaces.index(loc)
            spaces.pop(i)
            print(len(generated))
        else:
            grid[y][x] = 0
            print("tick")

print("Grid")
print(grid)
print("Row")
print(row)
print("Column")
print(column)
print("Cell")
print(cell)
for i in range(9):
    print(row[i])