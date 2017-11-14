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
from numpy import where
from matplotlib.pyplot import ioff, figure
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
        # Turn interactive plotting off by default
        ioff()
        
        #create histogram of image intensities
        fig1 = figure()
        ax1 = fig1.add_subplot(111)
        ax1.hist(array3D, bins='rice', facecolor='g')
        
        #fit histogram
        
        #find when function crosses line half_max (when sign of diff flips)
        #take the 'derivative' of signum(half_max - Y[])
        d = array3D - (max(array3D) / 2) #sign(half_max - array(Y[0:-1])) - sign(half_max - array(Y[1:]))
        indexes = where(d > 0)[0] 
        return abs(X[indexes[-1]] - X[indexes[0]])