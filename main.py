'''
@title general_image_processing_functions
@author: Rebecca Coles
Updated on Oct 25, 2017
Created on Sep 13, 2017

general_image_processing_functions
This project exists as a record of all of the day to day
image processing that I do.
'''

# Import #######################################################################################
from imageToArray import imageToArray
from colorAndIntensity import colorAndIntensity
from fileHandling import fileHandling
from fwhm import fwhm
from plots import plots
################################################################################################

if __name__ == '__main__':
    im = imageToArray()
    cl = colorAndIntensity()
    fH = fileHandling()
    #cutList = cl.colorFinder(im.nonfitsImageToArray(), r=150)
    #image = im.nonfitsImageToArray()
    #savedFITs = fH.saveAsFITs(image, '5')
    
    #hist for a 4D array of FITs images
    pl = plots()
    imageArray, fileList = im.openAllFITSImagesInDirectory()
    pl.stdPlotAll(imageArray, fileList)
    
    
    