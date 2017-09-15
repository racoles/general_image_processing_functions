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
from numpy import asarray
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
        #save pixel (row, column, values) to file
        data = []
        [[data.append(str(ii+1) + ',' + str(jj+1) + ',' + ','.join(str(pixelValues[ii,jj])) + '\n') for jj in range(pixelValues.shape[1])] for ii in range(pixelValues.shape[0])]
        with open(filePath.getFileNameFromPath(imageFileLocation) + '.csv', "w") as output:
            output.write(str(data))
        
        
        