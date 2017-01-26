# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:30:26 2017

@author: graha
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)