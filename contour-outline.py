import cv2 as cv
import numpy as np
#import imutils
cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv.imshow("screen",frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    cs,_ =cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for c in cs:
        cv.drawContours(frame,[c],-1,(0,255,0),3)
    cv.imshow("screen", frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()