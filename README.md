# Data Augmentation
Including remove background of images, rotate images and flip images.

## Installation
'OpenCV-Version' : '3.4.2.17'
```bash 
pip install opencv-python
```

## Usage 
```python 
import cv2
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_bound = np.array([0,0,0])   #bad 0 0 0
upper_bound = np.array([180,255,50]) #bad 180 255 40
mask = cv2.inRange(hsv, lower_bound, upper_bound)

erode = cv2.erode(mask,None,iterations=1) 
dilate = cv2.dilate(erode,None,iterations=1)

for i in range(rows):
            for j in range(cols):
                if dilate[i,j] == 255:
                    img[i,j] = (0,0,0) # remove background by color mask
```
## Image source
Two type of image 'good', 'bad' coffee bean
### Good bean example
![](https://github.com/tlchou/data_augmentation/blob/master/augmentation/good/1.bmp)
### Bad bean example
![](https://github.com/tlchou/data_augmentation/blob/master/augmentation/bad/1.bmp)
