import numpy as np
import cv2
from matplotlib import pyplot as plt

auto_img = cv2.imread("image/automedian.png", 0)  # flags=0 读取为灰度图像
auto_hImg = auto_img.shape[0]
auto_wImg = auto_img.shape[1]
am, an = 5, 5
# 边缘填充
auto_hPad = int((am - 1) / 2)
auto_wPad = int((an - 1) / 2)
auto_imgPad = np.pad(auto_img.copy(), ((auto_hPad, am - auto_hPad - 1), (auto_wPad, an - auto_wPad - 1)), mode="edge")

# 估计原始图像的噪声方差 sigmaEta
mean, stddev = cv2.meanStdDev(auto_img)
sigmaEta = stddev ** 2

# 自适应局部降噪
imgAdaLocal = np.zeros(auto_img.shape)
for i in range(auto_hImg):
    for j in range(auto_wImg):
        pad = auto_imgPad[i:i + am, j:j + an]  # 邻域 Sxy, m*n
        gxy = auto_img[i, j]  # 含噪声图像的像素点
        zSxy = np.mean(pad)  # 局部平均灰度
        sigmaSxy = np.var(pad)  # 灰度的局部方差
        rateSigma = min(sigmaEta / (sigmaSxy + epsilon), 1.0)  # 加性噪声假设：sigmaEta/sigmaSxy < 1
        imgAdaLocal[i, j] = gxy - rateSigma * (gxy - zSxy)

plt.figure(figsize=(9, 6))
plt.subplot(131), plt.axis('off'), plt.title("Original")
plt.imshow(auto_img, cmap='gray', vmin=0, vmax=255)
plt.subplot(122), plt.axis('off'), plt.title("Adaptive local filter")
plt.imshow(imgAdaLocal, cmap='gray', vmin=0, vmax=255)
plt.tight_layout()
plt.show()
