import cv2
import numpy as np
from time import time
import math
import matplotlib.pyplot as plt




boxes = []



#this functions help in draw a line btn any 2 points
#click at any point and drag it to its final point..
def on_mouse(event, x, y, flags, params):
    global img
    
    if (event == cv2.EVENT_LBUTTONDOWN):
        print ('Start Mouse Position: '+str(x)+', '+str(y))
        
        boxes.append([x,y])
        
        # print count
        # print sbox

    elif(event == cv2.EVENT_LBUTTONUP):
        print ('End Mouse Position: '+str(x)+', '+str(y))
        
        boxes.append([x,y])
        print (boxes)
        print(boxes[0][0],boxes[0][1],boxes[1][0],boxes[1][1])
        
        scale_percent = 100 # percent of original size
        width = int(img.shape[1] * scale_percent/100)
        height = int(img.shape[0] * scale_percent/100)
        dim = (width, height)
        #img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        
        y1=-boxes[1][1]*10+boxes[0][1]*10
        x1=boxes[1][0]*10-boxes[0][0]*10

        g = math.gcd(y1,x1)
        y1=y1/g
        x1=x1/g

        w=width
        h=height

        while(w%x1!=0):
            w-=1
        while(h%y1!=0):
            h-=1

        print(w,h,"size after croping of image")
        w=w/x1
        h=h/y1
        while(w<width/10 and h<height/10):
            w*=2
            h*=2
        w/=2
        h/=2

        print(w,h,"after croping we have to resize the image to this dimmensions")

        print("for 10%")
        print(x1,y1)



img = cv2.imread(r"C:\Users\dell\Desktop\project\project\Dr._Viswanath\us_6144x4415pixels_113dpi_24bitdepth\W10_017_3ms_(7).tif")    

histg = cv2.calcHist([img],[2],None,[256],[0,256])
a=[]
#for i in range(len(histg)):
for i in range(255):
    a.append(histg[i][0])
plt.plot(a)


img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#resize the image

scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
print(width,height)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#resized = cv2.GaussianBlur(resized,(resized.shape[0],resized.shape[1],0) )


cv2.namedWindow('real image')       
cv2.setMouseCallback('real image', on_mouse, 0)
    
cv2.imshow('real image', resized)
cv2.waitKey(0)