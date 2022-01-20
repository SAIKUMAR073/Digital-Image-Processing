#Assignment2:
#Task-->Read a color image,convert the color image to gray scale and dispaly both images.
#Make some part of that gray scale image total black and display it.Now subtract this to images andd display output image.

import math                                                #import the required libraries.
import numpy as np
import cv2
image = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')        #reading the color image
m,n,v = image.shape                                       #knowing the dimensions of color image.
gray_image = np.zeros((m,n),np.uint8)                     #declaring an zeroes array for the operations of converting gray scale and pixel of garyscale image to either 1 or 0
gray_image2 = np.zeros((m,n),np.uint8)  
image_onezeroes2 = np.zeros((m,n),np.uint8)
print("dimensions of image is {}x{}x{}".format(m,n,v))

#Converting Color image to gray scale
Sum = 0
for i in range(m):
    for j in range(n):                            
        for k in range(v):
            Sum = Sum + image[i][j][k]
        gray_image[i][j] = math.floor(Sum/3)
        Sum = 0

for x in range(m):
    for y in range(n):
        gray_image2[x][y] = gray_image[x][y]

#making some part of gray scale image to black
for x in range(20,720,1):
   for y in range(300,980,1):
       gray_image2[x][y] = 0

cv2.imshow("original Image",image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image',gray_image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image2',gray_image2)
cv2.waitKey(0)
cv2.imshow('Grayscale Image - Grayscale Image2',abs(gray_image - gray_image2)) #Subtraction of two of images
cv2.waitKey(0)