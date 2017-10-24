'''
@title cropAndResize
@author: Rebecca Coles
Updated on Oct 13, 2017
Created on Oct 13, 2017

cropAndResize
This module holds a series of functions that I use to crop and
otherwise resize images.

Modules:
cropImages
    This function accepts an array and crops the images for a given size and location.
'''

# Import #######################################################################################
from numpy import append, array
################################################################################################

class cropAndResize(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def cropImages(self, imageArray, xStart, yStart, widthCrop, heightCrop):
        #If 3D (one image)
        if len(imageArray.shape) == 3:
            croppedImages = imageArray.crop((xStart, yStart, widthCrop, heightCrop))
        #If 4D (array of 3D images)
        elif len(imageArray.shape) == 4:
            croppedImages = array()
            for ii in range(imageArray.shape[0]):
                croppedImages.append(imageArray[ii].crop((xStart, yStart, widthCrop, heightCrop)))
        else:
            print('Image(s) can not be cropped, the array dimensions are not acceptable.')
        return croppedImages