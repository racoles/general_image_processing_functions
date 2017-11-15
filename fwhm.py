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
#from numpy import where, mean, var, sqrt, linspace, min, max
#from matplotlib.mlab import normpdf
#from matplotlib.pyplot import ioff, xlabel, ylabel, title, grid, savefig, figure, text
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
        '''
        
        #find starting values
        maxi = amax(array3D)
        floor = median(array3D.flatten())
        height = maxi - floor
        if height == 0.0:                #if star is saturated it could be that median value is 32767 or 65535 --> height=0
            floor = mean(array3D.flatten())
            height = maxi - floor
        fwhm = sqrt(sum((array3D>floor+height/2.).flatten()))
        return fwhm
        
        #normpdf
        #mean_value = mean(array3D)
        #sigma = sqrt(var(array3D)) #sqrt(variance)
        #xx = linspace(min(array3D), max(array3D), 1000)
        #yy = normpdf(xx, mean_value, sigma)
        
        #print(array3D.shape)
        #fig = figure()
        #ax = fig.add_subplot(111)
        #ax.plot(xx, yy, 'ro')
        #xlabel(' ')
        #ylabel(' ')
        #title('pdf')
        #grid(True)
        #save figure
        #fig.savefig('fwhm_vs_position1.png')
        
        #find when function crosses line half_max (when sign of diff flips)
        #take the 'derivative' of signum(half_max - Y[])
        #dd = yy - (max(yy) / 2) #sign(half_max - array(Y[0:-1])) - sign(half_max - array(Y[1:]))
        #indexes = where(dd > 0)[0] 
        #return abs(xx[indexes[-1]] - xx[indexes[0]])
        