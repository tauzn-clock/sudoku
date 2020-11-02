#Gets the corners of the 
import cv2
from imutils.perspective import four_point_transform
import numpy as np


def square(PATH):
    image_corners=[]

    #Get Coordinates
    def clicks(event,x,y,flags,param):
        if (event==cv2.EVENT_LBUTTONDOWN):
            image_corners.append((x,y))
            print(x,y)

    #Load Image
    IMG=cv2.imread(PATH)
    #_,IMG=cv2.threshold(IMG,100,255,cv2.THRESH_BINARY)
    cv2.namedWindow("ORIGINAL_IMAGE")
    cv2.setMouseCallback("ORIGINAL_IMAGE",clicks)
    cv2.imshow("ORIGINAL_IMAGE",IMG)

    while True:
        key=cv2.waitKey(1) &0xFF
        if (key==ord(" ")):
            if len(image_corners)==4:
                cv2.destroyAllWindows()
                break
            else:
                print("Need to select 4 points")
                image_corners=[]

    sq=four_point_transform(IMG,np.array(image_corners).reshape(4,2))

    #cv2.imshow("CROP_IMAGE",sq)
    return sq
