import numpy as np
import matplotlib.pyplot as plt
import cv2
image = cv2.imread('DIP\little.jpg')
reference_image = cv2.imread('DIP\little2.jpg')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
refer_img = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)


m_img,n_img = img.shape
m_refer_img,n_refer_img = refer_img.shape
print(m_img,n_img)
print(m_refer_img,n_refer_img)

unique_array_img = np.unique(img)
unique_array_refer_img = np.unique(refer_img)

count_array_img = np.zeros(len(unique_array_img),int)
count_array_refer_img = np.zeros(len(unique_array_refer_img),int)

cdf_array_img = np.zeros(len(unique_array_img),int)
cdf_array_refer_img = np.zeros(len(unique_array_refer_img),int)

for i in range(0,len(unique_array_img)):
    count_array_img[i] = np.count_nonzero(img == unique_array_img[i])

for i in range(0,len(unique_array_refer_img)):
    count_array_refer_img[i] = np.count_nonzero(refer_img == unique_array_refer_img[i])

cdf_array_img[0] = count_array_img[0]

for i in range(1,len(unique_array_img)):
    cdf_array_img[i] = cdf_array_img[i-1] + count_array_img[i]

cdf_array_refer_img[0] = count_array_refer_img[0]

for i in range(1,len(unique_array_refer_img)):
    cdf_array_refer_img[i] = cdf_array_refer_img[i-1] + count_array_refer_img[i]

for i in range(m_img):
    for j in range(n_img):
        index = np.where(unique_array_img == img[i][j])
        for k in range(0,len(cdf_array_refer_img)):
            if(cdf_array_img[index] == cdf_array_refer_img[k]):
                img[i][j] = unique_array_refer_img[k]
            else:
                continue

cv2.imshow("original Image",image)
cv2.waitKey(0)
cv2.imshow('reference Image',reference_image)
cv2.waitKey(0)
cv2.imshow("Original image's  Gray Scale image",gray_img)
cv2.waitKey(0)
cv2.imshow("Reference Image's Gray Scale Image",refer_img)    
cv2.waitKey(0)
cv2.imshow('Histogram Matched Image',img)                       
cv2.waitKey(0)
cv2.destroyAllWindows()