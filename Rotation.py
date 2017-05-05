#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:29:05 2017

@author: Mohnish_Devadiga
"""

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
height, width = image.shape[:2]

# Divide by two to rototate the image around its centre
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Other Option to Rotate But 90° at a time

img = cv2.imread('images/input.jpg')

rotated_image = cv2.transpose(img)

cv2.imshow('Rotated Image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

# Now to a horizontal flip.
flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipped) 
cv2.waitKey()
cv2.destroyAllWindows()