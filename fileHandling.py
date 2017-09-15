'''
@title fileHandling
@author: Rebecca Coles
Updated on Sep 14, 2017
Created on Sep 14, 2017

fileHandling
This module holds a series of functions that I use to handle
various file creation/manipulation/etc.

Modules:
openFile
    This function creates an open file dialogue box and returns the name of the user selected file.
getFileNameFromPath
    Extract filenames from paths, no matter what the operating system or path format is from.
'''

# Import #######################################################################################
from tkinter import filedialog
from ntpath import split, basename
################################################################################################

class fileHandling(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def openFile(self):
        '''
        Create open file dialogue box
        '''
        return filedialog.askopenfilename()
    
    def getFileNameFromPath(self, path):
        '''
        Extract filenames from paths, no matter where the operating system or path format is from
        '''
        head, tail = split(path)
        return tail or basename(head)
        