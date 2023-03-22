from random import *
import time

def ia(board,signe):
    seed(time.time())
    play_selection=[]
    to_play=[]
    egalite=[]
    column1_selection=[]
    column2_selection=[]
    column3_selection=[]
    case1=0
    case2=0
    case3=0
    for i in range(len(board)):
        if board[i]==0:
            egalite.append(i)
        if board[i]==0 or board[i]==1:
            play_selection.append(i)
    
    for i in range(len(play_selection)):
        
        if play_selection[i]%3==0:
            case1+=1
            if board[play_selection[i]]!=1:
                column1_selection.append(play_selection[i])
                
        if play_selection[i]%3==1:
            case2+=1
            if board[play_selection[i]]!=1:
                column2_selection.append(play_selection[i])
                
        if play_selection[i]%3==2:
            case3+=1
            if board[play_selection[i]]!=1:
                column3_selection.append(play_selection[i])

        if case1==3:
            to_play=column1_selection
            break
        elif case2==3:
            to_play=column2_selection
            break
        elif case3==3:
            to_play=column3_selection
            break
        
    
    if len(to_play):
        return choice(to_play)
    else:
        return choice(egalite)
    return False
