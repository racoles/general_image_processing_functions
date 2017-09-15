'''
@title imageToArray
@author: Rebecca Coles
Updated on Sep 15, 2017
Created on Sep 13, 2017

imageToArray
This module holds a series of functions that I use to convert
images to arrays.

Modules:
nonFitsImageToArray
    This function converts a non-FITs type image to an array.
'''

# Import #######################################################################################
from numpy import asarray,savetxt
from PIL import Image
from fileHandling import fileHandling
################################################################################################

class imageToArray(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def nonfitsImageToArray(self):
        '''
        Convert a non-FITs type image to an array
        '''
        #open image file
        filePath = fileHandling()
        try:
            imageFileLocation = filePath.openFile()
        except IOError:
            print('The file could not be opened, or no file was selected.')
        try:
            im = Image.open(imageFileLocation)
        except IOError:
            print('The file could not be opened.')
        #read pixel values to a numpy array 
            #(array with each pixel value as a set of 3 or 4 values: R,G,B,A)
        pixelValues = asarray(im)
        #save row and column values to file
        saveFile = open(filePath.getFileNameFromPath(imageFileLocation) + '.csv', 'w')
        [[saveFile.write("{0},{1},\n".format(ii+1, jj+1)) for jj in range(pixelValues.shape[1])] for ii in range(pixelValues.shape[0])]
        #append pixel values to file
        #savetxt(saveFile, pixelValues, delimiter=',')
        
        
        
        