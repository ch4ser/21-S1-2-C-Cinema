import cv2 as cv
import numpy as np

def extrace_object_demo():
    str = input("dir：")
    capture=cv.VideoCapture(str)
    while(True):
        ret, frame=capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv=np.array([37,43,46])
        upper_hsv=np.array([77,255,255])
        mask=cv.inRange(hsv,lower_hsv,upper_hsv)
        dst=cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)
        cv.imshow("dst",dst)
        c=cv.waitKey(40)
        if c==27:
            break

extrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()