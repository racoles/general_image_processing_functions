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
stdPlotAll
    Accepts a 4D numpy array and plots standard deviations of the images.
    Note: assumes filenames are distances (int)
fwhmPlotAll
    Accepts a 4D array and finds the FWHM of the images, and plots a focus curve.
fileNameToInt
    Create x values by remove extension from filenames and converting them to ints
zipAndSort
    Zip xx and yy values into array of tulups
    Sort list by distance (x) so xx (distances) are in the proper order in the plot
xyPolyFit
    Calculate polynomial fit (order given)
    Calculate new x's and y's for plotting
'''

# Import #######################################################################################
from numpy import std, zeros, poly1d, polyfit, linspace, polyder
from matplotlib.pyplot import ioff, xlabel, ylabel, title, grid, savefig, figure, text
import os
from os.path import basename
from operator import itemgetter
from fwhm import fwhm
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
        #start plotting
        for image in range(imageArray4D.shape[0]):
            flattenedArray = imageArray4D[image].flatten()
            fig1 = figure()
            ax1 = fig1.add_subplot(111)
            ax1.hist(flattenedArray, bins='rice', facecolor='g')
            xlabel('Counts (per pixel)')
            ylabel('Frequency')
            title(filelist[image])
            grid(True)
            savefig(filelist[image] + ".png")
     
    def stdPlotAll(self, imageArray4D, filelist):
        '''
        Accepts a 4D numpy array and plots standard deviations of the images.
        note: assumes filenames are distances (int)
        '''
        # Turn interactive plotting off
        ioff()
        
        #initialize std array
        stdList = zeros(imageArray4D.shape[0])
        
        #get stds
        for image in range(imageArray4D.shape[0]):
            flattenedArray = imageArray4D[image].flatten()
            stdList[image] = std(flattenedArray)
        
        #create x values by remove extension from filenames and converting them to ints
        xx = self.fileNameToInt(filelist)
        
        ################### best fit (poly order=2) ###################
        
        #zip xx and yy = std values into array of tulups
        #sort list by distance (x) so xx (distances) are in the proper order in the plot
        sortedX, sortedY = self.zipAndSort(xx, stdList)
        
        #calculate polynomial (order = 2)
        f2 = poly1d(polyfit(sortedX, sortedY, 2))
        
        #calculate new x's and y's
        xFit, yFit = self.xyPolyFit(sortedX, sortedY, 2)
        
        ################### find best focus ###################
        
        #find slope = 0 for fit, this will be used to split the data to a left and right liner fit
        ##find the first derivative of the poly1d
        deriv = polyder(f2)
        ##solve deriv =ax + b for deriv = 0 (used to split data into left and right sides of the curve)
        xSplitPoint = (0-deriv.c[1])/(deriv.c[0])
        
        #get separate X and Y lists from sorted data
        sortedXL = [kk for kk in sortedX if kk <= xSplitPoint]
        sortedYL = sortedY[:len(sortedXL)]
        sortedXR = sortedX[len(sortedXL):]
        sortedYR = sortedY[len(sortedXL):]
        
        #linear fit each side
        mL, bL = polyfit(sortedXL, sortedYL, 1) #left
        mR, bR = polyfit(sortedXR, sortedYR, 1) #right
        
        #find intercept of the linear fits
        # want position where XL = XR and YL = YR using y =mx +b:
        # mL*sortedXL + bL = mR*sortedXR + bR
        xInter = (bR-bL)/(mL-mR)
        yInter = mL*xInter +bL
        
        #add intercept point to x and y value sets
        sortedXL.append(xInter)
        sortedXR.append(xInter)
        
        ################## plot stds ##################
        fig2 = figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot(sortedX, sortedY, 'ro', xFit, yFit, 
                 sortedXL, [mL*ll+bL for ll in sortedXL], 
                 sortedXR, [mR*mm+bR for mm in sortedXR])
        xlabel('Focal Position (microns)')
        ylabel('Standard Deviation')
        title('Standard Deviation versus Distance')
        text(0, 0, 'Left Linear Fit: y = ' + str(mL) + ' x + ' + str(bL) + 
             '\n\nRight Linear Fit: y = ' + str(mR) + ' x + ' + str(bR) + 
             '\n\nPolynomial Fit:\n        ' + str(f2) +
             '\n\nPolynomial Fit Max Distance= ' + str(xSplitPoint)[0:3] + ' um\n', fontsize = 7, transform=ax2.transAxes)
        grid(True)
        ax2.annotate('Best Focus = ' + str(xInter)[0:5] + ' um', xy=(xInter, yInter), 
                     xytext=(xInter+1, yInter+1), fontsize = 7, 
                     arrowprops=dict(arrowstyle='->', facecolor='black'),)  
         
        #save figure
        fig2.savefig('std_vs_position-fitted.png')
        
    def fwhmPlotAll(self, imageArray4D, filelist):
        '''
        Accepts a 4D array and finds the FWHM of the images, and plots a focus curve.
        '''
        #Create x values by remove extension from filenames and converting them to ints
        xx = self.fileNameToInt(filelist)
        
        ################### Get fwhm for all images ###################
        
        fw = fwhm()
        yy = []
        [yy.append(fw.fwhm3D(imageArray4D[ii])) for ii in range(imageArray4D.shape[0])]
        
        ################### best fit (poly order=2) ###################
        
        #zip xx and yy = fwhm values into array of tulups
        #sort list by distance (x) so xx (distances) are in the proper order in the plot
        sortedX, sortedY = self.zipAndSort(xx, yy)
        
        #calculate new x's and y's
        xFit, yFit = self.xyPolyFit(sortedX, sortedY, 2)
        
        ################### plot fwhm focus curve ###################
        
        fig = figure()
        ax = fig.add_subplot(111)
        ax.plot(xx, yy, 'ro', xFit, yFit)
        xlabel('Focal Position (microns)')
        ylabel('FWHM (pixels)')
        title('FWHM versus Distance')
        grid(True)
        text(0, 0, 'Polynomial Fit:\n        ' + str(poly1d(polyfit(sortedX, sortedY, 2))), fontsize = 7, transform=ax.transAxes)
        #save figure
        fig.savefig('fwhm_vs_position.png')
    
    def fileNameToInt(self, filelist):
        '''
        Create x values by remove extension from filenames and converting them to ints
        '''
        xx = []
        [xx.append(os.path.splitext(filelist[image])[0]) for image in range(len(filelist))]
        for ii in range(len(xx)):#get basename of files
            xx[ii] = int(basename(xx[ii]))
        return xx
    
    def zipAndSort(self, xx, yy):
        '''
        Zip xx and yy values into array of tulups
        Sort list by distance (x) so xx (distances) are in the proper order in the plot
        '''
        #zip xx and yy
        xy = []
        [xy.append(jj) for jj in zip(xx, yy)]
        #sort list by distance (x)
        sortedXY = sorted(xy, key=itemgetter(0))
        #seperate into X and Y
        sortedX = [kk[0] for kk in sortedXY]
        sortedY = [ll[1] for ll in sortedXY]
        return sortedX, sortedY
    
    def xyPolyFit(self, xx, yy, order):
        '''
        Calculate polynomial fit (order given)
        Calculate new x's and y's for plotting
        '''
        #calculate polynomial
        f2 = poly1d(polyfit(xx, yy, order))
        #calculate new x's and y's
        xFit = linspace(xx[0], xx[-1])
        yFit = f2(xFit)
        return xFit, yFit