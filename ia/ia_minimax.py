              
def minimax(plateau, signe_actuel,signe_gagnant,depth,alpha,beta):
    if test_winning(plateau,signe_gagnant)!="vide":
        return test_winning(plateau,signe_gagnant)
    
    if signe_gagnant==signe_actuel:
        maxEval=-50
        for i in range(len(plateau)):
            if plateau[i] ==0:
                plateau[i]=signe_actuel
                if signe_actuel==1:
                    eval=minimax(plateau,signe_actuel+1, signe_gagnant,depth+1,alpha,beta)
                else:
                    eval=minimax(plateau,signe_actuel-1, signe_gagnant,depth+1,alpha,beta)
                maxEval = max(maxEval,eval)  
                plateau[i]=0
            alpha=max(alpha,maxEval)  
            if beta<=alpha:
                break
        return maxEval
    else:
        minEval=50
        for i in range(len(plateau)):
            if plateau[i] ==0:
                plateau[i]=signe_actuel
                if signe_actuel==1:
                    eval=minimax(plateau,signe_actuel+1,signe_gagnant,depth+1,alpha,beta)
                else:
                    eval=minimax(plateau,signe_actuel-1,signe_gagnant,depth+1,alpha,beta)
                minEval = min(minEval,eval)
                plateau[i]=0
            beta=min(beta,minEval)  
            if beta<=alpha:
                break
        return minEval



def ia(board,signe):
    play_move=-50
    move=0
    for i in range(len(board)):
        if board[i] ==0:
            board[i]=signe
            if signe==1:
                best_move=minimax(board,signe+1,signe,0,-50,50)
            else:
                best_move=minimax(board,signe-1,signe,0,-50,50)
            board[i]=0
            if best_move>play_move:
                play_move=best_move
                move=i
    return move
                
    
def test_winning(board,signe):
    croix=[]
    cercle=[]
    count=0
    for i in range(len(board)):
        if board[i]==1:
            croix.append(i)
        elif board[i]==2:
            cercle.append(i)
        else:
            count+=1
    ligne1=set([0,1,2])
    ligne2=set([3,4,5])
    ligne3=set([6,7,8])
    column1=set([0,3,6])
    column2=set([1,4,7])
    column3=set([2,5,8])
    diag1=set([0,4,8])
    diag2=set([2,4,6])
    test_win_croix=ligne1.issubset(croix) or ligne2.issubset(croix)  or ligne3.issubset(croix) or column1.issubset(croix) or column2.issubset(croix)  or column3.issubset(croix) or diag1.issubset(croix) or diag2.issubset(croix)
    test_win_cercle=ligne1.issubset(cercle) or ligne2.issubset(cercle)  or ligne3.issubset(cercle) or column1.issubset(cercle) or column2.issubset(cercle)  or column3.issubset(cercle) or diag1.issubset(cercle) or diag2.issubset(cercle)
    if signe==1:
        if test_win_croix:
            return 1
        elif test_win_cercle:
            return -1
        elif count==0:
            return 0
        else:
            return "vide"
    else:
        if test_win_croix:
            return -1
        elif test_win_cercle:
            return 1
        elif count==0:
            return 0
        else:
            return "vide"