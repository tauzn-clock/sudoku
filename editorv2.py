import tkinter as tk
import copy

sudoku=[[0 for x in range(9)] for y in range(9)]
sudoku[2][0]=2
sudoku[5][0]=9
sudoku[6][0]=5
sudoku[4][1]=2
sudoku[8][1]=7
sudoku[1][2]=6
sudoku[3][2]=8
sudoku[6][2]=9
sudoku[7][2]=3
sudoku[2][3]=8
sudoku[4][3]=4
sudoku[5][3]=6
sudoku[8][3]=9
sudoku[0][4]=7
sudoku[2][5]=3
sudoku[4][5]=9
sudoku[5][5]=7
sudoku[8][5]=4
sudoku[1][6]=7
sudoku[3][6]=5
sudoku[6][6]=3
sudoku[7][6]=9
sudoku[4][7]=3
sudoku[8][7]=5
sudoku[2][8]=5
sudoku[5][8]=2
sudoku[6][8]=8

def edit(sudoku):
    window = tk.Tk()
    grid_size=10
    all_button_sudoku=[]
    all_button_val=[]
    global cur_x,cur_y,cur_val
    cur_x=0
    cur_y=0
    cur_val=0

    #Add sudoku val buttons
    def add_button_sudoku(x,y):
        global cur_x,cur_y,cur_val
        button_str=""
        if (sudoku[x][y]!=0): button_str=str(sudoku[x][y])
        bg_color=""
        if ((x//3+y//3)%2==0): bg_color="#ff00ff"
        else: bg_color="#00ffff"
        new_button=tk.Button(window,text=button_str,width=2,height=1,bg=bg_color)
        new_button.grid(column=y,padx=3,pady=3,row=x)
        all_button_sudoku.append(new_button)

        #Replace button text with cur_val
        def keyevent(event):
            global cur_x,cur_y,cur_val
            cur_x=x
            cur_y=y
            all_button_sudoku[9*cur_x+cur_y]['text']=str(cur_val)
        new_button.bind("<Button-1>",keyevent)

    #Add val buttons
    def add_button_val(x,y):
        global cur_val
        button_str=str(y)
        new_button=tk.Button(window,text=button_str,width=2,height=1)
        new_button.grid(column=y,padx=3,pady=3,row=x)
        all_button_sudoku.append(new_button)

        #Change cur_val
        def keyevent(event):
            global cur_val
            cur_val=y
        new_button.bind("<Button-1>",keyevent)

    #Set Up GUI window
    window.columnconfigure([0,1,2,3,4,5,6,7,8,9],minsize=grid_size)
    window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10],minsize=grid_size)
    for x in range(9):
        for y in range(9):
            add_button_sudoku(x,y)

    for x in range(10):
        add_button_val(10,x)
    button=tk.Button(window,text="ENTER")
    button.grid(column=9,row=0)

    
    #After Editting
    def keyevent(event):
        for x in range(81):
            result=all_button_sudoku[x]["text"]
            if len(result)==1:
                sudoku[x//9][x%9]=int(result)
        window.destroy()
    button.bind("<Button-1>",keyevent)
    window.mainloop()
    return sudoku
