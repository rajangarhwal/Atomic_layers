import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "/home/garhwal/Desktop/Dr_Viswanath/3_us_6144x4415pixels_113dpi_24bitdepth/W10_017 3ms (8).tif"
src = cv2.imread(path,0)
dim = (600, 600)
img = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
img = clahe.apply(img)



'''edges = cv2.Canny(img,70,210)
print(img.shape, edges.shape)
cv2.imshow("Canny",edges)
cv2.waitKey(0)'''





laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

print(laplacian.shape)
cv2.imshow("laplacian",laplacian)
cv2.waitKey(0)
print("LALLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
print(sobelx.shape)
cv2.imshow("sobelx",sobelx)
cv2.waitKey(0)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(sobely.shape)
cv2.imshow("sobely",sobely)
cv2.waitKey(0)

'''
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()'''