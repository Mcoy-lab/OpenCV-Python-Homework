import cv2 as cv
import numpy as np


# 循环侵蚀
def erosion_loop(er_img, n, k=3):
    kernel = np.ones((k, k), np.uint8)
    temp = er_img
    for t in range(n):
        temp = cv.erode(temp, kernel, iterations=1)
    return temp


# 循环扩张
def dilation_loop(er_img, n, k=3):
    kernel = np.ones((k, k), np.uint8)
    temp = er_img
    for t in range(n):
        temp = cv.dilate(temp, kernel, iterations=1)
    return temp


# 循环闭运算
def closing_loop(er_img, n, k=3):
    kernel = np.ones((k, k), np.uint8)
    temp = er_img
    for t in range(n):
        temp = cv.morphologyEx(temp, cv.MORPH_CLOSE, kernel)
    return temp


# 循环开运算
def opening_loop(er_img, n, k=3):
    kernel = np.ones((k, k), np.uint8)
    temp = er_img
    for t in range(n):
        temp = cv.morphologyEx(temp, cv.MORPH_OPEN, kernel)
    return temp


text_break = cv.imread("image/text-broken.tif", 0)
letter = cv.imread("image/letterT.tif")
FPrint = cv.imread("image/fingerprint-noisy.tif", 0)
text_img = closing_loop(text_break, 10, 5)
print_img = opening_loop(FPrint, 3, 3)
print_img = closing_loop(print_img, 3, 3)
x, y, z = letter.shape
R = letter[:, :, 2]
for i in range(x - 1):
    for j in range(y - 1):
        if letter[i, j, 0] == letter[i, j + 1, 0] | letter[i, j, 0] == letter[i + 1, j, 0]:
            continue
        else:
            R[i, j] = 255

letter[:, :, 2] = R
cv.imshow("Text", text_img)
cv.imshow("print", print_img)
cv.imshow("letter", letter)
cv.waitKey(0)
