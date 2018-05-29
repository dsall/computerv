import cv2
import numpy as np
import imutils
from time import sleep

cap = cv2.VideoCapture(1)
cap1 = cv2.VideoCapture(1)
ret, frame1 = cap.read()
frame1 = imutils.resize(frame1, width=600)
class find:
    def detect_object(self, v, w,a,b,c,d,e,f,z):
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
        xc = 0
        yc = 0

        if len(red_center) > 0 :
            c = max(red_center, key=cv2.contourArea)
            #((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)

            xc = int(M["m10"] / M["m00"])
            yc = int(M["m01"] / M["m00"])

        self.color = z
        self.xcoord = xc
        self.ycoord = yc
        cv2.imshow("Frame", mask1)
    def getcoordx(self):
        return self.xcoord
    def getcoordy(self):
        return self.ycoord
    def getcolor(self):
        return self.color
    def getOuput(self):
        return self.maskoutput

def detect_w_avg(s,w,a,b,c,d,e,f,color):
    i = 0
    xred = 0
    yred = 0
    x = 0
    y = 0
    red = find()
    red.detect_object(s, w,a,b,c,d,e,f,color)
    while i < 10:
        x_now = red.getcoordx()
        y_now = red.getcoordy()
        if(x_now!=0 and y_now!=0):
            xred = xred + x_now
            yred = yred + y_now
            i += 1
        else:
            red = find()
            red.detect_object(s, w,a,b,c,d,e,f,color)
            i=0
    return (color,(xred/i), (yred/i))

i = 1


    #color, x,y = detect_w_avg(cap, 600,0,100,100,189,255,255,"red")





while True:
    color1, x1,y1 = detect_w_avg(cap, 600,65,60,60,80,255,255,"green")
    #color, x,y = detect_w_avg(cap, 600,0,50,50,180,255,255,"brightred")
    #print (color, x,y )
    print (color1, x1,y1 )


    #cv2.line(frame1,(int(x),int(y)),(int(x1),int(y1)),(255,0,0),1)
    cv2.imshow("Output", frame1)
    #else:
        #print("No object detected")
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    i += 1

cv2.destroyAllWindows()
cap.release
