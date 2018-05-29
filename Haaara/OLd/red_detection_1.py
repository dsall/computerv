import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read(1)
    #frame = imutils.resize(frame, width=1024)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([166,84,141])
    upper_red = np.array([286,255,255])


    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    kernel = np.ones((15,15),np.float32)/225
    #smoothed = cv2.filter2D(res,-1,kernel)
    blur = cv2.GaussianBlur(res,(15,15),0)
    #median = cv2.medianBlur(res,15)
    #bilateral = cv2.bilateralFilter(res,15,75,75)


    #cv2.imshow('bilateral Blur',bilateral)
    #cv2.imshow('Median Blur',median)
    cv2.imshow('Gaussian Blurring',res)
    cv2.imshow('Original',frame)
    #cv2.imshow('Averaging',smoothed)

    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    #cv2.imshow('res', res)
    #cv2.imshow('smoothed', smoothed)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release
