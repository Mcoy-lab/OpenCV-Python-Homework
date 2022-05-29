import cv2
import numpy

'''第一题'''
fish_img = cv2.imread('image/fish.png')
girl_img = cv2.imread('image/girl.png')
print("height = " + str(fish_img.shape[0]) + ",width = " + str(fish_img.shape[1]))

'''第二题'''
width = girl_img.shape[1]
height = girl_img.shape[0]
girl_img1 = cv2.resize(girl_img, (width * 2, height * 2), cv2.INTER_NEAREST)
girl_img2 = cv2.resize(girl_img, (width * 2, height * 2), cv2.INTER_LINEAR)
girl_img3 = cv2.resize(girl_img, (width * 2, height * 2), cv2.INTER_CUBIC)
cv2.imshow("NN", girl_img1)
cv2.imshow("Bilinear", girl_img2)
cv2.imshow("Bicubic", girl_img3)
cv2.waitKey(0)

'''第三题'''
str_img = cv2.imread('image/string.jpg')
gray = cv2.cvtColor(str_img, cv2.COLOR_RGB2GRAY)
ret, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
colorful_img = numpy.zeros((str_img.shape[0], str_img.shape[1], 3), numpy.uint8)
for i in range(1, num_labels):
    mask = labels == i
    colorful_img[:, :, 0][mask] = numpy.random.randint(0, 255)
    colorful_img[:, :, 1][mask] = numpy.random.randint(0, 255)
    colorful_img[:, :, 2][mask] = numpy.random.randint(0, 255)

cv2.imshow('colorful', colorful_img)
cv2.waitKey(0)
