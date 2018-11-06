import os
import cv2
import shutil
from hotelscombine import cut_and_label
# from rm_background4 import rm_background
from color_rm_bkgnd import rm_background
from just_rotate import just_rotate
from resize import resize
location_A = "./augmentation/good"
location_B = "./augmentation/bad"
store_A = "./result/train_data/good_train"
store_B = "./result/train_data/bad_train"
#
# type = input('If data in augmentation are good, please type 1; if bad, please type 2 : ')
#
# while(type != '1' and type != '2'):
#     print('Incorrect input, please type again!')
#     type = input('If data in augmentation are good, please type 1; if bad, please type 2 : ')
#
# if type == '1':
#     label_type = True
#     location = location_A
#     store_train = store_A
# else:
#     label_type = False
#     location = location_B
#     store_train = store_B

# create folder for data augmentation

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder('./result')
shutil.rmtree('./result')
createFolder('./result')

createFolder('./result/cut')
createFolder('./result/cut_after_rotate')
createFolder('./result/label')
createFolder('./result/rm_bkgnd')
createFolder('./result/rotate')
createFolder('./result/train_data/good_train')
createFolder('./result/train_data/bad_train')

# --------- Deal with Good bean --------- #
# cut_and_label(String DATA_DIR, Boolean label_or_not, String STORE_DIR, Boolean GOOD, Boolean flip)
cut_and_label(location_A, False, "./result/cut", True, False)
# rm_background(String DATA_DIR)
rm_background("./result/cut")

just_rotate("./result/rm_bkgnd")

cut_and_label("./result/rotate", True, "./result/cut_after_rotate", True, True)

resize("./result/cut_after_rotate",store_A)

shutil.rmtree('./result/cut')
shutil.rmtree('./result/cut_after_rotate')
shutil.rmtree('./result/label')
shutil.rmtree('./result/rm_bkgnd')
shutil.rmtree('./result/rotate')
createFolder('./result/cut')
createFolder('./result/cut_after_rotate')
createFolder('./result/label')
createFolder('./result/rm_bkgnd')
createFolder('./result/rotate')

# --------- Deal with Bad bean --------- #
# cut_and_label(String DATA_DIR, Boolean label_or_not, String STORE_DIR, Boolean GOOD, Boolean flip)
cut_and_label(location_B, False, "./result/cut", False, False)
# rm_background(String DATA_DIR)
rm_background("./result/cut")

just_rotate("./result/rm_bkgnd")

cut_and_label("./result/rotate", True, "./result/cut_after_rotate", False, True)

resize("./result/cut_after_rotate",store_B)
