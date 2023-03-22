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
    case_column1=0
    case_column2=0
    case_column3=0
    diagonal1_selection=[]
    diagonal2_selection=[]
    case1=0
    case2=0
    line_play=[]
    win_selection=0
    case_count=0
    
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
        
        if play_selection[i]%3==0:
            case_count=0
            line_play=[]
            win_selection=0
        win_selection+=play_selection[i]
        case_count+=1
        if board[play_selection[i]]!=1:
            line_play.append(play_selection[i])
        
        if play_selection[i]%3==0:
            case_column1+=1
            if board[play_selection[i]]!=1:
                column1_selection.append(play_selection[i])        
        if play_selection[i]%3==1:
            case_column2+=1
            if board[play_selection[i]]!=1:
                column2_selection.append(play_selection[i])       
        if play_selection[i]%3==2:
            case_column3+=1
            if board[play_selection[i]]!=1:
                column3_selection.append(play_selection[i])

        if case_column1==3:
            to_play=column1_selection
            break
        elif case_column2==3:
            to_play=column2_selection
            break
        elif case_column3==3:
            to_play=column3_selection
            break    

                
        if case1==3:
            to_play=diagonal1_selection
            break
        elif case2==3:
            to_play=diagonal2_selection
            break
        
        if win_selection%3==0 and case_count==3:
            to_play=line_play
            break

    
    if len(to_play):
        return choice(to_play)
    else:
        return choice(egalite)
    return False