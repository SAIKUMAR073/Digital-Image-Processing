#Assignment6:
#Task-->Read a color image,convert the color image to gray scale and do contrast maniplution.
#display output images.
import math                                                #import the required libraries.
import numpy as np
import cv2
image = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')         #reading the image.
grayscaleimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   #Converting it into grayscale.

#-----------------Contrast Manipulation-------------------
#to increase contrast we multiple image with a constant, greater than one.
#to decrease contrast we multiple image with a constant, lesser than one.

cv2.imshow("original Image",grayscaleimage)
cv2.waitKey(0)
cv2.imshow("increase contrast Image",grayscaleimage*1.1)
cv2.waitKey(0)
cv2.imshow("decrease contrast Image",grayscaleimage*0.0009)
cv2.waitKey(0)
cv2.destroyAllWindows()