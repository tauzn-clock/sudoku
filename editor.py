import tkinter as tk

def edit(sudoku):
    window = tk.Tk()
    grid_size=10
    all_text_box=[]
    
    def add_text_box(x,y):
        #note width and height is in char and lines
        new_text=tk.Text(window,width=2,height=1)
        if (sudoku[x][y]!=0): new_text.insert(tk.END,str(sudoku[x][y]))
        new_text.grid(column=y,padx=3,pady=3,row=x)
        all_text_box.append(new_text)

    #Set Up GUI window
    window.columnconfigure([0,1,2,3,4,5,6,7,8,9],minsize=grid_size)
    window.rowconfigure([0,1,2,3,4,5,6,7,8],minsize=grid_size)
    for x in range(9):
        for y in range(9):
            add_text_box(x,y)
    button=tk.Button(window,text="ENTER")
    button.grid(column=9,row=0)

    #After Editting
    def keyevent(event):
        for x in range(81):
            result=all_text_box[x].get("1.0","end")
            if (len(result)==2):
                sudoku[x//9][x%9]=int(result[0])
        #for x in range(9): print(sudoku[x])
        window.destroy()
    button.bind("<Button-1>",keyevent)
    window.mainloop()
    return sudoku
