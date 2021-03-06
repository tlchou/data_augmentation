import cv2
import numpy as np
import os
#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 100
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format
#DATA_DIR = "./result/cut" #set the picture directory

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

def rm_background(DATA_DIR):
    #== Processing =======================================================================
    # for filename in os.listdir(DATA_DIR):
        # path = './result/' + str(filename)
        # img = cv2.imread(path)
        #-- Read image -----------------------------------------------------------------------
    print(DATA_DIR)
    for filename in os.listdir(DATA_DIR):
        img = cv2.imread('./result/cut/' + filename)
        print(filename)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
        edges = cv2.dilate(edges, None)
        contour_info = []
        _, contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        for c in contours:
            contour_info.append((
                c,
                cv2.isContourConvex(c),
                cv2.contourArea(c),
            ))
        contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
        max_contour = contour_info[0]
        mask = np.zeros(edges.shape)
        cv2.fillConvexPoly(mask, max_contour[0], (255))
        mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask
        mask_stack  = mask_stack.astype('float32') / 255.0          # Use float matrices,
        img         = img.astype('float32') / 255.0                 #  for easy blending

        masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR) # Blend

        x = 0
        for i in range(0,24):
            rotated = rotate_bound(mask_stack * img, x)
            #cv2.imshow('rotated:'+ str( i * 15 ), rotated)                                   # Display
            #cv2.waitKey()
            # print(filename)
            rotated = (rotated * 255).astype('uint8')                     # Convert back to 8-bit
            filename_len = len(filename)
            filename_without_jpg = filename[0:filename_len-4]
            cv2.imwrite('./result/rotate/' + str(filename_without_jpg) + '_' + str(i) + ".jpg", rotated)
            x = x + 15
