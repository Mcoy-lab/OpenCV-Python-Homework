import cv2 as cv
from matplotlib import pyplot as plt

font = cv.FONT_HERSHEY_SIMPLEX
img = cv.imread('image/expression.png')
median_img = cv.imread('image/median_img.png')
bilateral_img = cv.imread('image/bilateral_img.png')
blur_aver = cv.blur(img, (5, 5))  # 图像平滑
blur_GS = cv.GaussianBlur(img, (9, 9), 0)  # 高斯模糊
blur_median = cv.medianBlur(img, 5)  # 中位模糊
blur_bilateral = cv.bilateralFilter(img, 9, 75, 75)  # 双边滤波

plt.xticks([]), plt.yticks([])
plt.subplot(151), plt.imshow(img), plt.title('Original')
plt.subplot(152), plt.imshow(blur_GS), plt.title('GS')
plt.subplot(153), plt.imshow(blur_median), plt.title('median')
plt.subplot(154), plt.imshow(blur_bilateral), plt.title('bilateral')
plt.subplot(155), plt.imshow(blur_aver), plt.title('smooth')
plt.show()
cv.putText(img, 'ZYF14', (0, 25), font, 0.5, (0, 0, 0), 2, cv.LINE_AA)
cv.putText(blur_GS, 'ZYF14', (0, 25), font, 0.5, (0, 0, 0), 2, cv.LINE_AA)
cv.putText(blur_median, 'ZYF14', (0, 25), font, 0.5, (0, 0, 0), 2, cv.LINE_AA)
cv.putText(blur_bilateral, 'ZYF14', (0, 25), font, 0.5, (0, 0, 0), 2, cv.LINE_AA)
cv.putText(blur_aver, 'ZYF14', (0, 25), font, 0.5, (0, 0, 0), 2, cv.LINE_AA)

plt.imsave('filter_GS.jpg', blur_GS)
plt.imsave('filter_median.jpg', blur_median)
plt.imsave('filter_bilateral.jpg', blur_bilateral)
plt.imsave('filter_aver.jpg', blur_aver)

