'''
@title general_image_processing_functions
@author: Rebecca Coles
Updated on Sep 18, 2017
Created on Sep 13, 2017

general_image_processing_functions
This project exists as a record of all of the day to day
image processing that I do.
'''

# Import #######################################################################################
from imageToArray import imageToArray
from colorAndIntensity import colorAndIntensity
################################################################################################

if __name__ == '__main__':
    im = imageToArray()
    cl = colorAndIntensity()
    
    cutList = cl.colorFinder(im.nonfitsImageToArray(), r=120)