import cv2
import numpy as np

lower_red = np.array([166,84,141])
upper_red = np.array([286,255,255])

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

ret, img = cam.read()

img = cv2.resize(img,(340,220))

imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

mask=cv2.inRange(imgHSV,lower_red,upper_red)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

cv2.imshow("maskClose",maskClose)
cv2.imshow("maskOpen",maskOpen)

k = cv2.waitKey(5) & 0xFF
if k == 27:
   break
cv2.destroyAllWindows()
cap.release
