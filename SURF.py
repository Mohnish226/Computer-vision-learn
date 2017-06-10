#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 22:02:33 2017

@author: Mohnish_Devadiga
"""

import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Create SURF Feature Detector object
surf = cv2.xfeatures2d.SIFT_create()

keypoints, descriptors = surf.detectAndCompute(gray, None)
print "Number of keypoints Detected: ", len(keypoints)

outImage = np.zeros((1,1))

# Draw rich key points on input image
image = cv2.drawKeypoints(image, keypoints, outImage, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Feature Method - SURF', image)
cv2.waitKey()
cv2.destroyAllWindows()