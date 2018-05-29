import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read(0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)



    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
   corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow('Corner',img)
