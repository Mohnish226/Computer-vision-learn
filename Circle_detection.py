#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 23:26:46 2017

@author: Mohnish_Devadiga
"""

import numpy as np
import argparse
import cv2
import cv2.cv as cv
 
image = cv2.imread('images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 10)
 
for i in circles[0,:]:
       # draw the outer circle
       cv2.circle(image,(i[0], i[1]), i[2], (255, 0, 0), 2)
      
       # draw the center of the circle
       cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)
 
cv2.imshow('detected circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()