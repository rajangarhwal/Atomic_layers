import cv2
import argparse
import numpy as np

########################MAIN#######################################################

#read the image
img = cv2.imread(r"C:\Users\dell\Desktop\project\Dr._Viswanath\us_6144x4415pixels_113dpi_24bitdepth\W10_017_3ms_(7).tif")    



img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
boxes = []
#resize the image
 
 

dim = (int(0.1*img.shape[0]), int(0.1*img.shape[1]))
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
width = 376*2
height = 232*2
dim = (width, height)
#dim = (height, width)
#crop
img=img[0:611*2,0:435*2]
#img=img[0:437,0:609]
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

total=0

def on_mouse(event, x, y, flags, params):
    global img
    global boxes
    global total
    if(event ==  cv2.EVENT_LBUTTONUP):
        print('Start Mouse Position: '+str(x)+', '+str(y))
        sbox = [x, y]
        boxes.append(sbox)
        # print count
        print(boxes)
        if(len(boxes)==2):
            for i in range(boxes[0][0],boxes[1][0]):
                cnt=0
                
                for j in range(30):
                    if(int(img[boxes[0][1]-j,i+j])-int(img[boxes[0][1]-1-j,i+j])>0):        
                        if(abs(int(img[boxes[0][1],i])-int(img[boxes[0][1]-j,i+j]))<4):
                            cnt+=1    
                    if(int(img[boxes[0][1]+j,i-j])-int(img[boxes[0][1]-1+j,i-j])>0):    
                        if(abs(int(img[boxes[0][1],i])-int(img[boxes[0][1]+j,i-j]))<4):
                            cnt+=1
                if(cnt>30):
                    for j in range(30):
                        img[boxes[0][1]-j,i+j]=255
                        img[boxes[0][1]+j,i-j]=255
                    total+=1
            print(total)
            cv2.imshow('img',img)
            cv2.waitKey(0)
    

cv2.namedWindow('real image')       
cv2.setMouseCallback('real image', on_mouse, 0)
    
cv2.imshow('real image', img)
cv2.waitKey(0)