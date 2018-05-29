#import required libraries
#import OpenCV library
import cv2
import numpy as np
import os
import time

Color = (255,0,0)
image = cv2.imread('jibby.jpg')
def detect_face(photo, color, thickness, cascade_file):
    face_cascade = cv2.CascadeClassifier(cascade_file)
    face = face_cascade.detectMultiScale(photo, scaleFactor=1.2, minNeighbors = 5);
    for (x, y, w, h) in face:
        cv2.rectangle(photo, (x, y), (x+w, y+h), color, thickness)
    print('Faces Found: ', len(face))


detect_face(image, Color, 2, 'lb_front.xml')

cv2.imshow("photo",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
