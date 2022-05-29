import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
while True:
    _, frame = cap.read()  # 读取帧
    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义HSV中白色的范围
    lower_wight = np.array([0, 30, 221])
    upper_wight = np.array([180, 221, 255])
    mask_wight = cv.inRange(hsv, lower_wight, upper_wight)
    res = cv.bitwise_and(frame, frame, mask=mask_wight)
    # closing = cv.morphologyEx(mask_wight, cv.MORPH_CLOSE, kernel)  # 闭运算
    # erosion = cv.erode(mask_wight, kernel, iterations=1)  # 侵蚀
    closing = cv.morphologyEx(mask_wight, cv.MORPH_CLOSE, kernel)  # 闭运算
    erosion = cv.erode(closing, kernel, iterations=1)  # 侵蚀
    # dilation = cv.dilate(erosion, kernel, iterations=1)  # 扩张
    erosion = cv.morphologyEx(erosion, cv.MORPH_CLOSE, kernel)  # 闭运算
    circles = cv.HoughCircles(erosion, cv.HOUGH_GRADIENT, 1, 150, param1=50, param2=30, minRadius=0, maxRadius=0)
    try:
        print(circles)
        circles = np.uint16(np.around(circles))
        c = 0
        for i in circles[0, :]:
            c = c + 1
        cv.putText(erosion, str(c), (200, 300), font, 4, (255, 255, 255), 2, cv.LINE_AA)
    except:
        cv.putText(erosion, "404 NOT FOUND", (200, 300), font, 4, (255, 255, 255), 2, cv.LINE_AA)
    # if circles == None:
    #     cv.putText(erosion, "404 NOT FOUND", (200, 300), font, 4, (255, 255, 255), 2, cv.LINE_AA)
    # else:
    #     circles = np.uint16(np.around(circles))
    #     c = 0
    #     for i in circles[0, :]:
    #         c = c + 1
    #     cv.putText(erosion, str(c), (200, 300), font, 4, (255, 255, 255), 2, cv.LINE_AA)

    # circles = np.uint16(np.around(circles))
    # c = 0
    # for i in circles[0, :]:
    #     c = c + 1
    # cv.putText(erosion, str(c), (200, 300), font, 4, (255, 255, 255), 2, cv.LINE_AA)

    # cv.putText(erosion, str(c), (200, 800), font, 4, (255, 255, 255), 2, cv.LINE_AA)
    # cv.imshow('frame', frame)
    cv.imshow('mask', erosion)
    # cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
# gray = cv.cvtColor(mask_wight, cv.COLOR_BGR2GRAY)
cv.imwrite("origin.jpg", erosion)

# circles = cv.HoughCircles(closing, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
# circles = np.uint16(np.around(circles))
# for i in circles[0, :]:
#     # 绘制外圆
#     cv.circle(closing, (i[0], i[1]), i[2], (0, 255, 0), 2)
#     # 绘制圆心
#     cv.circle(closing, (i[0], i[1]), 2, (0, 0, 255), 3)
# cv.imwrite('circles.jpg', closing)


# ret, thresh = cv.threshold(closing, 127, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(closing, contours, -1, (0, 255, 0), 3)
# cv2.imwrite("test.jpg",closing)