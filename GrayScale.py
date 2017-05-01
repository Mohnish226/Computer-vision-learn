#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 16:44:47 2017

@author: Mohnish_Devadiga
"""

import cv2

# Load our input image
image = cv2.imread('./images/input.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()

#Another method faster method
img = cv2.imread('./images/input.jpg',0)

cv2.imshow('Grayscale', img)
cv2.waitKey()
cv2.destroyAllWindows()