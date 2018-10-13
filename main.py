import os 
import cv2
from hotelscombine import cut_and_label
from rm_background4 import rm_background
from just_rotate import just_rotate
location = "./augmentation"

type = input('If data in '+str(location)+' are good, please type 1; if bad, please type 2 : ')

while(type != '1' and type != '2'):
    print('Incorrect input, please type again!')
    type = input('If data in '+str(location)+' are good, please type 1; if bad, please type 2 : ')
    
if type == '1':
    label_type = True
else:
    label_type = False

# cut_and_label(String DATA_DIR, Boolean label_or_not, String STORE_DIR, Boolean GOOD, Boolean flip)
cut_and_label(location, False, "./result/cut", label_type, False)
# rm_background(String DATA_DIR)
# Automatically remove background, rotate photos, and save in './result/rotate'

#rm_background("./result/cut")
just_rotate("./result/cut")

cut_and_label("./result/rotate", True, "./result/cut_after_rotate", label_type, True)
