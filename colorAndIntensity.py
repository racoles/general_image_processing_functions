'''
@title colorAndIntensity
@author: Rebecca Coles
Updated on Sep 14, 2017
Created on Sep 14, 2017

colorAndIntensity
This module holds a series of functions that I use to convert
analyze the color or intensity of values in an image.

Modules:
colorFinder
    This function searches an array for a given RGBA color value above a given
    threshold, and returns a list of all of the pixels that meet that criteria.
'''

# Import #######################################################################################
################################################################################################

class colorAndIntensity(object):
    
    def __init__(self):
        '''
        Constructor
        '''
            
    def colorFinder(self, colorArray, **kwargs):
        '''
        Search an array for a given RGBA color value above a given
        threshold, and returns a list of all of the pixels that meet that criteria.
        '''
        #Initialize empty list that will be filled with pixels that fit the 
            #users RGBA criteria.
        colorCutPixels = []
        #Search the data based on the colors that the user has specified
        if kwargs is not None:
            #Red
            if 'r' in kwargs:
                [colorCutPixels.append(colorArray[ii,:]) for ii in colorArray if colorArray[ii,2] >= kwargs.get('r')]
            #Green
            if 'g' in kwargs:
                [colorCutPixels.append(colorArray[jj,:]) for jj in colorArray if colorArray[jj,3] >= kwargs.get('g')]
            #Blue
            if 'b' in kwargs:
                [colorCutPixels.append(colorArray[kk,:]) for kk in colorArray if colorArray[kk,4] >= kwargs.get('b')]
            #Alpha
            if 'a' in kwargs and colorArray.shape[1] >= 5: #to account for a RGB image as opposed to a RGBA
                [colorCutPixels.append(colorArray[ll,:]) for ll in colorArray if colorArray[ll,5] >= kwargs.get('a')]
        #return list of accepted pixels
        return colorCutPixels