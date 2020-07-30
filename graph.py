import matplotlib.pyplot as plt
import numpy as np
import cv2

# Mouse_points function gives mouse points on mouse clicking

def mouse_points(event,x,y,flags,params):
    global img
    global point_start
    if event == cv2.EVENT_LBUTTONDOWN:
        point_start.append([x,y])
        print(x,y)

# Drow Line by slected points
def draw_one(point_start):
    global img
    for i in range(len(point_start)/2):

# slope includes here 

        point_start[2*i+1][1] = point_start[2*i+1][0] + point_start[2*i][1] - point_start[2*i][0]
    for i in range(len(point_start)/2):
        cv2.line(img,(point_start[2*i][0],point_start[2*i][1]),(point_start[2*i+1][0],point_start[2*i+1][1]),(255,0,0),0)
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)


# Draw three lines by two point selection

def draw_three(point_start):
    global img

    for i in range(4):
        point_start.append([0,0])

    for i in range(2):
        point_start[2*i+2][1] = point_start[2*i][1] + 4
        point_start[2*i+2][0] = point_start[2*i][0]
        point_start[2*i+3][0] = point_start[2*i+1][0]

        
    for i in range(len(point_start)/2):

# slope includes here 

        point_start[2*i+1][1] = point_start[2*i+1][0] + point_start[2*i][1] - point_start[2*i][0]
    for i in range(len(point_start)/2):
        cv2.line(img,(point_start[2*i][0],point_start[2*i][1]),(point_start[2*i+1][0],point_start[2*i+1][1]),(255,0,0),0)
    cv2.imshow("Original Image", img)
    cv2.waitKey(0)


# we will get pixels between two points line here and plots the  graph of pixels here

def get_pixels_graph(point_start):
    
    for i in range (len(point_start)/2):
        pixels = []
        xaxis = []

        q = point_start[2*i][1]
    
        j = 0
        while q != point_start[2*i+1][1]:
            pixels.append(img[point_start[2*i][0]-j][point_start[2*i][1]-j])
            xaxis.append(j)
            j = j+1
            q = point_start[2*i][1]-j

        plt.plot(xaxis,pixels)
    plt.grid()
#    plt.savefig('books_read_orginal.png')
    plt.show()


# image with increasing contrast 

def contrast():
    global img
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
    img = clahe.apply(img)


point_start = []

path = "/home/garhwal/Desktop/Dr_Viswanath/3_us_6144x4415pixels_113dpi_24bitdepth/W10_017 3ms (8).tif"
src = cv2.imread(path,0)
dim = (600, 600)
img = cv2.resize(src, dim, interpolation = cv2.INTER_AREA)

#   contrast()


cv2.imshow("Original Image", img)
cv2.setMouseCallback('Original Image',mouse_points)
cv2.waitKey(0)

draw_one(point_start)
get_pixels_graph(point_start)

#cv2.imwrite("/home/garhwal/Desktop/image_original.png",img)
