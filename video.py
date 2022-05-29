import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("error")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame (stream end?). Exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break
cv.imwrite('image/img.png', gray)
cap.release()
cv.destroyAllWindows()
