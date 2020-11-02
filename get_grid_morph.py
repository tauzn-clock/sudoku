#https://stackoverflow.com/questions/10196198/how-to-remove-convexity-defects-in-a-sudoku-square
from skimage.segmentation import clear_border
import imutils
import cv2
import numpy as np
import tensorflow as tf
from approx_square import square
from get_puzzle import puzzle

def kernel(x,y):
    return np.ones((x,y),np.uint8)

PATH="original/sudo1.png"
IMG=square(PATH)
RAW_INFO=puzzle(IMG)


processed = cv2.morphologyEx(RAW_INFO[1], cv2.MORPH_CLOSE, kernel(5,5))

#I still dont quite understand how this work
#This is a method to get the gradient of the image along two axis
#X=cv2.GaussianBlur(processed,(7,0),sigmaX=10,sigmaY=10)
X=cv2.Sobel(processed,cv2.CV_16S,1,0)

#Since gradient can be negative, this two lines conver the image into black and white image
X=cv2.convertScaleAbs(X)
cv2.normalize(X,X,0,255,cv2.NORM_MINMAX)

#Sharpens the imag??
kernelx = cv2.getStructuringElement(cv2.MORPH_RECT,(2,10))
ret,X = cv2.threshold(X,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
X = cv2.morphologyEx(X,cv2.MORPH_DILATE,kernelx,iterations = 1)

#Draw a box over the long lines and then extract them
contour, hier = cv2.findContours(X,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contour:
    x,y,w,h = cv2.boundingRect(cnt)
    if h/w > 5: #Assume lines are long
        cv2.drawContours(X,[cnt],0,255,-1)
    else:
        cv2.drawContours(X,[cnt],0,0,-1)
X = cv2.morphologyEx(X,cv2.MORPH_CLOSE,None,iterations = 1)
cv2.imshow("X",X)



#I still dont quite understand how this work
#This is a method to get the gradient of the image along two axis
#Y=cv2.GaussianBlur(processed,(0,7),sigmaX=10,sigmaY=10)
Y=cv2.Sobel(processed,cv2.CV_16S,0,1)

#Since gradient can be negative, this two lines conver the image into black and white image
Y=cv2.convertScaleAbs(Y)
cv2.normalize(Y,Y,0,255,cv2.NORM_MINMAX)

#Sharpens the imag??
kernely = cv2.getStructuringElement(cv2.MORPH_RECT,(10,2))
ret,Y = cv2.threshold(Y,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
Y = cv2.morphologyEx(Y,cv2.MORPH_DILATE,kernely,iterations = 1)

#Draw a box over the long lines and then extract them
contour, hier = cv2.findContours(Y,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contour:
    x,y,w,h = cv2.boundingRect(cnt)
    if w/h>5: #Assume lines are long
        cv2.drawContours(Y,[cnt],0,255,-1)
    else:
        cv2.drawContours(Y,[cnt],0,0,-1)

Y = cv2.morphologyEx(Y,cv2.MORPH_CLOSE,None,iterations = 1)
cv2.imshow("Y",Y)

tog=cv2.bitwise_and(X,Y)
cv2.imshow("tog",tog)
