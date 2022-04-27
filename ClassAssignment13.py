import cv2
image = cv2.imread("DIP\dhoni.jpg")
img = cv2.imread("DIP\dhoni.jpg")
WaterMark = cv2.imread("DIP\little.jpg")

m_img,n_img,v = img.shape
m_WaterMark,n_WaterMark,v1 = WaterMark.shape

center_y = int(m_img/2)
center_x = int(n_img/2)

top_y = center_y - int(m_WaterMark/2)
bottom_y = top_y + m_WaterMark
left_x = center_x - int(n_WaterMark/2)
right_x = left_x + n_WaterMark

destination = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(destination,0.1,WaterMark,0.5,0)
img[top_y:bottom_y, left_x:right_x] = result

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()