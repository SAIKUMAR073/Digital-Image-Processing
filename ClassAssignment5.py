#Assignment5:
#Task-->Read a color image,convert the color image to gray scale and performe histogram equalization by algorithm discussed in class.
#also check with direct function avaialable.
#note: to get the histogram results of wikipedia site that dissussed in class, uncomment the commented part and comment the part that is mentioned to comment,
# you cant able to visualize image of wikipedia site becacause it is small but you can see the graph.
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('D:\pythonfiles\DIP\dhoni.jpg')  #comment this for wikipedia results
m,n,v= np.shape(image)                              #comment this for wikipedia results

#grayscaleimage = np.array([[52,55,61,59,79,61,76,61],
#[62,59,55,104,94,85,59,71],
#[63,65,66,113,144,104,63,72],
#[64,70,70,126,154,109,71,69],
#[67,73,68,106,122,88,68,68],
#[68,79,60,70,77,66,58,75],
#[69,85,64,58,55,61,65,83],
#[70,87,69,68,65,73,78,90]],dtype=np.uint8)
#m,n = np.shape(grayscaleimage)
#grayscaleimage_1 = np.array([[52,55,61,59,79,61,76,61],
#[62,59,55,104,94,85,59,71],
#[63,65,66,113,144,104,63,72],
#[64,70,70,126,154,109,71,69],
#[67,73,68,106,122,88,68,68],
#[68,79,60,70,77,66,58,75],
#[69,85,64,58,55,61,65,83],
#[70,87,69,68,65,73,78,90]],dtype=np.uint8)

grayscaleimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)            #comment this for wikipedia results
grayscaleimage_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          #comment this for wikipedia results
unique_array = np.unique(grayscaleimage)
count_array = np.zeros(len(unique_array),int)
cdf_array = np.zeros(len(unique_array),int)
hv_array = np.zeros(len(unique_array),int)

for i in range(0,len(unique_array)):
    count_array[i] = np.count_nonzero(grayscaleimage == unique_array[i])

cdf_array[0] = count_array[0]

for i in range(1,len(unique_array)):
    cdf_array[i] = cdf_array[i-1] + count_array[i]

cdf_min = min(cdf_array)

for i in range(0,len(unique_array)):
    hv_array[i] = round(((cdf_array[i] - cdf_min)*255)/((m*n) - cdf_min))

for i in range(0,len(unique_array)):
    for j in range(m):
        for k in range(n):
            if(grayscaleimage_1[j][k] == unique_array[i]):
                grayscaleimage_1[j][k] = hv_array[i]
            else:
                continue

print("m x n x v  = %d x %d x %d"%(m,n,v))            #comment this for wikipedia results
#print("m x n = %d x %d"%(m,n))

print("grayscaleimage =")
print(grayscaleimage)
print("unique_array =")
print(unique_array)
print("count_array =")
print(count_array)
print("cdf_array =")
print(cdf_array)
print("cdf_min = %d"%(cdf_min))
print("hv_array =")
print(hv_array)
print("grayscaleimage_1 =")
print(grayscaleimage_1)

cv2.imshow('Image before histogram equalization',grayscaleimage)
cv2.waitKey(0)
cv2.imshow('Image after histogram equalization with algorithm discussed in class',grayscaleimage_1)
cv2.waitKey(0)
cv2.imshow('Image after histogram equalization with direct function',cv2.equalizeHist(grayscaleimage))
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.subplot(3,1,1)
plt.hist(grayscaleimage.ravel(),256,[0,256])
plt.subplot(3,1,2)
plt.hist(grayscaleimage_1.ravel(),256,[0,256])
plt.subplot(3,1,3)
plt.hist(cv2.equalizeHist(grayscaleimage).ravel(),256,[0,256])
plt.show()

#note:Enter space or any key on keyboard after display of first image to see other images....
