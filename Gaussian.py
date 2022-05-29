import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def gaussian_filter(img, D0, N=2):
    '''
        D0: 截止频率
        N: butterworth和指数滤波器的阶数
    '''

    # 离散傅里叶变换
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
    # 中心化
    dtf_shift = np.fft.fftshift(dft)
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)  # 计算频谱中心
    mask = np.ones((rows, cols, 2))  # 生成rows行cols列的2纬矩阵
    for i in range(rows):
        for j in range(cols):
            D = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            mask[i, j] = np.exp(-(D0 ** 2 / (D+1) ** 2))
    fshift = dtf_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])  # 计算像素梯度的绝对值
    img_back = np.abs(img_back)
    img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
    return img_back


img = cv.imread('image/sign_a.png', 0)
plt.subplot(141), plt.imshow(img, cmap='gray'), plt.title('origin image')
img_back = gaussian_filter(img, 30)
plt.subplot(142), plt.imshow(img_back, cmap='gray'), plt.title('D0=30')
img_back1 = gaussian_filter(img, 60)
plt.subplot(143), plt.imshow(img_back1, cmap='gray'), plt.title('D0=60')
img_back2 = gaussian_filter(img, 150)
plt.subplot(144), plt.imshow(img_back2, cmap='gray'), plt.title('D0=150')
plt.show()
