import cv2

'''--------------平滑滤波器--------------'''
dog_img = cv2.imread('image/dog.jpg', cv2.COLOR_BGR2GRAY)
blur_33 = cv2.blur(dog_img, ksize=(3, 3))
blur_99 = cv2.blur(dog_img, ksize=(9, 9))
cv2.imshow('Original Dog Image', dog_img)
cv2.imshow('size = 3*3', blur_33)
cv2.imshow('size = 9*9', blur_99)

'''--------------拉普拉斯算子--------------'''
moon_img = cv2.imread('image/blurry_moon.tif', cv2.COLOR_BGR2GRAY)
# 拉普拉斯
temp3_img = cv2.Laplacian(moon_img, cv2.CV_16S, ksize=3)
temp5_img = cv2.Laplacian(moon_img, cv2.CV_16S, ksize=5)
Lap3_img = cv2.convertScaleAbs(temp3_img)
Lap5_img = cv2.convertScaleAbs(temp5_img)
cv2.imshow('size=3', Lap3_img)
cv2.imshow('size=5', Lap5_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
