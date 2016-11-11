# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:36:53 2016

@author: Graham Cooke
"""

website = "ex.ample.com/home/main"

#If there is a / in website
if("/" in website):
    #print from the last . to the first /
    print(website[website.rfind("."):website.find("/")])
else:
    print(website[website.rfind("."):])