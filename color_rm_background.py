# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 00:15:56 2018

@author: user
"""

import glob as gb
import cv2
import numpy as np
import os

img_path = gb.glob("C:/Users/user/Downloads/bean_data/*.jpg")

for path in img_path:
    img  = cv2.imread(path)
    #img=cv2.resize(img,None,fx=0.5,fy=0.5)
    rows,cols,channels = img.shape
    #转换hsv
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([0,0,0])   #bad 0 0 0
    upper_blue=np.array([180,255,50]) #bad 180 255 40
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #cv2.imshow('Mask', mask)

    #腐蚀膨胀
    erode=cv2.erode(mask,None,iterations=1)
    #cv2.imshow('erode',erode)
    dilate=cv2.dilate(erode,None,iterations=1)
    #cv2.imshow('dilate',dilate)

    #遍历替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i,j]==255:
                img[i,j]=(0,0,0)#此处替换颜色，为BGR通道

    new_im = np.zeros((150,150,3))
    new_im[0:0+x,0:y] = img
    # new_im.paste(im, ((size - x) / 2, (size - y) / 2))


    #cv2.imshow('res',img)
    cv2.imwrite('C:/Users/user/Downloads/non_background/'+os.path.basename(path), new_im)
#    cv2.waitKey(10000)
#    cv2.destroyAllWindows()
