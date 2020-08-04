import cv2
import numpy

im=cv2.imread("pop.jpg",1)
img=cv2.resize(im,(600,450))
cv2.imshow("screen",img)

def click(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        blackimg=numpy.zeros((512,512,3),numpy.uint8)
        blackimg[:]=[blue,green,red]
        cv2.imshow("color",blackimg)

cv2.setMouseCallback("screen",click)
cv2.waitKey(0)
cv2.destroyAllWindows()
