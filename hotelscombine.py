import os
import cv2
import numpy as np
from flip_and_label import flip_image

'''
coffee_type = "good" #set the label
num = 0
'''
#DATA_DIR = "./augmentation" #set the picture directory
file_data = []

def writeXML(width,height,num,file_name,coffee_type):

    if coffee_type is "good":
        label_type = "good_bean"
    else:
        label_type = "bad_bean"
    new_name = str(file_name[0:len(file_name)-4])

    f = open("./result/label/"+str(new_name)+".xml","w+")
    f.write('<annotation>\n\t<folder>'+str(coffee_type)+'</folder>\n\t<filename>'+str(file_name)+'</filename>\n\t<path>C:\\coffee\\'+str(coffee_type)+'\\'+str(file_name)+'</path>\n\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n\t<size>\n\t\t<width>'+str(width)+'</width>\n\t\t<height>'+str(height)+'</height>\n\t\t<depth>3</depth>\n\t</size>\n\t<segmented>0</segmented>\n\t<object>\n\t\t<name>'+str(label_type)+'</name>\n\t\t<pose>Unspecified</pose>\n\t\t<truncated>1</truncated>\n\t\t<difficult>0</difficult>\n\t\t<bndbox>\n\t\t\t<xmin>1</xmin>\n\t\t\t<ymin>1</ymin>\n\t\t\t<xmax>'+str(width)+'</xmax>\n\t\t\t<ymax>'+str(height)+'</ymax>\n\t\t</bndbox>\n\t</object>\n</annotation>')

def cut_and_label(DATA_DIR,label,STORE_DIR,GOOD,flip):

    if GOOD:
        coffee_type = "good"
    else:
        coffee_type = "bad"

    num = 0

    for filename in os.listdir(DATA_DIR):
        # if filename[len(filename)-1] != 'g':
        #     continue
        print("Loading: " + str(filename))


        # read image
        # wget https://bigsnarf.files.wordpress.com/2017/05/hammer.png
        #file_name = "A_01"
        #file_name_jpg = file_name+".jpg"
        path = DATA_DIR+'/'+str(filename) #set the picture directory
        print(path)
        img = cv2.pyrDown(cv2.imread(path, cv2.IMREAD_UNCHANGED))
        # img = cv2.imread(path)


        # threshold image
        ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),64, 255, cv2.THRESH_BINARY)#ori=127
        # find contours and get the external one
        image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        # with each contour, draw boundingRect in green
        # a minAreaRect in red and
        # a minEnclosingCircle in blue

        for c in contours:
            # get the bounding rect
            x, y, w, h = cv2.boundingRect(c)
            # draw a green rectangle to visualize the bounding rect
            if h > 120 and w>120:
                #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                print("x = "+str(x)+", y = "+str(y)+", w = "+str(w)+", h = "+str(h)+"\n")
                if coffee_type == 'good':
                    print("A")
                    #cv2.imwrite("./result/cut/A"+"_"+filename,img[y:y+h,x:x+w,:])
                    store_name = 'A_'+str(num)+'_'+filename
                    cv2.imwrite(STORE_DIR+"/"+store_name+'',img[y:y+h,x:x+w,:])
                    if label:
                        writeXML(w,h,num,store_name,coffee_type)
                    if flip:
                        flip_image(img[y:y+h,x:x+w,:],store_name,w,h,num,coffee_type)

                else:
                    print("B")
                    #cv2.imwrite("./result/cut/A"+"_"+str(num)+"_1.jpg",img[y:y+h,x:x+w,:])
                    store_name = 'B_'+str(num)+'_'+filename
                    cv2.imwrite(STORE_DIR+"/"+store_name,img[y:y+h,x:x+w,:])
                    if label:
                        writeXML(w,h,num,store_name,coffee_type)
                    if flip:
                        flip_image(img[y:y+h,x:x+w,:],store_name,w,h,num,coffee_type)

                num = num+1
                #img[x,y,:] = (255,0,0)
                # get the min area rect
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            # convert all coordinates floating point values to int
            box = np.int0(box)
            # draw a red 'nghien' rectangle
            #cv2.drawContours(img, [box], 0, (0, 0, 255))

            # finally, get the min enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(c)
            # convert all values to int
            center = (int(x), int(y))
            radius = int(radius)
            # and draw the circle in blue
            #img = cv2.circle(img, center, radius, (255, 0, 0), 2)



        print(len(contours))
        #cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

        #cv2.imshow("contours", img)
        #cv2.imwrite("./result/detect.jpg",img)
        #ESC = 27
        '''
        while True:
            keycode = cv2.waitKey()
            if keycode != -1:
                keycode &amp;= 0xFF
            if keycode == ESC:
                break
    '''
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
