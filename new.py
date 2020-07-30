import cv2
import numpy as np
from time import time
import matplotlib.pyplot as plt


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

        ispeak &= (x[i] > 0.05 * maxn)
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
        xx = (boxes[1][0]-boxes[0][0])
        yy = (boxes[0][1]-boxes[1][1])
        
        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        img = cv2.line(img,(boxes[0][0],boxes[0][1]),(boxes[1][0],boxes[1][1]),255,1)



        cv2.imshow('img',img)
        cv2.waitKey(0)
        a=0
        xy=[]
        pixel1=[]
        pixel2=[]
        pixel3=[]
        pixel4=[]   
        
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

        print(img)
        for i in range(height):
            for j in range(width-1):
                if(img[i][j] ==255 ):
                    xy.append(img[i,j+1])
                    '''
                    pixel1.append(img[i,j])
                    pixel2.append(img[i,j-10])
                    pixel3.append(img[i,j+10])
                    pixel4.append(img[i,j-5])
                    '''

        plt.plot(xy)
        plt.show()
        '''
        plt.plot(pixel2)
        plt.plot(pixel3)
        plt.plot(pixel4)
        pixel5=[]
        for i in range(len(pixel1)):
            pixel5.append((pixel1[i]+pixel2[i]+pixel3[i]+pixel4[i])/4)
        plt.show()
        print(pixel5)
        '''
        q=find_peaks(xy)
        print(len(q))


        '''
        img2= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        

        scale_percent = 10 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        print(resized.shape)

        img2= cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        cv2.imshow('crop',resized)
        cv2.waitKey(0)

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

histg = cv2.calcHist([img],[2],None,[256],[0,256])
a=[]
#for i in range(len(histg)):
for i in range(255):
    a.append(histg[i][0])
plt.plot(a)
plt.show()
q2 = find_peaks(a)
print(q2)
w=q2[len(q2)-2]


img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
width = img.shape[1] 
height = img.shape[0]
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