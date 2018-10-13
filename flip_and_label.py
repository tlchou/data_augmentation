import os
import cv2

def writeXML(width,height,num,file_name,coffee_type):

    if coffee_type is "good":
        label_type = "good_bean"
    else:
        label_type = "bad_bean"
    new_name = str(file_name[0:len(file_name)-4])

    f = open("./result/label/"+str(new_name)+".xml","w+")
    f.write('<annotation>\n\t<folder>'+str(coffee_type)+'</folder>\n\t<filename>'+str(file_name)+'</filename>\n\t<path>C:\\coffee\\'+str(coffee_type)+'\\'+str(file_name)+'</path>\n\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n\t<size>\n\t\t<width>'+str(width)+'</width>\n\t\t<height>'+str(height)+'</height>\n\t\t<depth>3</depth>\n\t</size>\n\t<segmented>0</segmented>\n\t<object>\n\t\t<name>'+str(label_type)+'</name>\n\t\t<pose>Unspecified</pose>\n\t\t<truncated>1</truncated>\n\t\t<difficult>0</difficult>\n\t\t<bndbox>\n\t\t\t<xmin>1</xmin>\n\t\t\t<ymin>1</ymin>\n\t\t\t<xmax>'+str(width)+'</xmax>\n\t\t\t<ymax>'+str(height)+'</ymax>\n\t\t</bndbox>\n\t</object>\n</annotation>')


FLIP_STORE_DIR = './result/cut_after_rotate/'


def flip_image(image,filename,w,h,num,coffee_type):

    flipped_horizontally = cv2.flip(image,1) #Flipped horizontally
    flipped_vertically = cv2.flip(image,0) #Flipped vertically
    flipped_hori_verti = cv2.flip(image,-1) #Flipped horizontally and vertically

    # filename = A_A_01.jpg
    name_without_jpg = str(filename[0:len(filename)-4]) 
    # name_without_jpg = A_A_01

    # Rewrite name
    filpped_name_with_jpg_hori = name_without_jpg+'_1.jpg' # A_A_01_1.jpg
    filpped_name_with_jpg_verti = name_without_jpg+'_0.jpg' # A_A_01_0.jpg
    flipped_name_with_jpg_hori_verti = name_without_jpg+'_-1.jpg' # A_A_01_-1.jpg

    # Write Flipped image
    cv2.imwrite(FLIP_STORE_DIR+filpped_name_with_jpg_hori,flipped_horizontally)
    cv2.imwrite(FLIP_STORE_DIR+filpped_name_with_jpg_verti,flipped_vertically)
    cv2.imwrite(FLIP_STORE_DIR+flipped_name_with_jpg_hori_verti,flipped_hori_verti)

    # Write XML
    writeXML(w,h,num,filpped_name_with_jpg_hori,coffee_type)
    writeXML(w,h,num,filpped_name_with_jpg_verti,coffee_type)
    writeXML(w,h,num,flipped_name_with_jpg_hori_verti,coffee_type)



    

