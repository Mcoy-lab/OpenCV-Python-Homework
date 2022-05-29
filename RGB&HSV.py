import cv2 as cv
import numpy as np


# 第一题
rgb_img = cv.imread('image/iris-RGB.tif', cv.COLOR_BGR2RGB)
b_img = cv.imread('image/iris-RGB.tif', cv.COLOR_BGR2RGB)
g_img = cv.imread('image/iris-RGB.tif', cv.COLOR_BGR2RGB)
r_img = cv.imread('image/iris-RGB.tif', cv.COLOR_BGR2RGB)
monkey = cv.imread('image/monkey.jpg')
cv.imshow("origin", rgb_img)
b_img[:, :, 0] = 0
g_img[:, :, 1] = 0
r_img[:, :, 2] = 0
cv.imshow("B=0", b_img)
cv.imshow("G=0", g_img)
cv.imshow("R=0", r_img)
cv.waitKey(0)
cv.destroyAllWindows()

# 第二题
b, g, r = monkey[:, :, 0], monkey[:, :, 1], monkey[:, :, 2]
x, y, z = monkey.shape
HSI_img = monkey
H_img = cv.imread('image/monkey.jpg')
S_img = cv.imread('image/monkey.jpg')
I_img = cv.imread('image/monkey.jpg')

for i in range(x):
    for j in range(y):

        B = b[i][j]
        G = g[i][j]
        R = r[i][j]
        mem = (int(R) - int(G) + int(R) - int(B)) / 2
        den = np.sqrt(pow((int(R) - int(G)), 2) + (int(R) - int(B)) * (int(G) - int(B)))

        if den == 0:
            theta = 0
            if B <= G:
                H = theta / (2 * np.pi)
            else:
                H = 360 - theta / (2 * np.pi)
        else:
            theta = np.arccos(mem / den)
            if B <= G:
                H = theta / (2 * np.pi)
            else:
                H = 360 - theta / (2 * np.pi)
        if (int(R) + int(G) + int(B)) == 0:
            S = 1
        else:
            MIN = 3 * min(R, G, B) / (int(R) + int(G) + int(B))
            S = 1 - MIN
        I = (int(R) + int(G) + int(B)) / 3
        H_img[i, j] = H
        S_img[i, j] = S
        I_img[i, j] = I

cv.imshow("H", H_img)
cv.imshow("S", S_img)
cv.imshow("I", I_img)
cv.waitKey(0)
cv.destroyAllWindows()

#  第三题
B1B = cv.imread('image/Band1-Blue-512.tif')
B2G = cv.imread('image/Band2-Green-512.tif')
B3R = cv.imread('image/Band3-Red-512.tif')
B4N = cv.imread('image/Band4-NearInfrared-512.tif')

temp1 = cv.imread('image/Band1-Blue-512.tif')
temp2 = cv.imread('image/Band1-Blue-512.tif')
x0, y0, z0 = temp1.shape

for i in range(x0):
    for j in range(y0):
        temp1[i, j, 0] = B1B[i, j, 0]
        temp1[i, j, 1] = B2G[i, j, 1]
        temp1[i, j, 2] = B3R[i, j, 2]
        temp2[i, j, 0] = B4N[i, j, -1]
        temp2[i, j, 1] = B2G[i, j, 1]
        temp2[i, j, 2] = B3R[i, j, 2]
cv.imshow("1&2&3", temp1)
cv.imshow("2&3&4", temp2)
cv.waitKey(0)
