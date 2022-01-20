#Assignment1:
#Task1-->Read a color image and convert it into gray scale image without using inbulit function(i.e do it by average method(R+G+B)/3)).
#Task2-->Convert the pixel of gray scale image to either 1 or 0.
#Task3-->Add gray image and image with pixels either 1 or 0 and add 20 to gray scale image.
#Performe the task and display the output images. 

import math                                                #import the required libraries.
import numpy as np
import cv2
image = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')        #reading the color image
m,n,v = image.shape                                       #knowing the dimensions of color image.
gray_image = np.zeros((m,n),np.uint8)                     #declaring an zeroes array for the operations of converting gray scale and pixel of garyscale image to either 1 or 0
image_onezeroes2 = np.zeros((m,n),np.uint8)
print("dimensions of image is {}x{}x{}".format(m,n,v))

#---------------------Task1------------------------------------------------------------

Sum = 0
for i in range(m):
    for j in range(n):
        for k in range(v):
            Sum = Sum + image[i][j][k]
        gray_image[i][j] = math.floor(Sum/3)
        Sum = 0

#---------------------------------Task2------------------------------
for v in range(m):
    for w in range(n):
        if(gray_image[v][w] >= 127):
            image_onezeroes2[v][w] = 1
        else:
            image_onezeroes2[v][w] = 0


cv2.imshow("original Image",image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image',gray_image)
cv2.waitKey(0)
cv2.imshow('Image with pixels 1 or 0',image_onezeroes2)
cv2.waitKey(0)
cv2.imshow('Grayscale image + Image with pixels 1 or 0',gray_image + image_onezeroes2)    #Task3
cv2.waitKey(0)
cv2.imshow('Grayscale Image + 20 ',gray_image + 20)                             #Task3
cv2.waitKey(0)
cv2.destroyAllWindows()