import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

gamma_img = cv.imread('image/gamma.png', 0)
fi = gamma_img / 255.0
# 伽马变换
gamma3 = 3
gamma10 = 10
out3 = np.power(fi, gamma3)
out10 = np.power(fi, gamma10)
cv.imshow("gamma10", out10)
cv.imshow("gamma3", out3)
cv.waitKey()


# 计算灰度直方图
def calcGrayHist(in_value):
    h, w = in_value.shape[:2]
    gray_hist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            gray_hist[in_value[i][j]] += 1
    return gray_hist


girl_img = cv.imread('image/girl.png', 0)
grayHist = calcGrayHist(girl_img)
x = np.arange(256)
# 绘制灰度直方图
plt.plot(x, grayHist, linewidth=2, c='black')
plt.xlabel("gray Label")
plt.ylabel("number of pixels")
plt.show()
# 输出均衡化图像
equal = cv.equalizeHist(girl_img)
cv.imshow("equal", equal)
cv.waitKey()
