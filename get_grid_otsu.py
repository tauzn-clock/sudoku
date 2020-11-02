from skimage.segmentation import clear_border
import imutils
import cv2
import numpy as np
import tensorflow as tf

def grid(RAW_INFO,MODEL_NAME):
    (WIDTH,HEIGHT,_)=RAW_INFO[0].shape
    LOW_BOUND=0.1
    HIGH_BOUND=0.8
    MODEL = tf.keras.models.load_model(MODEL_NAME)
    SUDOKU=[[0 for x in range(9)]for y in range(9)]

    cv2.imshow("NUMBERS",RAW_INFO[0])
    #Process Black White Image
    kernel = np.ones((2, 2), np.uint8)
    thresh=cv2.erode(RAW_INFO[1],kernel,iterations=1)
    thresh = cv2.threshold(thresh, 0, 255,
                           cv2.THRESH_OTSU)[1]
    thresh = clear_border(thresh)
    thresh=cv2.bitwise_not(thresh)
    #cv2.imshow("GRAY_NUMBERS",thresh)


    #Use contours to identify the numbers
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        x,y,w,h=cv2.boundingRect(c)
        if (w*h<(WIDTH*HEIGHT/81)*HIGH_BOUND and w*h>(WIDTH*HEIGHT/81)*LOW_BOUND):
            #Extact image
            mid_x=x+w/2
            mid_y=y+h/2
            sz=max(w,h)
            new_x=int(mid_x-sz/2)
            new_y=int(mid_y-sz/2)
            incre=2
            
            crop_img=thresh[new_y-incre:new_y+sz+incre,new_x-incre:new_x+sz+incre]
            crop_img=cv2.resize(crop_img,(28,28),cv2.INTER_AREA)
            crop_img=cv2.bitwise_not(crop_img)


            #Run throught Model
            crop_img=[crop_img]
            crop_img=np.array(crop_img)
            crop_img=crop_img.reshape(-1,28,28,1)
            crop_img = tf.keras.utils.normalize(crop_img, axis=1)
            prob=MODEL.predict(crop_img)
            if (prob[0][np.argmax(prob[0])]>0.3 and
                SUDOKU[int(9*(y+h/2)/(WIDTH))][int(9*(x+w/2)/(HEIGHT))]==0):
                SUDOKU[int(9*(y+h/2)/(WIDTH))][int(9*(x+w/2)/(HEIGHT))]=np.argmax(prob[0])
                
    #for x in range(9): print(sudoku[x])
    return SUDOKU
