import cv2 as cv
import numpy as np

# Red = numpy.uint8([[[255, 0, 0]]])
# Green = numpy.uint8([[[0, 255, 0]]])
# Blue = numpy.uint8([[[0, 0, 255]]])
# hsv_Red = cv.cvtColor(Red, cv.COLOR_BGR2HSV)
# hsv_Green = cv.cvtColor(Green, cv.COLOR_BGR2HSV)
# hsv_Blue = cv.cvtColor(Blue, cv.COLOR_BGR2HSV)
# mod = input('please input mixed module:\n')
# font = cv.FONT_HERSHEY_SIMPLEX
cap = cv.VideoCapture(0)
while True:
    _, frame = cap.read()  # 读取帧
    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义HSV中蓝色的范围
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    # 设置HSV的阈值使得只取蓝色
    # 定义HSV中绿色的范围
    lower_green = np.array([40, 43, 46])
    upper_green = np.array([90, 255, 255])
    # 设置HSV的阈值使得只取绿色
    # 定义HSV中红色的范围
    lower_red = np.array([0, 43, 36])
    upper_red = np.array([10, 255, 255])
    # 设置HSV的阈值使得只取红色

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)  # 将掩膜和蓝像素图像逐像素相加
    mask_red = cv.inRange(hsv, lower_red, upper_red)  # 将掩膜和红像素图像逐像素相加
    mask_green = cv.inRange(hsv, lower_green, upper_green)  # 将掩膜和绿像素图像逐像素相加
    # if mod == 'R':
    #     res = cv.bitwise_and(frame, frame, mask=mask_red)
    #     mask = mask_red
    # elif mod == 'G':
    #     res = cv.bitwise_and(frame, frame, mask=mask_green)
    #     mask = mask_green
    # elif mod == 'B':
    #     res = cv.bitwise_and(frame, frame, mask=mask_blue)
    #     mask = mask_blue
    # else:
    RB = cv.addWeighted(mask_blue, 0.5, mask_red, 0.5, 0)
    mask = cv.addWeighted(RB, 0.5, mask_green, 0.5, 0)
    res = cv.bitwise_and(frame, frame, mask=mask)
    # res = cv.bitwise_and(frame, frame, mask=mask_green)
    # mask = mask_green
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    # cv.putText(res, 'ZYF110309014', (200, 800), font, 4, (0, 255, 255), 2, cv.LINE_AA)
    # cv.putText(mask, 'ZYF110309014', (200, 800), font, 4, (0, 255, 255), 2, cv.LINE_AA)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
cv.imwrite('image/res.jpg', res)
cv.imwrite('image/mask.jpg', mask)
