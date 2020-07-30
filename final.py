import cv2
import argparse
import numpy as np

########################MAIN#######################################################

#read the image
img = cv2.imread("C:/Users/dell/Desktop/project/project/Dr._Viswanath/us_6144x4415pixels_113dpi_24bitdepth/W10_017_3ms_(7).tif")    

#resize the image
 
 
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
edges = cv2.Canny(gray,50,150,apertureSize = 3) 
minLineLength = 100 
maxLineGap = 10 
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap) 
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


import cv2
from time import time
boxes = []
def on_mouse(event, x, y, flags, params):
   # global img
   t = time()

   if event ==  cv2.EVENT_LBUTTONDBLCLK:
        print('Start Mouse Position: '+str(x)+', '+str(y))
        sbox = [x, y]
        boxes.append(sbox)
        # print count

   if event == cv2.EVENT_LBUTTONDBLCLK:
        print('End Mouse Position: '+str(x)+', '+str(y))
        ebox = [x, y]
        boxes.append(ebox)
        print(boxes)
        k =  cv2.waitKey(0)
        img = cv2.line(img,(sbox[0],sbox[1]),(ebox[0],ebox[1]),(255,0,0),5)
        if ord('r')== k:
            cv2.imwrite('Crop'+str(t)+'.jpg',img)
            print("Written to file")

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "C:/Users/dell/Desktop/project/project/Dr._Viswanath/3_us_6144x4415pixels_113dpi_24bitdepth/W10_017_3ms_(7).tif", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)
# keep looping until the 'q' key is pressed
