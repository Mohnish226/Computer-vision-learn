#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:56:03 2017

@author: Mohnish_Devadiga
"""

import cv2
import numpy as np

img = cv2.imread('images/chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# We specific the top 50 corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 150)

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,0), 2)
    
cv2.imshow("Corners Found", img)
cv2.waitKey()
cv2.destroyAllWindows()