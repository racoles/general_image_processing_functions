'''
@title plot
@author: Rebecca Coles
Updated on Oct 24, 2017
Created on Oct 24, 2017

cropAndResize
This module holds a series of functions that I use to plot images.

Modules:
plotAllHist
    This function accepts a 4D numpy array and plots histograms of the images that are saved
    to files.
'''

# Import #######################################################################################
from numpy import std, ndarray
from matplotlib.pyplot import ioff, hist, xlabel, ylabel, title, grid, savefig
################################################################################################

class plots(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def plotAllHist(self, imageArray4D, filelist):
        '''
        Accepts a 4D numpy array and plots histograms of the images.
        '''
        # Turn interactive plotting off
        ioff()
        #start plotting
        for image in range(imageArray4D.shape[0]):
            flattenedArray = imageArray4D[image].flatten()
            imageStd = std(flattenedArray)
            n, bins, patches = hist(flattenedArray, facecolor='g')
            xlabel('Counts (per pixel)')
            ylabel('Frequency')
            title(filelist[image] + '\n' + 'std = ' + str(imageStd))
            grid(True)
            savefig(filelist[image] + ".png")
            