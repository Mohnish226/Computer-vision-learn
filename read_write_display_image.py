#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:57:31 2017

@author: Mohnish_Devadiga
"""

import cv2 
import numpy as np

# Load an image using 'imread' specifying the path to image
input = cv2.imread('./images/input.jpg')

print 'Height of Image:', int(input.shape[0]), 'pixels'
print 'Width of Image: ', int(input.shape[1]), 'pixels'
# Our file 'input.jpg' is now loaded and stored in python 

# To display our image variable, we use 'imshow'
# The first parameter will be title shown on image window
# The second parameter is the image varialbe


cv2.imshow('Hello World', input)

# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('./images/Output/output.jpg', input)
cv2.imwrite('./images/Output/output.png', input)

# 'waitKey' allows us to input information when a image window is open

cv2.waitKey(3)

# This closes all open windows 
# Failure to place this will cause your program to hang

cv2.destroyAllWindows()
