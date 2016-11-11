# -*- coding: utf-8 -*-

import sys

"""
Created on Wed Oct 12 15:13:24 2016

@author: Graham Cooke
"""
lineNumber = 0;

try:
    book = open("Don_Quixote.txt", "r").read()
    l = open("Don_Quixote.txt", "r")
except:
    print("Couldn't read the file, exiting the program")
    sys.exit()
    
length = len(book)
wordCount = 0  

print("The book is {:,} characters long".format(length))
for line in l:
    try:
        lineNumber = lineNumber + 1
    except:
        print("Couldn't read after line {:,}.").format(lineNumber)
        
print("The book is {:,} lines long".format(lineNumber))

w = open("Don_Quixote.txt", "r")
for line in w:
    a = line.strip().split()
    wordCount += len(a)
    
    
print("This book is {:,} words long".format(wordCount))
    
