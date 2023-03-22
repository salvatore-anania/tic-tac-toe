from random import *
import time

def ia(board,signe):
    seed(time.time())
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
    case_diag1=0
    case_diag2=0
    case_line1=0
    case_line2=0
    case_line3=0
    case_column_priority1=0
    case_column_priority2=0
    case_column_priority3=0
    case_diag_priority1=0
    case_diag_priority2=0
    case_line_priority1=0
    case_line_priority2=0
    case_line_priority3=0
    line1_selection=[]
    line2_selection=[]
    line3_selection=[]
    
    for i in range(len(board)):
        if board[i]==0:
            egalite.append(i)
    
    for i in range(len(board)):
        
        if i%4==0:
            
            if board[i]==0:
                case_diag1+=1
                diagonal1_selection.append(i)
            elif board[i]==1:
                case_diag1+=1
                case_diag_priority1-=10
            elif board[i]==2:
                case_diag_priority1+=1   
        if i%2==0 and i>0 and i<8 :
            
            if board[i]==0:
                case_diag2+=1
                diagonal2_selection.append(i)
            elif board[i]==1:
                case_diag2+=1
                case_diag_priority2-=10
            elif board[i]==2:
                case_diag_priority2+=1
        
        if i<3:
            
            if board[i]==0:
                case_line1+=1
                line1_selection.append(i)
            elif board[i]==1:
                case_line1+=1
                case_line_priority1-=10
            elif board[i]==2:
                case_line_priority1+=1
        if i>=3 and i<6:
            
            if board[i]==0:
                case_line2+=1
                line2_selection.append(i)
            elif board[i]==1:
                case_line2+=1
                case_line_priority2-=10
            elif board[i]==2:
                case_line_priority2+=1
        if i>=6 and i<9:
            
            if board[i]==0:
                case_line3+=1
                line3_selection.append(i)
            elif board[i]==1:
                case_line3+=1
                case_line_priority3-=10
            elif board[i]==2:
                case_line_priority3+=1
        
        if i%3==0:
            
            if board[i]==0:
                case_column1+=1
                column1_selection.append(i) 
            if board[i]==1:
                case_column1+=1
                case_column_priority1-=10
            if board[i]==2:
                case_column_priority1+=1       
        if i%3==1:
            
            if board[i]==0:
                case_column2+=1
                column2_selection.append(i)
            if board[i]==1:
                case_column2+=1
                case_column_priority2-=10
            if board[i]==2:
                case_column_priority2+=1  
        if i%3==2:
            
            if board[i]==0:
                case_column3+=1
                column3_selection.append(i)
            if board[i]==1:
                case_column3+=1
                case_column_priority3-=10
            if board[i]==2:
                case_column_priority3+=1
            
        if case_column1==3:
            to_play=column1_selection
            if len(column1_selection)==1:
                break
        elif case_column2==3:
            to_play=column2_selection
            if len(column2_selection)==1:
                break
        elif case_column3==3:
            to_play=column3_selection 
            if len(column3_selection)==1:
                break 

                
        if case_diag1==3:
            to_play=diagonal1_selection
            if len(diagonal1_selection)==1:
                break 
        elif case_diag2==3:
            to_play=diagonal2_selection
            if len(diagonal2_selection)==1:
                break
        
        if case_line1==3:
            to_play=line1_selection
            if len(line1_selection)==1:
                break
        elif case_line2==3:
            to_play=line2_selection
            if len(line2_selection)==1:
                break
        elif case_line3==3:
            to_play=line3_selection
            if len(line3_selection)==1:
                break
            
        if case_column_priority1==2:
            to_play=column1_selection
            if case_column1==3:
                break
        elif case_column_priority2==2:
            to_play=column2_selection
            if case_column2==3:
                break
        elif case_column_priority3==2:
            to_play=column3_selection
            if case_column3==3:
                break
                

                
        if case_diag_priority1==2:
            to_play=diagonal1_selection
            if case_diag1==3:
                break 
        elif case_diag_priority2==2:
            to_play=diagonal2_selection
            if case_diag2==3:
                break
            
        
        if case_line_priority1==2:
            to_play=line1_selection
            if case_line1==3:
                break
        elif case_line_priority2==2:
            to_play=line2_selection
            if case_line2==3:
                break
        elif case_line_priority3==2:
            to_play=line3_selection
            if case_line3==3:
                break


    
    if len(to_play):
        return choice(to_play)
    else:
        return choice(egalite)
