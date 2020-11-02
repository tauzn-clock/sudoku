import copy

def check_vert(sudoku,col):
    entry={}
    for x in range(1,10): entry[x]=0
    for x in range(9):
        if (sudoku[x][col]!=0):
            entry[sudoku[x][col]]+=1
            if (entry[sudoku[x][col]]>1):
                return False
    return True

def check_hori(sudoku,row):
    entry={}
    for x in range(1,10): entry[x]=0
    for x in range(9):
        if (sudoku[row][x]!=0):
            entry[sudoku[row][x]]+=1
            if (entry[sudoku[row][x]]>1):
                return False
    return True
def check_box(sudoku,coord):
    entry={}
    top=(coord//9)//3
    left=(coord%9)//3
    for x in range(1,10): entry[x]=0
    for x in range(3):
        for y in range(3):
            if (sudoku[top*3+x][left*3+y]!=0):
                entry[sudoku[top*3+x][left*3+y]]+=1
                if (entry[sudoku[top*3+x][left*3+y]]>1):
                    return False
    return True

def dfs(sudoku,coord):
    if (coord==81):
        return (True,sudoku)
    if (sudoku[coord//9][coord%9]==0):
        for x in range(1,10):
            temp_sudoku=copy.deepcopy(sudoku)
            temp_sudoku[coord//9][coord%9]=x
            row=coord//9
            col=coord%9
            if (check_vert(temp_sudoku,col) and check_hori(temp_sudoku,row) and check_box(temp_sudoku,coord)):
                TEMP=dfs(temp_sudoku,coord+1)
                if (TEMP[0]): return TEMP
        return (False,None)
    else: return dfs(sudoku,coord+1)

##sudoku=[[0 for x in range(9)] for y in range(9)]
##sudoku[2][0]=2
##sudoku[5][0]=9
##sudoku[6][0]=5
##sudoku[4][1]=2
##sudoku[8][1]=7
##sudoku[1][2]=6
##sudoku[3][2]=8
##sudoku[6][2]=9
##sudoku[7][2]=3
##sudoku[2][3]=8
##sudoku[4][3]=4
##sudoku[5][3]=6
##sudoku[8][3]=9
##sudoku[0][4]=7
##sudoku[2][5]=3
##sudoku[4][5]=9
##sudoku[5][5]=7
##sudoku[8][5]=4
##sudoku[1][6]=7
##sudoku[3][6]=5
##sudoku[6][6]=3
##sudoku[7][6]=9
##sudoku[4][7]=3
##sudoku[8][7]=5
##sudoku[2][8]=5
##sudoku[5][8]=2
##sudoku[6][8]=8
##
##ans=dfs(sudoku,0)
##for x in range(9):
##    print(ans[1][x])
##while True:
##    continue
