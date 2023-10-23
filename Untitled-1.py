import turtle as t
import math
import random as rng

def drawsquare(a): #a = distance entre le centre du cercle et ses cotés
    t.setheading(0)
    t.up()
    t.forward(a)
    t.right(90)          
    t.down()
    for i in range(4):   #dessine le carré, à noter que ses cotés sont égaux à 2*a (pour a=100, le coté sera égal à 200)
        t.forward(a)
        t.right(90)
        t.forward(a)
    t.up()        #à noter que la fonction drawsquare finit sur turtle qui n'est plus en position d'écrire

def drawcircle(a): #a = taille du plateau
    t.up()
    t.width(a/25)
    t.color('green')
    t.setheading(90)
    t.back(0.9*a/2)
    t.down()
    t.setheading(0)
    t.circle(0.9*a/2)
    t.color('black')
    t.width(1)
    t.up()

def drawcross(a): #a = taille du plateau
    t.up()
    t.color('red')
    t.width(a/25)
    t.setheading(0)
    t.back(0.9*a/2)
    t.right(90)
    t.forward(0.9*a/2)
    t.setheading(45)
    t.down()
    t.forward(0.9*((2*a)/1.41))
    t.up()
    t.setheading(0)
    t.back(0.9*a)
    t.right(45)
    t.down()
    t.forward(0.9*((2*a)/1.41))
    t.color('black')
    t.width(1)
    t.up()

def draw(a,b):
    if a == "Cercle":
        drawcircle(b)
    elif a == "Croix":
        drawcross(b)

def drawboard(a):          # a = taille du plateau, a définit la taille des cotés des carrés de la fonction drawsquare et en dessine 9 pour faire le plateau
    a = int(math.ceil(math.sqrt(a*a))) #prévu pour empêcher les erreurs en cas de float ou de nombre négatifs 
    j = 0
    for h in range(-a,a+1,a):
        for i in range(-a,a+1,a):
            t.goto(i,h)
            t.write(j, move=False, align='center', font=('Arial', int(math.ceil(a/15)), 'normal'))
            j+=1
            drawsquare(a/2)         # taille idéale:200

def exportxy(a): # a= taille du plateau, cette fonction va enregistrer 9 coordonnées.
    a = int(math.ceil(math.sqrt(a*a)))
    b = []                           # liste de coordonnées
    for h in range(-a,a+1,a):        # 6 , 7 , 8
        for i in range(-a,a+1,a):    # 3,  4,  5
            b.append([i,h])          # 0,  1,  2  |position des coordonnées relatives au plateau de jeu
    return b

def sum(a):
    b = 0
    for i in a:
        if i != 0:
            b+=1
    return b

def checkvictory(a):
    if a[6] + a[7] + a[8] == 3:
        x = [6,8]
        return x
    elif a[3] + a[4] + a[5] == 3:
        x = [3,5]
        return x
    elif a[0] + a[1] + a[2] == 3:
        x = [0,2]
        return x
    elif a[0] + a[3] + a[6] == 3:
        x = [0,6]
        return x
    elif a[1] + a[4] + a[7] == 3:
        x = [1,7]
        return x
    elif a[2] + a[5] + a[8] == 3:
        x = [2,8]
        return x
    elif a[2] + a[4] + a[6] == 3:
        x = [2,6]
        return x
    elif a[0] + a[4] + a[8] == 3:
        x = [0,8]
        return x
    else:
        return False

t.speed(0)
t.up()

a = 200              # a = taille du plateau
b = exportxy(a)     # b = coordonnées du plateau
c =[0,0,0 ,0,0,0 ,0,0,0]



e = rng.randrange(0,8,1)
ask = True
askrng = True
board = False
repeat = True
while repeat == True:
    type = t.textinput("Joueur 1:", "Entrez 'Cercle' ou 'Croix':")
    if type == "Croix" or type == "Cercle":
        repeat = False
    else:
        type = t.textinput("Joueur 1:", "Entrez 'Cercle' ou 'Croix':")
repeat = True
while repeat == True:
    jr = t.numinput("1 ou 2 Joueurs ?", "Entrez '1' ou '2':")
    if jr == 1 or jr == 2:
        repeat = False
    else:
        jr = t.numinput("1 ou 2 Joueurs ?", "Entrez '1' ou '2':")

repeat = True

while repeat == True:
    if jr == 1 :
        start = t.numinput("Qui commence?", "Joueur:1, Ordinateur:2")
        if start == 1 or start == 2:
            repeat = False
        else:
            start = t.numinput("Qui commence?", "Joueur:1, Ordinateur:2")
    else: 
        start = t.numinput("Qui commence?", "Joueur1:1, Joueur2:2")
        if start == 1 or start == 2:
            repeat = False
        else:
            start = t.numinput("Qui commence?", "Joueur1:1, Joueur2:2")


if type == "Croix":
    invtype = "Cercle"
elif type == "Cercle":
    invtype = "Croix"
drawboard(a)

coups1 = [0,0,0 ,0,0,0 ,0,0,0 , type]
coups2 = [0,0,0 ,0,0,0 ,0,0,0 , invtype]
check = 0
while board != True:
    retry=True; retrybot=True  
    while retry == True and start < 2:
        boardstatus = sum(c)
        if jr == 1:
            if boardstatus != 9:
                d=int(t.numinput("Choisissez votre coups.","Écrivez un chiffre compris entre 0 et 8:"))
            else:
                board = True
                retry = False
                retrybot=False
                winner = False
        else:
            if boardstatus != 9:
                d=int(t.numinput("J1 : Choisissez votre coups.","Écrivez un chiffre compris entre 0 et 8:"))
            else:
                board = True
                retry = False
                retrybot=False
                winner = False
        try:
            c[d]
        except:
            d=4
        if c[d] == 0:
            t.goto(b[d])
            c[d] = 1
            coups1[d] = 1
            draw(type,a)  
            retry=False
        else:
            if boardstatus != 9:
                retrybot=True
            else:
                board=True
                retry=False
        if checkvictory(coups1) != False:
                board = True
                retry = False
                retrybot= False
                winner = checkvictory(coups1)
                winner.append(type)
                winner.append("Joueur 1")

    

    while retrybot == True:
        boardstatus = sum(c)
        if jr == 1:
            boardstatus = sum(c)
            if boardstatus !=9:
                g=int(rng.randrange(0,8,1))
            else:
                board = True
                retry = False
                retrybot=False
                winner = False

        else:
            if boardstatus != 9:
                g=int(t.numinput("J2 : Choisissez votre coups.","Écrivez un chiffre compris entre 0 et 8:"))
            else:
                board = True
                retry = False
                retrybot=False
                winner = False
        
        if c[g] == 0:
            t.goto(b[g])
            c[g] = 1
            coups2[g] = 1
            draw(invtype,a) 
            retrybot=False
        else:
            if boardstatus != 9:
                retrybot=True
            else:
                board=True
                retrybot=False
        if checkvictory(coups2) != False:
                board = True
                retry = False
                retrybot=False
                winner = checkvictory(coups2)
                winner.append(invtype)
                winner.append("Joueur 2")
    start=1
    boardstatus = sum(c)
try:
    t.goto(b[winner[0]])
    t.down()
    t.width(5)
    t.goto(b[winner[1]])
    t.up()
    t.width()
    t.goto(0,0)
    if jr == 1:
        t.write(str(winner[2]) + " gagne !", move=False, align='center', font=('Arial', int(math.ceil(a/5)), 'normal'))
    else:
        t.write(str(winner[2]) + " (" + str(winner[3]) + ") gagne !", move=False, align='center', font=('Arial', int(math.ceil(a/5)), 'normal'))
except:
    t.goto(0,0)
    t.write("Égalité!", move=False, align='center', font=('Arial', int(math.ceil(a/5)), 'normal'))

t.mainloop()
