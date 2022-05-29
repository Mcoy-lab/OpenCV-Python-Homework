import numpy as np
import cv2 as cv

font = cv.FONT_HERSHEY_SIMPLEX
img = cv.imread('image/star.jpeg', 0)
ret, thresh = cv.threshold(img, 200, 255, 0)

contours, hierarchy = cv.findContours(thresh, 1, 2)
for i in contours:
    # cnt = contours[0]
    cnt = i
    M = cv.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    area = cv.contourArea(cnt)  # 轮廓区域
    perimeter = cv.arcLength(cnt, True)  # 轮廓周长
    Area = "Area " + str(area)  # 轮廓面积
    location = "Centroid Location (" + str(cx) + "," + str(cy) + ")"
    Perimeter = "Perimeter " + str(perimeter)

    epsilon = 0.1 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
    if area > 2900000:
        continue
    cv.circle(img, (cx, cy), 2, (0, 255, 0), 10)
    cv.putText(img, location, (cx+10, cy), font, 1, (0, 0, 0), 3, cv.LINE_AA)
    cv.putText(img, Perimeter, (cx+10, cy-50), font, 1, (0, 0, 0), 3, cv.LINE_AA)
    cv.putText(img, Area, (cx+10, cy-100), font, 1, (0, 0, 0), 3, cv.LINE_AA)
cv.imshow("info", img)
cv.waitKey(0)
