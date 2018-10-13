import cv2
import numpy as np
import os

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH),borderValue=(0,0,0))

def just_rotate(DATA_DIR):
    for filename in os.listdir(DATA_DIR):
        x=30
        img = cv2.imread(str(DATA_DIR)+'/'+str(filename))
        
        while(x<360):
            rotated = rotate_bound(img, x)
            #cv2.imshow('a',rotated)
            #cv2.imshow('rotated:'+ str( i * 15 ), rotated)                                   # Display
            #cv2.waitKey(0)
            # print(filename)
            #rotated = (rotated * 255).astype('uint8')                     # Convert back to 8-bit
            filename_len = len(filename)
            filename_without_jpg = filename[0:filename_len-4]
            cv2.imwrite('./result/rotate/' + str(filename_without_jpg) + '_' + str(x) + ".jpg", rotated)
            x = x + 30