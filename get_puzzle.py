import cv2
import imutils
from imutils.perspective import four_point_transform

def puzzle(ORI):
    #Process Image
    IMG=cv2.cvtColor(ORI,cv2.COLOR_BGR2GRAY)
    IMG=cv2.GaussianBlur(IMG,(5,5),1)
    IMG = cv2.adaptiveThreshold(IMG, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    IMG=cv2.bitwise_not(IMG)

    #Manipulate contours
    contours=cv2.findContours(IMG,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(contours)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    puzzleCnt = None
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        #Assumes that if we find the biggest square, it is the puzzle
        if len(approx) == 4:
            puzzleCnt = approx
            break

    #Return both colored and grayed image
    color=four_point_transform(ORI,puzzleCnt.reshape(4,2))
    gray=four_point_transform(IMG,puzzleCnt.reshape(4,2))


    return (color,gray)


