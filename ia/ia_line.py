from random import *
import time

#IA line up


def ia(board,signe):
    seed(time.time())
    play_selection=[]
    to_play=[]
    egalite=[]
    win_selection=0
    case_count=0
    
    for i in range(len(board)):
        if board[i]==0:
            egalite.append(i)
        if board[i]==0 or board[i]==1:
            play_selection.append(i)
    
    for i in range(len(play_selection)):
        
        if play_selection[i]%3==0:
            case_count=0
            to_play=[]
            win_selection=0
        win_selection+=play_selection[i]
        case_count+=1

        if board[play_selection[i]]!=1:
            to_play.append(play_selection[i])
        if win_selection%3==0 and case_count==3:
            break

    
    if len(to_play):
        return choice(to_play)
    else:
        return choice(egalite)
    return False
