import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read(1)



    frame = imutils.resize(frame, width=1024)
    lower_red = np.array([166,84,80])
    upper_red = np.array([286,255,255])

    colors = {'red':(255,0,0)}

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    kernel = np.ones((9,9),np.float32)/225
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        sc = str(center)
        # only proceed if the radius meets a minimum size. Correct this value for your obect's size
        if radius > 0.5:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (255,0,0), 2)
            cv2.putText(frame, sc, (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,255,0),2)
            print(center)


    cv2.imshow("frame", mask2)




    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release
