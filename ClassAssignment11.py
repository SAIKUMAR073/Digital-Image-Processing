##############------------Histogram Strecthing--------------------#############

import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('DIP\dhoni.jpg',0)

m,n = image.shape
print(m,n)

Strechted_image = np.zeros((m,n),np.uint8)

f_max = np.max(image)
f_min = np.min(image)
for i in range(m):
    for j in range(n):
        Strechted_image[i][j] = round((((image[i][j] - f_min)/(f_max - f_min))*255))
plt.subplot(2,1,1)
plt.hist(image.ravel(),256,[0,256])
plt.subplot(2,1,2)
plt.hist(Strechted_image.ravel(),256,[0,256])

plt.show()
cv2.imshow("Original Gray Scaled Image",image)
cv2.waitKey(0)
cv2.imshow("Histogram strechted Image",Strechted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

