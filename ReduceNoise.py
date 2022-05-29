import numpy as np
import cv2
import cv2 as cv
from matplotlib import pyplot as plt


PCB_img = cv.imread('image/gaussian.tif')
auto_img = cv.imread('image/automedian.png')
blur_GS = cv.GaussianBlur(PCB_img, (9, 9), 1)
cv.imshow("Gaussian", blur_GS)
cv.waitKey(0)


img_H = cv2.imread("image/hujiao.png", 0)
img_S = cv2.imread("image/salt.png", 0)
img_h = img_H.shape[0]
img_w = img_H.shape[1]


m, n = 3, 3
order = m * n
kernalMean = np.ones((m, n), np.float32)  # 生成盒式核
hPad = int((m - 1) / 2)
wPad = int((n - 1) / 2)
imgPad_H = np.pad(img_H.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge")
imgPad_S = np.pad(img_S.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), mode="edge")
QH = 1.1  # 反谐波平均滤波器 阶数
QS = -1.1
epsilon = 1e-8
imgH = img_H.copy()
imgS = img_S.copy()
for i in range(hPad, img_h + hPad):
    for j in range(wPad, img_w + wPad):
        # 反谐波平均滤波器 (contraharmonic mean filter)
        temp = imgPad_H[i - hPad:i + hPad + 1, j - wPad:j + wPad + 1] + epsilon
        imgH[i - hPad][j - wPad] = np.sum(np.power(temp, (QH + 1))) / np.sum(np.power(temp, QH) + epsilon)
        imgS[i - hPad][j - wPad] = np.sum(np.power(temp, (QS + 1))) / np.sum(np.power(temp, QS) + epsilon)


plt.figure(figsize=(9, 6))
plt.subplot(121), plt.axis('off'), plt.title("hujiao")
plt.imshow(imgH, cmap='gray', vmin=0, vmax=255)
plt.subplot(122), plt.axis('off'), plt.title("salt")
plt.imshow(imgS, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
