import cv2
import numpy as np
import imutils
from time import sleep

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)


def detect_object(v, w,a,b,c,d,e,f,z):
    _, frame = v.read(c)
    frame = imutils.resize(frame, width=w)
    lower_color = np.array([a,b,c])
    upper_color = np.array([d,e,f])
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    kernel = np.ones((11,11),np.float32)/225
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask1 = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    kernel = np.ones((11,11),np.float32)/225
    
    red_center = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center_red = None
    

    if len(red_center) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(red_center, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        x_red = int(M["m10"] / M["m00"])
        y_red = int(M["m01"] / M["m00"])

       # sc = str("x-red:",x_red, "y_red:",y_red)
        # only proceed if the radius meets a minimum size. Correct this value for your obect's size
        if radius > 0.5:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (255,0,0), 2)
            #cv2.putText(frame, sc, (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,0),2)
            print(z, x_red, y_red)
          
    return mask1
    
while True:
    cv2.imshow("red", detect_object(cap, 600,166,84,80,286,255,255,"red"))
    cv2.imshow("blue",detect_object(cap1, 600,97, 100, 117,117,255,255,"blue"))

    




    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release



#    _, frame = cap.read(0)
#    _, frame1 = cap1.read(1)
#    
#
#
#
#    frame = imutils.resize(frame, width=600)
#    frame1 = imutils.resize(frame1, width=600)
#    lower_red = np.array([166,84,80])
#    upper_red = np.array([286,255,255])
#    
#    lower_blue = np.array([97, 100, 117])
#    upper_blue = np.array([117,255,255])
#
#   # colors = {'red':(255,0,0)}
#
#    blurred_red = cv2.GaussianBlur(frame, (11, 11), 0)
#    blurred_blue = cv2.GaussianBlur(frame1, (11, 11), 0)
#    
#    hsv_red = cv2.cvtColor(blurred_red, cv2.COLOR_BGR2HSV)
#    hsv_blue = cv2.cvtColor(blurred_blue, cv2.COLOR_BGR2HSV)
#
#    kernel = np.ones((11,11),np.float32)/225
#    
#    #mask = cv2.inRange(hsv_red, lower_red, upper_red)
#    mask_red = cv2.inRange(hsv_red, lower_red, upper_red)
#    mask_red1 = cv2.inRange(hsv_red, lower_red, upper_red)
#    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
#    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)
#    
#   
#    
#    mask_blue = cv2.inRange(hsv_blue, lower_blue, upper_red)
#    mask_blue1 = cv2.inRange(hsv_blue, lower_blue, upper_red)
#    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
#    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
#    
#    kernel = np.ones((11,11),np.float32)/225
#
#    red_center = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL,
#        cv2.CHAIN_APPROX_SIMPLE)[-2]
#    center_red = None
#    
#    blue_center = cv2.findContours(mask_blue.copy(), cv2.RETR_EXTERNAL,
#        cv2.CHAIN_APPROX_SIMPLE)[-2]
#    center_blue = None
#
#    if len(red_center) > 0:
#        # find the largest contour in the mask, then use
#        # it to compute the minimum enclosing circle and
#        # centroid
#        c = max(red_center, key=cv2.contourArea)
#        ((x, y), radius) = cv2.minEnclosingCircle(c)
#        M = cv2.moments(c)
#        center_red = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
#
#        sc = str(center_red)
#        # only proceed if the radius meets a minimum size. Correct this value for your obect's size
#        if radius > 0.5:
#            # draw the circle and centroid on the frame,
#            # then update the list of tracked points
#            cv2.circle(frame, (int(x), int(y)), int(radius), (255,0,0), 2)
#            cv2.putText(frame, sc, (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,0),2)
#            print(center_red)
#    
#
