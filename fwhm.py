'''
@title fwhm
@author: Rebecca Coles
Updated on Nov 09, 2017
Created on Oct 12, 2017

fwhm
This module holds a series of functions that I use to find the
full-well-half-maximum of a given curve.

Modules:
fwhm3D
    This function accepts a 3D array and finds the FWHM of the image.
focusCurve
    Accepts a 4D array and finds the FWHM of the images, and plots a focus curve.
'''

# Import #######################################################################################
################################################################################################

class fwhm(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def fwhm3D(self, array3D):
        '''
        Accepts a 3D array and finds the FWHM of the image.
        '''
        max_y = max(array3D)  # Find the maximum y value
        xs = [x for x in range(20) if array3D[x] > max_y/2.0] #######################################
        return min(xs), max(xs)
    
    def fwhmPlotAll(self, imageArray4D, filelist):
        '''
        Accepts a 4D array and finds the FWHM of the images, and plots a focus curve.
        '''
        pass