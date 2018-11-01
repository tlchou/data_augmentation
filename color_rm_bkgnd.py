import cv2
import numpy as np
import os


def rm_background(DATA_DIR):
    max_H = 0
    max_L = 0
    square_size = 0
    for filename in os.listdir(DATA_DIR):
        path = DATA_DIR+'/'+str(filename) #set the picture directory
        img  = cv2.imread(path)
        sp = img.shape
        height = sp[0]
        length = sp[1]
        if height>max_H:
            max_H = height
        if length>max_L:
            max_L = length
            
    if max_L>max_H:
        square_size = max_L
    else:
        square_size = max_H

    for filename in os.listdir(DATA_DIR):
        path = DATA_DIR+'/'+str(filename) #set the picture directory
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

        new_im = np.zeros((square_size,square_size,3))
        new_im[0:rows,0:cols] = img
        #cv2.imshow('res',img)
        cv2.imwrite('./result/rm_bkgnd/' + os.path.basename(filename), new_im)
    #    cv2.waitKey(10000)
    #    cv2.destroyAllWindows()
