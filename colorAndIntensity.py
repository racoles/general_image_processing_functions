'''
@title colorAndIntensity
@author: Rebecca Coles
Updated on Sep 18, 2017
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
from numpy import vstack, zeros
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
                [colorCutPixels.extend([ii, jj, colorArray[ii,jj,:]]) for ii in range(colorArray.shape[0]) for jj in range(colorArray.shape[1]) if colorArray[ii,jj,0] >= kwargs.get('r')]
            #Green
            if 'g' in kwargs:
                [colorCutPixels.extend([kk, ll, colorArray[kk,ll,:]]) for kk in range(colorArray.shape[0]) for ll in range(colorArray.shape[1]) if colorArray[kk,ll,1] >= kwargs.get('g')]
            #Blue
            if 'b' in kwargs:
                [colorCutPixels.extend([mm, nn, colorArray[mm,nn,:]]) for mm in range(colorArray.shape[0]) for nn in range(colorArray.shape[1]) if colorArray[mm,nn,2] >= kwargs.get('b')]
        #return list of accepted pixels
        print(colorCutPixels) 
        return colorCutPixels