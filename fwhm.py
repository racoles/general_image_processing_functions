'''
@title fwhm
@author: Rebecca Coles
Updated on Nov 15, 2017
Created on Oct 12, 2017

fwhm
This module holds a series of functions that I use to find the
full-well-half-maximum of a given curve.

Modules:
fwhm3D
    This function accepts a 3D array and finds the FWHM of the image.
    FWHM is the gaussian PSF full width half maximum (fit result) in pixels
'''

# Import #######################################################################################
from numpy import amax, median, mean, sqrt, sum
################################################################################################

class fwhm(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def fwhm3D(self, array3D):
        '''
        Accepts a 3D array and finds the FWHM (in pixels) of the image.
        FWHM is the gaussian PSF full width half maximum (fit result) in pixels
        '''
        #Starting values
        maxi = amax(array3D)
        floor = median(array3D.flatten())
        height = maxi - floor
        if height == 0.0: # if object is saturated it could be that median value is 32767 or 65535 --> height=0
            floor = mean(array3D.flatten())
            height = maxi - floor
        fwhm = sqrt(sum((array3D>floor+height/2.).flatten()))
        return fwhm