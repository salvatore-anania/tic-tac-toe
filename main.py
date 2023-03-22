import pygame as pg
import ia.ia_hard as ia
import json

def affiche_cercle(click_save):
    for i in click_save:
        screen.blit(cercle_img,(grille_case[i][0],grille_case[i][1]))
    
def affiche_croix(click_save):
    for i in click_save:
        screen.blit(croix_img,(grille_case[i][0],grille_case[i][1]))
        
def test_win(croix,cercle):
    global play_game,choose
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
    if test_win_croix:
        screen.blit(croix_win,(0,0))
        play_game=False
        if choose==1:
            battle_save(first_user,username)
    elif test_win_cercle:
        screen.blit(cercle_win,(0,0))
        play_game=False
        if choose==2:
            score_save(first_user)
        elif choose==1:
            battle_save(first_user,username)
            
    elif len(cercle)>4 or len(croix)>4 :
        screen.blit(egalite,(0,0))
        play_game=False
    
def test_click_position(x,y):
    count_case=-1
    for case in grille_case:
        count_case+=1
        if y>case[1] and y<case[3] and x>case[0] and x<case[2]:
            return (count_case)
    return(0,0)

def menu_back():
    if event.type == pg.MOUSEBUTTONDOWN:
        if pg.mouse.get_pos()[0] in range(275,475) and pg.mouse.get_pos()[1]in range(500,557):
            global cercle_save,croix_save,signe_save,play_game,board,choose
            cercle_save=[]
            croix_save=[]
            signe_save=1
            board=[]
            screen.fill((0,0,0))
            for i in range(9):
                board.append(0)
            play_game=True
            choose=0
    
def sign_position():
    if event.type == pg.MOUSEBUTTONDOWN:
        global cercle_save,croix_save,signe_save,board
        pos=test_click_position(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
        if pos in cercle_save or pos in croix_save:
            pos=0
        else:
            if signe_save==2:
                if isinstance(pos,int):
                    board[pos]=2
                    cercle_save.append(pos)
                    signe_save=1
            else:
                if isinstance(pos,int):
                    board[pos]=1
                    croix_save.append(pos)
                    signe_save=2

def quit():
    global running
    if event.type == pg.QUIT:
        running = False

def test_choose_mode():
    global choose
    if event.type == pg.MOUSEBUTTONDOWN:
        if pg.mouse.get_pos()[0] in range(253,571) and pg.mouse.get_pos()[1] in range(150,225):
            choose=1
        elif pg.mouse.get_pos()[0] in range(253,571) and pg.mouse.get_pos()[1]in range(260,334):
            choose=2

def user_set():
    global username,active,color,connect,first_user,play_game,second_user
    font = pg.font.Font(None, 32)
    input_box = pg.Rect(253, 85, 320, 32)
    color_active = pg.Color('lightskyblue3')

    if event.type == pg.MOUSEBUTTONDOWN:
        # If the user clicked on the input_box rect.
        if input_box.collidepoint(event.pos):
            # Toggle the active variable.
            active = True
            color = color_active
    if event.type == pg.KEYDOWN:
        if active:
            if event.key == pg.K_RETURN:
                save(username)
                if len(first_user)<1:
                    first_user=username
                    username=""
                active=False
                connect=True
                color=(63,72,204)
                play_game=True
                second_user=True
            elif event.key == pg.K_BACKSPACE:
                username = username[:-1]
            elif len(username)<20:
                username += event.unicode

    # Render the current username.
    txt_surface = font.render(username, True, color)
    # Resize the box if the username is too long.
    screen.blit(connection,(0,0))
    
    # Blit the username.
    
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    
    # Blit the input_box rect.
    pg.draw.rect(screen, color, input_box, 2)
    
    pg.display.flip()
        
def save(user):
    try:
        open("data_ia.json", "x")
    except:
        nothing=0
    ecrire=open("data_ia.json", "r+")
    try:
        donnes=json.load(ecrire)
    except:
        ecrire.write("{\""+user+"\":\"0\"}")
    else:
        donnes[user] = 0
        ecrire.seek(0)
        ecrire.truncate(0)
        ecrire.write(json.dumps(donnes))
        ecrire.close()
           
def battle_save(user1,user2):
    try:
        open("data_battle.json", "x")
    except:
        ecrire=0  
    ecrire=open("data_battle.json", "r+")
    try:
        donnes=json.load(ecrire)
    except:
        ecrire.write("{\""+user1+" VS "+user2+"\":\"0 0\"}")
    else:
        ajout=int(donnes[user1+" VS "+user2][0])+1
        donnes[user1+" VS "+user2]=str(ajout)+donnes[user1+" VS "+user2][1:]
        ecrire.seek(0)
        ecrire.truncate(0)
        ecrire.write(json.dumps(donnes))
        ecrire.close()

def score_save(user):
    ecrire=open("data_ia.json", "r+")
    try:
        donnes=json.load(ecrire)
    except:
        ecrire.write("{\""+user+"\":\"0\"}")
    else:
        donnes[user] += 100
        ecrire.seek(0)
        ecrire.truncate(0)
        ecrire.write(json.dumps(donnes))
        ecrire.close()
        
def connected_choose():
    screen.blit(mode_choose,(0,0))
    font = pg.font.SysFont("calibri", 32, bold=True)
    txt_surface = font.render(first_user, True, color)
    screen.blit(txt_surface, (412- (txt_surface.get_width()/2), 85))

def play_screen():
    screen.fill((0,0,0))
    screen.blit(background,(50,50))
    connected_play()
    affiche_cercle(cercle_save)
    affiche_croix(croix_save)
            
def connected_play():
    
    if choose==2:
        user_info=lire()
        font = pg.font.SysFont("calibri", 32, bold=True)
        name = font.render(first_user, True, color)
        score = font.render("score : "+str(user_info[first_user]), True, color)
        screen.blit(name, (400-(name.get_width()/2) , 10))
        screen.blit(score, (450+(name.get_width()/2) , 10))
    else:
        battle_info=lire_battle()
        font = pg.font.SysFont("calibri", 32, bold=True)
        name1 = font.render(first_user+" : "+battle_info[first_user+" VS "+username][0], True, color)
        contre = font.render("contre", True, color)
        name2 = font.render(username+" : "+battle_info[first_user+" VS "+username][2], True, color)
        screen.blit(name1, (50 , 10))
        screen.blit(contre, (400-(contre.get_width()/2), 10))
        screen.blit(name2, (750-name2.get_width() , 10))

def lire():
    with open("data_ia.json", "r") as affiche:
        test=json.load(affiche)
    return test

def lire_battle():
    with open("data_battle.json", "r") as affiche:
        test=json.load(affiche)
    return test
         
pg.init()

pg.display.set_caption("tic_tac_toe")
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

screen = pg.display.set_mode((800,600))
background=pg.image.load("Grid.png")
cercle_win=pg.image.load("win_cercle.png")
croix_win=pg.image.load("croix_win.png")
egalite=pg.image.load("egalite.png")
rejouer=pg.image.load("rejouer.png")
mode_choose=pg.image.load("mode_choose.png")
connection=pg.image.load("connection.png")
cercle_img=pg.image.load("cercle.png")
croix_img=pg.image.load("croix.png")


grille_case=((75,55,308,221),(308,55,541,221),(541,55,750,221),(75,221,308,387),(308,221,541,387),(541,221,750,387),(75,387,308,548),(308,387,541,548),(541,387,750,548))     
        
global play_game,cercle_save,croix_save,signe_save,board,username,active,color,connect,first_user,second_user
first_user=""
color = pg.Color((63,72,204))
running=True
active=False
connect=False
second_user=False
username = ''
cercle_save=[]
croix_save=[]
signe_save=1
board=[]
play_game=True
choose=0

for i in range(9):
    board.append(0)

while running:
    if choose==0:
        
        for event in pg.event.get():
            quit()
            if connect:
                connected_choose()
                test_choose_mode()
            else:
                user_set()
                second_user=False    
    elif choose==1:
        
        if play_game and second_user:
            play_screen()
            test_win(croix_save,cercle_save)
            sign_position()
            for event in pg.event.get():
                quit()
                sign_position()
        elif play_game==False:
            screen.blit(rejouer,(275,500))
            for event in pg.event.get():
                username=""
                second_user=False
                quit()
                menu_back()
        elif second_user==False:
            for event in pg.event.get():
                user_set()
                quit()
    elif choose==2:
        if play_game:
            play_screen()
            test_win(croix_save,cercle_save)
            if signe_save==1 and len(cercle_save)<5 and len(croix_save)<5:
                ia_play=ia.ia(board,1)
                board[ia_play]=1
                croix_save.append(ia_play)
                signe_save=2
            else:
                for event in pg.event.get():
                    quit()
                    sign_position()
        else:
            screen.blit(rejouer,(275,500))
            for event in pg.event.get():
                quit()
                menu_back()            
    
    pg.display.update()