'''
@title imageToArray
@author: Rebecca Coles
Updated on Sep 14, 2017
Created on Sep 13, 2017

imageToArray
This module holds a series of functions that I use to convert
images to arrays.

Modules:
nonFitsImageToArray
    This function converts a non-FITs type image to an array.
'''

# Import #######################################################################################
from numpy import asarray
from PIL import Image
from fileHandling import fileHandling
################################################################################################

class imageToArray(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def nonFitsImageToArray(self):
        '''
        Convert a non-FITs type image to an array
        '''
        #open image file
        try:
            filePath = fileHandling.openFile()
        except IOError:
            print('The file could not be opened, or no file was selected.')
        try:
            im = Image.open(filePath, ' r')
        except IOError:
            print('The file could not be opened.')
        #read pixel values to a numpy array 
        #(array with each pixel value as a set of 6 values: row, column, R,G,B,A)
        pixelValues = asarray(im)
        #save pixel values to file
        print(pixelValues)
        #theFile = open(fileHandling.getFileNameFromPath(filePath) + '.txt', 'w')
        #for pixel in pixelValues:
        #    theFile.write("%s\n" % pixel)
        
        