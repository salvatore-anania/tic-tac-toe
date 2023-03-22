from random import *
import time

def ia(board,signe):
    seed(time.time())
    play_selection=[]
    to_play=[]
    egalite=[]
    diagonal1_selection=[]
    diagonal2_selection=[]
    case1=0
    case2=0
    for i in range(len(board)):
        if board[i]==0:
            egalite.append(i)
        if board[i]==0 or board[i]==1:
            play_selection.append(i)
    
    for i in range(len(play_selection)):
        
        if play_selection[i]%4==0:
            case1+=1
            if board[play_selection[i]]!=1:
                diagonal1_selection.append(play_selection[i])
                
        if play_selection[i]%2==0 and play_selection[i]>0 and play_selection[i]<8 :
            case2+=1
            if board[play_selection[i]]!=1:
                diagonal2_selection.append(play_selection[i])
                

        if case1==3:
            to_play=diagonal1_selection
            break
        elif case2==3:
            to_play=diagonal2_selection
            break

    
    if len(to_play):
        return choice(to_play)
    else:
        return choice(egalite)
    return False