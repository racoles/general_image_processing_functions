'''
@title imageToArray
@author: Rebecca Coles
Updated on Sep 13, 2017
Created on Sep 13, 2017

imageToArray
This module holds a series of functions that I use to convert
images to arrays.

Modules:
openFile
    This function creates an open file dialogue box and returns the name of the user selected file.
getFileNameFromPath
    Extract filenames from paths, no matter what the operating system or path format is from.
nonFitsImageToArray
    This function converts a non-FITs type image to an array.
'''

# Import #######################################################################################
from tkinter import filedialog
from ntpath import split, basename
from PIL import Image
################################################################################################

class imageToArray(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def _openFile(self):
        '''
        Create open file dialogue box
        '''
        return filedialog.askopenfilename()
    
    def _getFileNameFromPath(self, path):
        '''
        Extract filenames from paths, no matter what the operating system or path format is from
        '''
        head, tail = split(path)
        return tail or basename(head)
        
    def nonFitsImageToArray(self):
        '''
        Convert a non-FITs type image to an array
        '''
        #open image file
        try:
            filePath = self._openFile()
        except IOError:
            print('The file could not be opened, or no file was selected.')
        try:
            im = Image.open(filePath, ' r')
        except IOError:
            print('The file could not be opened')
        #read pixel values to list 
        #(list with each pixel value as a set of 4 values(R,G,B,A))
        pixelValues = list(im.getdata())
        #save pixel values to file
        theFile = open(self.getFileNameFromPath(filePath) + '.txt', 'w')
        for pixel in pixelValues:
            theFile.write("%s\n" % pixel)
        