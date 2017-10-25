'''
@title plot
@author: Rebecca Coles
Updated on Oct 25, 2017
Created on Oct 24, 2017

cropAndResize
This module holds a series of functions that I use to plot images.

Modules:
plotAllHist_distances
    This function accepts a 4D numpy array and plots histograms of the images that are saved
    to files. This functions assumes that the distances are the filenames (int)
'''

# Import #######################################################################################
from numpy import std, zeros
from matplotlib.pyplot import ioff, hist, xlabel, ylabel, title, grid, savefig, plot, figure
import os
from os.path import basename
from operator import itemgetter
################################################################################################

class plots(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def plotAllHist_distances(self, imageArray4D, filelist):
        '''
        Accepts a 4D numpy array and plots histograms of the images.
        note: assumes filenames are distances (int)
        '''
        # Turn interactive plotting off
        ioff()
        #std array
        stdList = zeros(imageArray4D.shape[0])
        #start plotting
        for image in range(imageArray4D.shape[0]):
            flattenedArray = imageArray4D[image].flatten()
            stdList[image] = std(flattenedArray)
            n, bins, patches = hist(flattenedArray, facecolor='g')
            xlabel('Counts (per pixel)')
            ylabel('Frequency')
            title(filelist[image] + '\n' + 'std = ' + str(stdList[image]))
            grid(True)
            savefig(filelist[image] + ".png")
            
        #plot stds
        ##create x values
        xx = []
        ##remove extension from filenames
        [xx.append(os.path.splitext(filelist[image])[0]) for image in range(len(filelist))]
        ##get basename of files
        for ii in range(len(xx)): 
            xx[ii] = int(basename(xx[ii]))
        ##zip xx and yy values into array of tulups
        xy = []
        [xy.append(jj) for jj in zip(xx, stdList)]
        ##sort list by distance
        sortedXY = sorted(xy, key=itemgetter(0))
        ##plot stds
        fig2 = figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot([kk[0] for kk in sortedXY],[mm[1] for mm in sortedXY], 'ro')
        xlabel('Distances (mm)')
        ylabel('Standard Deviation')
        title('Standard Deviation versus Distance')
        grid(True)
        fig2.savefig('std_vs_dis.png')
        
            