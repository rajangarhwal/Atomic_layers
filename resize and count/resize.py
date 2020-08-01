import cv2
import numpy as np
from time import time
import math
import matplotlib.pyplot as plt



f=True
box1 = []

#this functions help in draw a line btn any 2 points
#click at any point and drag it to its final point..
def on_mouse(event, x, y, flags, params):
    global img
    global box1
    scale_percent = 100 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    width1=width
    height1=height
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    
    if (event == cv2.EVENT_LBUTTONUP):
        print ('Start Mouse Position: '+str(x)+', '+str(y))
        box1.append([x,y])
        if(len(box1)==2):
            img2 = img.copy()
            print(box1)
            x1=box1[0][0]
            y1=box1[0][1]
            x2=box1[1][0]
            y2=box1[1][1]
            print(width,height)
            for i in range(x1,width):
                if(abs(int(img[y1][i])-int(img[y1][i-10]))>5):
                    box1[0][0]=i
                    img2[y1][i]=255
                    print(i)
                    break
                img2[y1][i]=255
            for i in range(x2,width):
                if(abs(int(img[y2][i])-int(img[y2][i-10]))>5):
                    box1[1][0]=i
                    img2[y2][i]=255
                    print(i)
                    break
                img2[y2][i]=255
            print(box1)
            cv2.imshow('real image', img2)
            cv2.waitKey(0)
            # important
            print(box1)
            y1=-box1[1][1]+box1[0][1]
            x1=box1[1][0]-box1[0][0]

            print(x1,y1)
            g = math.gcd(y1,x1)
            y1=y1/g
            x1=x1/g

            print(x1,y1)
            w=width1
            h=height1

            while(w%x1!=0):
                w-=1
            while(h%y1!=0):
                h-=1

            
            print(w,h,"size after croping of image")
            w=w/x1
            h=h/y1
            while(w<width and h<height):
                w*=2
                h*=2
            w/=2
            h/=2

            print(w,h,"after croping we have to resize the image to this dimmensions")

            cv2.imshow('real image', img)
            cv2.waitKey(0)
            print("for 10%")
            print(x1,y1)




img = cv2.imread(r"C:\Users\dell\Desktop\project\Dr._Viswanath\us_6144x4415pixels_113dpi_24bitdepth\W10_017_3ms_(7).tif")    

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



