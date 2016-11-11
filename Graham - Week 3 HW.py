# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:03:54 2016

@author: Graham Cooke
"""

#Website to be anaylyzed
website = "example.site.domain/main/home"
#stores the location of the most recently found slash
#-1 is a placholder to indicate that no slash has been found
slash = -1

#main loop
#sets the range of index to length of website(minus 1 due to starting at 0)
#to the end(-1), and to interate backwards through the range
for index in range(len(website)-1, -1, -1):
    
    #print(index)    
    
    #look for the last slash from the left and stores the location
    if website[index] == "/":
        slash = index
        
    #looks for the last period from the left
    if website[index] == ".":
        
        #if there was a slash, print from the last period to the next slash
        if slash != -1:
            print(website[index:slash])
            break
            
        #if therewas no slash, print from the period to the end
        else:
            print(website[index:])
            break
            
print("End")