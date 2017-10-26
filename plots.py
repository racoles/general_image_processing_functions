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
from numpy import std, zeros, poly1d, polyfit, linspace, polyder
from matplotlib.pyplot import ioff, xlabel, ylabel, title, grid, savefig, figure, text
import os
from os.path import basename
from operator import itemgetter
from scipy import optimize
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
        
        #std array
        stdList = zeros(imageArray4D.shape[0])
        
        #get stds
        for image in range(imageArray4D.shape[0]):
            flattenedArray = imageArray4D[image].flatten()
            stdList[image] = std(flattenedArray)
        
        #create x values by remove extension from filenames and converting them to ints
        xx = []
        [xx.append(os.path.splitext(filelist[image])[0]) for image in range(len(filelist))]
        for ii in range(len(xx)):#get basename of files
            xx[ii] = int(basename(xx[ii]))
            
        #zip xx and yy values into array of tulups
        xy = []
        [xy.append(jj) for jj in zip(xx, stdList)]
        
        #sort list by distance (x)
        sortedXY = sorted(xy, key=itemgetter(0))
        
        ################### best fit (poly order=2)###################
        
        #calculate polynomial (order = 2)
        f2 = poly1d(polyfit(sortedXY[:][0], sortedXY[:][1], 2))
        
        #calculate new x's and y's  (order = 2)
        xFit = linspace(sortedXY[0][0], sortedXY[-1][0])
        yFit = f2(xFit)
        
        ################### find best focus ###################
        
        #find slope = 0 for fit, this will be used to split the data to a left and right liner fit
        ##find the first derivative of the poly1d
        deriv = polyder(f2)
        ##solve x for y = 0 (used to split data into left and right sides of the curve)
        xSplitPoint = optimize.newton(deriv, 20) # the int is an initial estimate of the zero that is near the actual zero.
        
        #get separate X and Y lists from sorted data
        sortedXL = [kk[0] for kk in sortedXY if kk[0] <= xSplitPoint]
        sortedYL = [ll[1] for ll in sortedXY if ll[0] <= xSplitPoint]
        sortedXR = [mm[0] for mm in sortedXY if mm[0] >= xSplitPoint]
        sortedYR = [nn[1] for nn in sortedXY if nn[0] >= xSplitPoint]
        #linear fit each side
        mL, bL = polyfit(sortedXL, sortedYL, 1) #left
        mR, bR = polyfit(sortedXR, sortedYR, 1) #right
        
        #find intercept of the linear fits
        # want position where XL = XR and YL = YR using y =mx +b:
        # mL*sortedXL + bL = mR*sortedXR + bR
        # xInter = (bR-bL)/(mL-mR)
        # yInter = mL*xInter +bL
        xInter = (bR-bL)/(mL-mR)
        yInter = mL*xInter +bL
        
        ################## plot stds ##################
        fig2 = figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot(sortedXY[:][0], sortedXY[:][1], 'ro', 
                 xFit, yFit, 
                 sortedXY[:][0], mL*sortedXY[:][0]+bL,
                 sortedXY[:][0], mR*sortedXY[:][0]+bR)
        xlabel('Distances (mm)')
        ylabel('Standard Deviation')
        title('Standard Deviation versus Distance')
        text(0, 0, 'Polynomial Fit (Order = 2):\n      ' + str(f2), fontsize = 7, transform=ax2.transAxes)
        print(str(f2) + '\n\n')
        grid(True)
        ax2.annotate('Best Focus = ' + str(xInter), xy=(xInter, yInter), 
                     xytext=(xInter+4, yInter+3), fontsize = 7, 
                     arrowprops=dict(arrowstyle='->', facecolor='black'),)
        #save figure
        fig2.savefig('std_vs_dis-fitted.png')
        
    def sup(self,s):
        '''
        Convert an integer in to a superscript representation in UTF-8
        from:
        https://gist.github.com/giannitedesco/637a936a91982cfc0c10#file-poly-py-L51
        '''
        c = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        out = ''
        s = int(s)
        while s:
            d = s % 10
            s /= 10
            out = c[d] + out
        return out
        
    def pretty(self, p):
        '''
        Pretty print a numpy poly1d
        from:
        https://gist.github.com/giannitedesco/637a936a91982cfc0c10#file-poly-py-L51
        '''
        out = ''
        for i, c in enumerate(p):
            def mul(co, b = True):
                if 1.0 == co.round():
                    return 'x'
                else:
                    if b:
                        return '(%g*x)'%co
                    else:
                        return '%g*x'%co
                    power = len(p) - i
                    if i:
                        if c < 0:
                            out = out + ' - '
                            c = -c
                        else:
                            out = out + ' + '
                    if power == 0:
                        out = out + '%s'%c
                    elif power == 1:
                        out = out + mul(c, b = False)
                    else:
                        out = out + '%s%s'%(mul(c), self.sup(power))
        return out
        
            