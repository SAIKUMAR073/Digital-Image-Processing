#Assignment4:
#Task---> read a color image and display its reddish,greenisg and bluish image

import cv2

image_original = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')
image_reddish = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')
image_greenish = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')
image_blueish = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')

image_blueish[:,:,1],image_blueish[:,:,2] = 0,0
image_greenish[:,:,0],image_greenish[:,:,2] = 0,0            #Making other layer's pixel to 0 so that we can obtain image of only required layer
image_reddish[:,:,0],image_reddish[:,:,1] = 0,0

cv2.imshow("Original Image",image_original)
cv2.waitKey(0)
cv2.imshow("Reddish Image",image_reddish)
cv2.waitKey(0)
cv2.imshow("Greenish Image",image_greenish)
cv2.waitKey(0)
cv2.imshow("Blueish Image",image_blueish)
cv2.waitKey(0)