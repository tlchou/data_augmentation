import cv2
import numpy as np
import os


def resize(DATA_DIR,STORE_DIR):
    for filename in os.listdir(DATA_DIR):
        max_H = 0
        max_L = 0
        square_size = 0
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

        rows,cols,channels = img.shape
        new_im = np.zeros((square_size,square_size,3))
        new_im[0:rows,0:cols] = img
        resized_image = cv2.resize(new_im, (180, 180)) # fix the image size
        #cv2.imshow('res',img)
        # cv2.imwrite(STORE_DIR+"/"+store_name,img[y:y+h,x:x+w,:])
        cv2.imwrite(STORE_DIR+ "/" + os.path.basename(filename), resized_image)
'''
    for filename in os.listdir(DATA_DIR):
        path = DATA_DIR+'/'+str(filename) #set the picture directory
        img  = cv2.imread(path)
        rows,cols,channels = img.shape
        #img=cv2.resize(img,None,fx=0.5,fy=0.5)
        new_im = np.zeros((square_size,square_size,3))
        new_im[0:rows,0:cols] = img
        resized_image = cv2.resize(new_im, (180, 180)) # fix the image size
        #cv2.imshow('res',img)
        # cv2.imwrite(STORE_DIR+"/"+store_name,img[y:y+h,x:x+w,:])
        cv2.imwrite(STORE_DIR+ "/" + os.path.basename(filename), resized_image)
'''
