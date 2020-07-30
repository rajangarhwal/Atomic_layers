import cv2
import numpy as np
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



#read the image
img = cv2.imread(r"C:\Users\dell\Desktop\project\project\Dr._Viswanath\3_us_6144x4415pixels_113dpi_24bitdepth\W10_017_3ms_(7).tif")                                 
#my real image
print(img)

#resize the image

 
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 

histg = cv2.calcHist([img],[2],None,[256],[0,256])

histg1 = cv2.calcHist([resized],[2],None,[256],[0,256])

plt.plot(histg)
plt.show()
plt.plot(histg1)
plt.show()

a=[]
for i in range(255):
    a.append(histg[i][0])
plt.plot(a)
plt.show()
q2 = find_peaks(a)
print(q2)
w=q2[len(q2)-2]


resized= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

width = resized.shape[1] 
height = resized.shape[0]
for i in range(height):
    for j in range(width):
        if(resized[i][j]<w-6):
            resized[i-1][j]=resized[i][j]
            resized[i-2][j]=resized[i][j]
            resized[i-3][j]=resized[i][j]
            resized[i-4][j]=resized[i][j]
            resized[i-5][j]=resized[i][j]


#resize the image
 
 
scale_percent = 20 # percent of original size
width = int(resized.shape[1] * scale_percent / 100)
height = int(resized.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(resized, dim, interpolation = cv2.INTER_AREA)
 
cv2.imshow("img",resized)
cv2.waitKey(0)
'''
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,60,70,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

#resize the image
 
 
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
cv2.imshow('houghlines3.jpg',img)
cv2.waitKey(0)
'''