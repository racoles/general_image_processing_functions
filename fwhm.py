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
'''

# Import #######################################################################################
from numpy import where, mean, var, sqrt, linspace
from matplotlib.mlab import normpdf
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
        #create histogram of image intensities and fit histogram
        mean_value = mean(array3D)
        sigma = sqrt(var(array3D)) #sqrt(variance)
        xx = linspace(min(array3D), max(array3D), 100)
        yy = normpdf(xx, mean_value, sigma)
        
        #find when function crosses line half_max (when sign of diff flips)
        #take the 'derivative' of signum(half_max - Y[])
        d = yy - (max(yy) / 2) #sign(half_max - array(Y[0:-1])) - sign(half_max - array(Y[1:]))
        indexes = where(d > 0)[0] 
        return abs(xx[indexes[-1]] - xx[indexes[0]])