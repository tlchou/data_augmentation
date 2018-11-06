import os
import cv2
import shutil
from hotelscombine import cut_and_label
# from rm_background4 import rm_background
from color_rm_bkgnd import rm_background
from just_rotate import just_rotate
from resize import resize
location = "./augmentation"

type = input('If data in '+str(location)+' are good, please type 1; if bad, please type 2 : ')

while(type != '1' and type != '2'):
    print('Incorrect input, please type again!')
    type = input('If data in '+str(location)+' are good, please type 1; if bad, please type 2 : ')

if type == '1':
    label_type = True
else:
    label_type = False

# create folder for data augmentation
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

shutil.rmtree('./result')
createFolder('./result')
createFolder('./result/cut')
createFolder('./result/cut_after_rotate')
createFolder('./result/label')
createFolder('./result/rm_bkgnd')
createFolder('./result/rotate')
createFolder('./result/train_data')


# cut_and_label(String DATA_DIR, Boolean label_or_not, String STORE_DIR, Boolean GOOD, Boolean flip)
cut_and_label(location, False, "./result/cut", label_type, False)

# rm_background(String DATA_DIR)
# Automatically remove background, rotate photos, and save in './result/rotate'

rm_background("./result/cut")
just_rotate("./result/rm_bkgnd")

cut_and_label("./result/rotate", True, "./result/cut_after_rotate", label_type, True)
resize("./result/cut_after_rotate")
