import cv2 as cv
import numpy as np


# 循环侵蚀
def erosion_loop(er_img, n):
    temp1 = er_img
    for t in range(n):
        temp1 = cv.erode(temp1, kernel, iterations=1)
    return temp1


# 循环扩张
def dilation_loop(er_img, n):
    temp2 = er_img
    for t in range(n):
        temp2 = cv.dilate(temp2, kernel, iterations=1)
    return temp2


img = cv.imread('image/Highway.png', cv.COLOR_BGR2GRAY)
cropped = img[120:400, 170:550]
kernel = np.ones((5, 5), np.uint8)
lower_wight = np.array([0, 0, 235])
upper_wight = np.array([180, 221, 255])
hsv = cv.cvtColor(cropped, cv.COLOR_BGR2HSV)
mask_wight = cv.inRange(hsv, lower_wight, upper_wight)
erosion = erosion_loop(mask_wight, 1)
# dilation = dilation_loop(erosion, 16)
circles = cv.HoughCircles(mask_wight, cv.HOUGH_GRADIENT, 4, 150, param1=50, param2=50, minRadius=0, maxRadius=0)
temp = len(circles[0])

try:
    while temp > 1:
        erosion = cv.erode(erosion, kernel, iterations=1)
        circles = cv.HoughCircles(erosion, cv.HOUGH_GRADIENT, 4, 150, param1=50, param2=60, minRadius=0, maxRadius=0)
        temp = len(circles[0])

    circles = np.uint16(np.around(circles))
    dilation = dilation_loop(erosion, 16)
except Exception as err:
    dilation = erosion
    print("未找到,ERROR:" + str(err))
    cv.waitKey(0)
    exit(0)

length = circles[0][0][2]
x = circles[0][0][0]
y = circles[0][0][1]
left_angle_x = x - length+170
left_angle_y = y - length+120
right_angle_x = x + length+170
right_angle_y = y + length+120
cv.rectangle(img, (left_angle_x, left_angle_y), (right_angle_x, right_angle_y), (0, 0, 0), 4)
cv.imshow("process", dilation)
cv.imshow("consequence", img)
cv.imwrite("image/Final_process.png", erosion)
cv.imwrite("image/Final_consequence.png", img)
cv.waitKey(0)
