from approx_square import square
from get_puzzle import puzzle
from editor import edit
from solver import dfs
from skimage.segmentation import clear_border
import imutils
import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('epic_num_reader.model')

PIC=square("original/sudo1.png")
INFO=puzzle(PIC)
(WIDTH,HEIGHT,_)=INFO[0].shape
LOW_BOUND=0.1
HIGH_BOUND=0.8

cv2.imshow("Orig",INFO[0])
kernel = np.ones((2, 2), np.uint8)
thresh=cv2.erode(INFO[1],kernel,iterations=1)
thresh = cv2.threshold(thresh, 0, 255,
                       cv2.THRESH_OTSU)[1]

thresh = clear_border(thresh)
thresh=cv2.bitwise_not(thresh)
cv2.imshow("Cell Thresh", thresh)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

sudoku=[[0 for x in range(9)]for y in range(9)]
for c in contours:
    x,y,w,h=cv2.boundingRect(c)
    if (w<h and w*h<(WIDTH*HEIGHT/81)*HIGH_BOUND and w*h>(WIDTH*HEIGHT/81)*LOW_BOUND):
        #Extact image
        mid_x=x+w/2
        mid_y=y+h/2
        sz=max(w,h)
        new_x=int(mid_x-sz/2)
        new_y=int(mid_y-sz/2)
        cv2.rectangle(INFO[0],(new_x,new_y),(new_x+sz,new_y+sz),(0,255,0),2)
        incre=2
        crop_img=thresh[new_y-incre:new_y+sz+incre,new_x-incre:new_x+sz+incre]
        crop_img=cv2.resize(crop_img,(28,28),cv2.INTER_AREA)
        crop_img=cv2.bitwise_not(crop_img)
        #cv2.imshow(" ",crop_img)

        #Run throught Model
        crop_img=[crop_img]
        crop_img=np.array(crop_img)
        crop_img=crop_img.reshape(-1,28,28,1)
        crop_img = tf.keras.utils.normalize(crop_img, axis=1)
        prob=model.predict(crop_img)


        if (prob[0][np.argmax(prob[0])]>0.3):
            sudoku[int(9*(y+h/2)/(WIDTH))][int(9*(x+w/2)/(HEIGHT))]=np.argmax(prob[0])
            
for x in range(9): print(sudoku[x])

sudoku=edit(sudoku)

ANS=dfs(sudoku,0)
for x in range(9): print(ANS[1][x])

cv2.imshow("Orig",INFO[0])
