import cv2 as cv
import numpy as np

img = cv.imread('image/j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)  # 侵蚀
# cv.imshow("扩张", erosion)
dilation = cv.dilate(img, kernel, iterations=1)  # 扩张
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开运算
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # 闭运算
cv.imshow("侵蚀", erosion)
cv.imshow("扩张", dilation)
cv.imshow("开运算", opening)
cv.imshow("闭运算", closing)

cv.waitKey(0)
