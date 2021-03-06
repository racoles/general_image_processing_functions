'''
@title imageToArray
@author: Rebecca Coles
Updated on Sep 18, 2017
Created on Sep 13, 2017

imageToArray
This module holds a series of functions that I use to convert
images to arrays.

Modules:
nonFitsImageToArray
    This function converts a non-FITs type image to an array.
openAllFITSImagesInDirectory
    This function convertsFITs type images to a 4D array.
'''

# Import #######################################################################################
from numpy import asarray, array
from PIL import Image
from fileHandling import fileHandling
from glob import glob
from astropy.io import fits
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
        return pixelValues
    
    def openAllFITSImagesInDirectory(self):
        '''
        Open multiple images and save them to a numpy array
        '''
        #open image file
        dirPath = fileHandling()
        try:
            dirLocation = dirPath.openDir()
        except IOError:
            print('The directory could not be opened, or no directory was selected.')
        filelist = glob(dirLocation + '/*.*')
        fitsImages = [fits.getdata(image) for image in filelist]
        #convert to 4D numpy array
        return array(fitsImages), filelist
        
        
        