from random import *
import time
def ia(board,signe):
    seed(time.time())
    selection=[]
    for i in range(len(board)):
        if board[i]==0:
            selection.append(i)
    return choice(selection)