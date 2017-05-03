#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:00:48 2017

@author: Mohnish_Devadiga
"""

import cv2
import numpy as np

# We need to import matplotlib to create our histogram plots
from matplotlib import pyplot as plt

# For First Image
print "First Image"

image = cv2.imread('images/input.jpg')

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# We plot a histogram, ravel() flatens our image array 
plt.hist(image.ravel(), 256, [0, 256]); 
plt.show()

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
    
plt.show()

# For Second Image
print "Second Image"

image2 = cv2.imread('images/tobago.jpg')

histogram = cv2.calcHist([image2], [0], None, [256], [0, 256])

# We plot a histogram, ravel() flatens our image array 
plt.hist(image2.ravel(), 256, [0, 256]); 
plt.show()

# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image2], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
    
plt.show()