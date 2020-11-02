##import pandas as pd
##import cv2
##import os
##
####index=[53,2,4,5,4,2,3,6,2,0]
####index=["0","1","2","3","4","5","6","7","8","9"]
####d={0:[53],1:[15],2:[17],\
####   3:[18],4:[17],5:[15],\
####   6:[16],7:[18],8:[14],9:[13]}
####df=pd.DataFrame(data=d)
####df.to_csv("data_cnt.csv")
##
##
####
####
####dir_path = os.path.dirname(os.path.realpath(__file__))
####dir_path+="\\test.png"
####print(dir_path)
####
####
####img=cv2.imread("original/sudo.png",cv2.COLOR_BGR2GRAY)
####cv2.imshow(" ",img)
####cv2.imwrite(dir_path,img)
##
##dir_path = os.path.dirname(os.path.realpath(__file__))
##
##df=pd.read_csv("data_cnt.csv")
##df["0"][0]+=10000000
##df.to_csv("data_cnt.csv")
##print(df)

import tkinter as tk

sudoku=[[0 for x in range(9)] for y in range(9)]
sudoku[0][1]=3
sudoku[6][6]=2
window = tk.Tk()
grid_size=10

def add_text_box(x,y):
    global window,sudoku,grid_size
    #note width and height is in char and lines
    new_text=tk.Text(window,width=2,height=1)
    if (sudoku[x][y]!=0): new_text.insert(tk.END,str(sudoku[x][y]))
    new_text.grid(column=y,padx=3,pady=3,row=x)


window.columnconfigure([0,1,2,3,4,5,6,7,8],minsize=grid_size)
window.rowconfigure([0,1,2,3,4,5,6,7,8],minsize=grid_size)

for x in range(9):
    for y in range(9):
        add_text_box(x,y)
print(sudoku)
