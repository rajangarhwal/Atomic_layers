import cv2
import numpy as np
from time import time
import matplotlib.pyplot as plt
import copy


def find_peaks(a):
    x = np.array(a)
    maxn = np.max(a)
    lenght = len(a)
    ret = []
    for i in range(lenght):
        ispeak = True
        if i-1 > 0:
            ispeak &= (x[i] > 1 * x[i-1])
        if i+1 < lenght:
            ispeak &= (x[i] > 1 * x[i+1])

        ispeak &= (x[i] > 0.55 * maxn)
        if ispeak:
            ret.append(i)
    return ret


boxes = []


#this functions help in draw a line btn any 2 points
#click at any point and drag it to its final point..
def on_mouse(event, x, y, flags, params):
    global img
    t = time()

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
        
        
        width = 360*10
        height = 224*10
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        
        img2 = copy.deepcopy(img)
        
        img = cv2.line(img,(boxes[0][0]*5,boxes[0][1]*5),(boxes[1][0]*5,boxes[1][1]*5),255,1)
        
        cv2.imshow('img',img)
        cv2.waitKey(0)
       
        
        width = int(img.shape[1])
        height = int(img.shape[0])
        '''
        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        '''
        ### this part of is just for an idea to check change in pixel 
        #IMPORTANT ---- I already i tried it as taking 4 parallel lines but still did not get satisfied output

        xy=[]
        yx=[]
        count =0;
        print(img2)

        pxl = 75
        cc=1
        for i in range(3,height):
            for j in range(width-3):
                if(img[i][j] ==255 ):
                    f=False
                    '''
                    if(abs(int(img2[i][j])-int(img2[i-3][j+3]))<4) :
                        if( abs(int(img2[i][j])-int(img2[i+3][j-3]))<4 and img2[i][j]>78):        
                            if(abs(int(img2[i-3][j+3])-int(img2[i-6][j+6]))<4) :
                                if( abs(int(img2[i+6][j-6])-int(img2[i+3][j-3]))<4):
                                                    
                                    if(abs(int(img2[i][j])-int(img2[i-9][j+9]))<4) :
                                        if( abs(int(img2[i][j])-int(img2[i+9][j-9]))<4):        
                                            if(abs(int(img2[i-3][j+3])-int(img2[i-12][j+12]))<4) :
                                                if( abs(int(img2[i+12][j-12])-int(img2[i+3][j-3]))<4):
                                                    count+=1;
                                                    f=True
                                                    for e in range(100):
                                                        img2[i-e][j+e]=255
                                                        img2[i+e][j-e]=255
                    '''
                    if(img2[i-3][j+3]>pxl) :
                        if( img2[i+3][j-3]>pxl and img2[i][j]>pxl):        
                            if(img2[i-6][j+6]>pxl) :
                                if( img2[i+6][j-6]>pxl):        
                                    if(img2[i-9][j+9]>pxl) :
                                        if( img2[i+9][j-9]>pxl):        
                                            if(img2[i-12][j+12]>pxl) :
                                                if( img2[i+12][j-12]>pxl):
                                                    count+=1;
                                                    f=True
                                                    for e in range(100):
                                                        img2[i-e][j+e]=255
                                                        img2[i+e][j-e]=255
                    if(f==False):
                        for e in range(100):
                            img2[i-e][j+e]=0
                            img2[i+e][j-e]=0
                        

        print("total layers are : ",count )

        a=[]
        for i in range(3,height):
            for j in range(width-3):
                if(img[i][j] ==255 ):
                    a.append(img2[i][j])
        plt.plot(a)
        plt.show()

        scale_percent = 20 # percent of original size
        width = int(img2.shape[1] * scale_percent / 100)
        height = int(img2.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

       # print(resized.shape)

        cv2.imshow('crop',resized)
        cv2.waitKey(0)
        '''
        print(resized.size)
        px=np.array(resized)
        print(resized)
        
        
        x1=boxes[0][0]
        x2=boxes[1][0]
        y1=boxes[0][1]
        y2=boxes[1][1]
        print(boxes)
        print(img.shape)
        print(img2.shape)
        if(x2!=x1):
            m=(y2-y1)/(x2-x1)
            c=y2-m*x2
            pixel=[]
            for x in range(x1,x2+1):
                y=int(m*x+c)
                print(x,y)
                pixel.append(img2[x,y])
                img2[x,y]=255
            print(pixel)
            
            cv2.imshow("cwc",img2)
            cv2.waitKey(0)
        if ord('r')== k:
            cv2.imwrite('Crop'+str(t)+'.jpg',resized)
            print ("Written to file")
        '''
           



img = cv2.imread(r"C:\Users\dell\Desktop\project\project\Dr._Viswanath\us_6144x4415pixels_113dpi_24bitdepth\W10_017_3ms_(7).tif")    


img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


width = img.shape[1] 
height = img.shape[0]

crop = img[(height-4410):(height+1),0:6105]

'''
for i in range(height):
    for j in range(width):
        if(img[i][j]<w-6):
            img[i-1][j]=img[i][j]
            img[i-2][j]=img[i][j]
            img[i-3][j]=img[i][j]
            img[i-4][j]=img[i][j]
            img[i-5][j]=img[i][j]
            img[i-6][j]=img[i][j]
            img[i-7][j]=img[i][j]
            img[i-8][j]=img[i][j]
            img[i-9][j]=img[i][j]
            img[i-11][j]=img[i][j]
            img[i-12][j]=img[i][j]
            img[i-13][j]=img[i][j]
            img[i-14][j]=img[i][j]
            img[i-15][j]=img[i][j]
            img[i-16][j]=img[i][j]
            img[i-17][j]=img[i][j]
            img[i-18][j]=img[i][j]
            img[i-19][j]=img[i][j]
# img = cv2.blur(img, (3,3))
#img = cv2.resize(img, None, fx = 0.25,fy = 0.25)
'''
#resize the image

width = 360*2
height = 224*2
print(width,height)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#resized = cv2.GaussianBlur(resized,(resized.shape[0],resized.shape[1],0) )


cv2.namedWindow('real image')
cv2.setMouseCallback('real image', on_mouse, 0)
cv2.imshow('real image', resized)
cv2.waitKey(0)