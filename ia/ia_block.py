from random import *
import time

def ia(board,signe):
    seed(time.time())
    block_selection=[]
    to_play=[]
    egalite=[]
    column1_selection=[]
    column2_selection=[]
    column3_selection=[]
    case_column1=0
    case_column2=0
    case_column3=0
    case_column_priority1=0
    case_column_priority2=0
    case_column_priority3=0
    diagonal1_selection=[]
    diagonal2_selection=[]
    case1=0
    case2=0
    case_diag_priority1=0
    case_diag_priority2=0
    line1_selection=[]
    line2_selection=[]
    line3_selection=[]
    case_line1=0
    case_line2=0
    case_line3=0
    case_line_priority1=0
    case_line_priority2=0
    case_line_priority3=0
    
    for i in range(len(board)):
        if board[i]==0:
            egalite.append(i)
        if board[i]==2 or board[i]==0:
            block_selection.append(i)
    
    for i in range(len(board)):
        if i%4==0:
            case1+=1
            if board[i]==0:
                diagonal1_selection.append(i)
            elif board[i]==1:
                case_diag_priority1-=1
            elif board[i]==2:
                case_diag_priority1+=1   
        if i%2==0 and i>0 and i<8 :
            case2+=1
            if board[i]==0:
                diagonal2_selection.append(i)
            elif board[i]==1:
                case_diag_priority2-=1
            elif board[i]==2:
                case_diag_priority2+=1
        
        if i<3:
            case_line1+=1
            if board[i]==0:
                line1_selection.append(i)
            elif board[i]==1:
                case_line_priority1-=1
            elif board[i]==2:
                case_line_priority1+=1
        elif i<6:
            case_line2+=1
            if board[i]==0:
                line2_selection.append(i)
            elif board[i]==1:
                case_line_priority2-=1
            elif board[i]==2:
                case_line_priority2+=1
        elif i<9:
            case_line3+=1
            if board[i]==0:
                line3_selection.append(i)
            elif board[i]==1:
                case_line_priority3-=1
            elif board[i]==2:
                case_line_priority3+=1
        
        if i%3==0:
            case_column1+=1
            if board[i]==0:
                column1_selection.append(i)
            elif board[i]==1:
                case_column_priority1-=1
            elif board[i]==2:
                case_column_priority1+=1        
        if i%3==1:
            case_column2+=1
            if board[i]==0:
                column2_selection.append(i)
            elif board[i]==1:
                case_column_priority2-=1
            elif board[i]==2:
                case_column_priority2+=1    
        if i%3==2:
            case_column3+=1
            if board[i]==0:
                column3_selection.append(i)
            elif board[i]==1:
                case_column_priority3-=1
            elif board[i]==2:
                case_column_priority3+=1
        
        if case_column_priority1==2:
            to_play=column1_selection
        elif case_column_priority2==2:
            to_play=column2_selection
        elif case_column_priority3==2:
            to_play=column3_selection
                

                
        if case_diag_priority1==2:
            to_play=diagonal1_selection  
        elif case_diag_priority2==2:
            to_play=diagonal2_selection
            
        
        if case_line_priority1==2:
            to_play=line1_selection
        elif case_line_priority2==2:
            to_play=line2_selection
        elif case_line_priority3==2:
            to_play=line3_selection

            


    
    if len(to_play):
        return choice(to_play)
    else:
        return choice(egalite)
    return False