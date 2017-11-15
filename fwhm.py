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
    FWHM is the gaussian PSF full width half maximum (fit result) in pixels
'''

# Import #######################################################################################
from numpy import amax, median, mean, sqrt, sum, shape, log, square, exp, abs, ravel, indices
from scipy.optimize import leastsq
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
        #mean_x = (shape(array3D)[0]-1)/2
        #mean_y = (shape(array3D)[1]-1)/2
        #sig = fwhm / (2.*sqrt(2.*log(2.)))
        #width = 0.5/square(sig)
        #p0 = floor, height, mean_x, mean_y, width
        
        #Fitting Gaussian
        #def gauss(floor, height, mean_x, mean_y, width):        
        #    return lambda x,y: floor + height*exp(-abs(width)*((x-mean_x)**2+(y-mean_y)**2))

        #def err(p,data):
        #    return ravel(gauss(*p)(*indices(data.shape))-data)
    
        #p = leastsq(err, p0, args=(array3D), maxfev=1000)
        #p = p[0]
        
        #Format results
        #print(p)
        #floor = p[0]
        #height = p[1]
        #sig = sqrt(0.5/abs(p[4]))
        #fwhm = sig * (2.*sqrt(2.*log(2.)))
        #print(sig)
        #print(fwhm)
        return fwhm