import cv2 as cv
import numpy as np
from matplotlib import pyplot as pyplot
def cal_lines(img,lines):
    img = np.copy(img)
    newimage = np.zeros_like(img)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(newimage,(x1,y1),(x2,y2),(200,200,200),10)
        img = cv.addWeighted(img,1.0,newimage,1.0,0.0)
        return img
cap = cv.VideoCapture('lane.mp4')
while(1):

    ret,frame = cap.read()
    #blur = cv.GaussianBlur(frame,(3,3),0)
    #cv.imshow('blur',blur)
    mask = cv.inRange(frame,(110,110,110),(120,190,180))
    res = cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('res',res)
    gray = cv.cvtColor(res,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    ret,thresh = cv.threshold(gray,110,255,cv.THRESH_BINARY)
    cv.imshow('thresh',thresh)
    canny = cv.Canny(thresh,100,200)
    cv.imshow('canny',canny)
    crop = cv.rectangle(canny,(0,0),(640,163),(0,0,0),-1)
    cv.imshow('crop',crop)
    lines = cv.HoughLinesP(crop,10,np.pi/90,100,150,minLineLength=120,maxLineGap=50)
    bl = cal_lines(frame,lines)
    cv.imshow('img',bl)
    if cv.waitKey(10)==ord('q'):
        break
cv.destroyAllWindows()
