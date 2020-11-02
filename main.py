from approx_square import square
from get_puzzle import puzzle
from get_grid_otsu import grid
from editorv2 import edit
from solverv2 import func

PATH="original/sudo2.png"
IMG=square(PATH)
RAW_INFO=puzzle(IMG)
SUDOKU=grid(RAW_INFO,'emnist-516.model')
SUDOKU=edit(SUDOKU)
ANS=func(SUDOKU)

for x in range(9): print(ANS[1][x])
