#Assignment3:
#Task: Create two images one with a white circle at center and another with a white rentangle at center and performe all logical gate operations on both images and display the output images. 

import math                                  #import the required libraries.
import numpy as np
import cv2

Image1 = np.zeros((512,512),np.uint8)         #declaring two black images to do operations.
Image2 = np.zeros((512,512),np.uint8)

Image1 = cv2.circle(Image1,(235,250),80,(255,255,255),-1)            
Image2 = cv2.rectangle(Image2,(100,300),(330,190),(255,255,255),-1)          #Making a white circle and rectangle at center of two images respectively


#performing all logic gates operations and dispalying the output images

cv2.imshow("Image with white rectangle at center",Image2)
cv2.waitKey(0)
cv2.imshow("Image with white circle at center",Image1)
cv2.waitKey(0)
cv2.imshow("AND operation on images",cv2.bitwise_and(Image1,Image2))
cv2.waitKey(0)
cv2.imshow("NAND operation on images",cv2.bitwise_not(cv2.bitwise_and(Image1,Image2)))
cv2.waitKey(0)
cv2.imshow("OR operation on images",cv2.bitwise_or(Image1,Image2))
cv2.waitKey(0)
cv2.imshow("NOR operation on images",cv2.bitwise_not(cv2.bitwise_or(Image1,Image2)))
cv2.waitKey(0)
cv2.imshow("EXOR operation on images",cv2.bitwise_xor(Image1,Image2))
cv2.waitKey(0)
cv2.imshow("EXNOR operation on images",cv2.bitwise_not(cv2.bitwise_xor(Image1,Image2)))
cv2.waitKey(0)