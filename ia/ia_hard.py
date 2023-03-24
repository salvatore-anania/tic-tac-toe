from random import *
import time

def ia(board,signe):
    seed(time.time())
    priority={"case_column1":0,"case_column2":0,"case_column3":0,"case_diag1":0,"case_diag2":0,"case_line1":0,"case_line2":0,"case_line3":0}
    selection={"column1":[],"column2":[],"column3":[],"diagonal1":[],"diagonal2":[],"line1":[],"line2":[],"line3":[]}
    case_count={"column1":0,"column2":0,"column3":0,"diagonal1":0,"diagonal2":0,"line1":0,"line2":0,"line3":0}
    to_play=[]
    egalite=[]
    max=0
    
    for i in range(len(board)):
        if board[i]==0:
            egalite.append(i)
    
    for i in range(len(board)):
        
        if i%4==0:
            
            if board[i]==0:
                case_count["diagonal1"]+=1
                selection["diagonal1"].append(i)
            elif board[i]==signe:
                case_count["diagonal1"]+=2
                priority["case_diag1"]-=20
            else:
                case_count["diagonal1"]-=2
                priority["case_diag1"]+=1   
        if i%2==0 and i>0 and i<8 :
            
            if board[i]==0:
                case_count["diagonal2"]+=1
                selection["diagonal2"].append(i)
            elif board[i]==signe:
                case_count["diagonal2"]+=2
                priority["case_diag2"]-=20
            else:
                case_count["diagonal2"]-=2
                priority["case_diag2"]+=1
        
        if i<3:
            
            if board[i]==0:
                case_count["line1"]+=1
                selection["line1"].append(i)
            elif board[i]==signe:
                case_count["line1"]+=2
                priority["case_line1"]-=20
            else:
                case_count["line1"]-=2
                priority["case_line1"]+=1
        if i>=3 and i<6:
            
            if board[i]==0:
                case_count["line2"]+=1
                selection["line2"].append(i)
            elif board[i]==signe:
                case_count["line2"]+=2
                priority["case_line2"]-=20
            else:
                case_count["line2"]-=2
                priority["case_line2"]+=1
        if i>=6 and i<9:
            
            if board[i]==0:
                case_count["line3"]+=1
                selection["line3"].append(i)
            elif board[i]==signe:
                case_count["line3"]+=2
                priority["case_line3"]-=20
            else:
                case_count["line3"]-=2
                priority["case_line3"]+=1
                
        #verifie les colones
        
        if i%3==0:
            
            if board[i]==0:
                case_count["column1"]+=1
                selection["column1"].append(i) 
            elif board[i]==signe:
                case_count["column1"]+=2
                priority["case_column1"]-=20
            else:
                case_count["column1"]-=2
                priority["case_column1"]+=1
        if i%3==1:  
            if board[i]==0:
                case_count["column2"]+=1
                selection["column2"].append(i)
            elif board[i]==signe:
                case_count["column2"]+=2
                priority["case_column2"]-=20
            else:
                case_count["column2"]-=2
                priority["case_column2"]+=1  
        if i%3==2:
            
            if board[i]==0:
                case_count["column3"]+=1
                selection["column3"].append(i)
            elif board[i]==signe:
                case_count["column3"]+=2
                priority["case_column3"]-=20
            else:
                case_count["column3"]-=2
                priority["case_column3"]+=1
            
        for i in case_count.values():
            if i>max:
                max=i
            
        if case_count["diagonal1"]>3:
            for i in case_count.keys():
                if case_count["diagonal1"]>=max:
                    to_play=selection["diagonal1"]
                if case_count["diagonal1"]==4 and case_count["diagonal2"]==4 and 2 not in priority.values():
                    to_play=selection["diagonal1"]
                    break
        if case_count["diagonal2"]>3:
            for i in case_count.keys():
                if case_count["diagonal2"]>=max:
                    to_play=selection["diagonal2"]
                if case_count["diagonal1"]==4 and case_count["diagonal2"]==4 and 2 not in priority.values():
                    to_play=selection["diagonal2"]
                    break
                    
            
        if case_count["column1"]>3:
            for i in case_count.keys():
                if case_count["column1"]>=max:
                    to_play=selection["column1"]
        if case_count["column2"]>3:
            for i in case_count.keys():
                if case_count["column2"]>=max:
                    to_play=selection["column2"]
        if case_count["column3"]>3:
            for i in case_count.keys():
                if case_count["column3"]>=max:
                    to_play=selection["column3"]
    
        
        if case_count["line1"]>3:
            for i in case_count.keys():
                if case_count["line1"]>=max:
                    to_play=selection["line1"]
        if case_count["line2"]>3:
            for i in case_count.keys():
                if case_count["line2"]>=max:
                    to_play=selection["line2"]
        if case_count["line3"]>3:
            for i in case_count.keys():
                if case_count["line3"]>=max:
                    to_play=selection["line3"]




        if priority["case_column1"]==2 and 5 not in case_count.values():
            to_play=selection["column1"]
        if priority["case_column2"]==2 and 5 not in case_count.values():
            to_play=selection["column2"]
        if priority["case_column3"]==2 and 5 not in case_count.values():
            to_play=selection["column3"]
                

                
        if priority["case_diag1"]==2 and 5 not in case_count.values():
            to_play=selection["diagonal1"]
        if priority["case_diag2"]==2 and 5 not in case_count.values():
            to_play=selection["diagonal2"]
            
        
        if priority["case_line1"]==2 and 5 not in case_count.values():
            to_play=selection["line1"]
            
        if priority["case_line2"]==2 and 5 not in case_count.values():
            to_play=selection["line2"]
            
        if priority["case_line3"]==2 and 5 not in case_count.values():
            to_play=selection["line3"]
            

    
    if len(to_play):
        if 0 in to_play:
            return 0
        elif 2 in to_play:
            return 2
        elif 6 in to_play:
            return 6
        elif 8 in to_play:
            return 8
        return choice(to_play)
    else:
        if len(egalite)>=8:
            return choice((0,2,6,8))
        return choice(egalite)
