import cv2

#im=cv2.imread("pop.jpg",1)
#img=cv2.resize(im,(600,450))
#print(img)
#cv2.imshow("screen",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    cv2.imshow("screen",frame)
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()