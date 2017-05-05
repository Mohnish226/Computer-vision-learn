#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:20:02 2017

@author: Mohnish_Devadiga
"""

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')

# Store height and width of the image
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4

#  T  =  | 1 0 Tx |
#        | 0 1 Ty |

# T is our translation matrix
T = np.float32([[1, 0, quarter_width], [0, 1,quarter_height]])

# To see the Matrix
print T

# We use warpAffine to transform the image using the matrix, T
img_translation = cv2.warpAffine(image, T, (width, height))
cv2.imshow('Translation', img_translation)
cv2.waitKey()
cv2.destroyAllWindows()