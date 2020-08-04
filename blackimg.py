import numpy
import cv2
#img=numpy.zeros([400,400,3],numpy.uint8)
img=cv2.imread("pop.jpg",1)

img=cv2.line(img,(100,100),(200,200),(50,50,50),5)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
"""        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(x)+" "+str(y)
        cv2.putText(img,text,font,1,(100,100,100),5)
"""
cv2.imshow("screen",img)
cv2.setMouseCallback("screen",click)

cv2.imshow("screen",img)
cv2.waitKey(0)