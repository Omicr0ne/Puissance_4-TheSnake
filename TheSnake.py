# importation des modules
from tkinter import *
import random
import runpy 

def acc():
    root.destroy()
    runpy.run_path(path_name="accueil.py")
    
    
# taille de la fenetre
Largeur = 600
Hauteur = 600

# le niveau
level = 1

# la variable pause pour permettre d'arreter la fonction principale
pause = 0


# ces quatres fonctions qui suivent (droite,gauche,bas,haut) empechent le bug de la diagonale
def droite (event):
    global d
    global xs
    deplaceDroite()
    if d==1:
        deplaceBas()
    elif d==3:
        deplaceHaut()
    elif d==4:
        deplaceGauche()
    else:
        deplaceDroite()
    d=4 
    
def gauche (event):
    global xs
    global d
    deplaceGauche()
    if d==1 :
        deplaceBas()
    elif d==3:
        deplaceHaut()
    elif d==2:
        deplaceDroite()
    else:
        deplaceGauche()
    d=2

def bas (event):
    global d
    global ys
    deplaceBas()
    if d==4 :
        deplaceGauche()
    elif d==2:
        deplaceDroite()
    elif d==3:
        deplaceHaut()
    else:
        deplaceBas()
    d=3
    
def haut (event):
    global d
    global ys
    deplaceHaut()
    if d==4 :
        deplaceGauche()
    elif d==2:
        deplaceDroite()
    elif d==1:
        deplaceBas()
    else:
        deplaceHaut()
    d=1

# fonction qui permet de déplacer le serpent vers le haut
def deplaceHaut ():
    global ys
    global xs
    try:
        eatPomme() 
        borderOutside()
        ys=ys-v
        canvas.coords(serpent,xs,ys,xs+20,ys+20)
        canvas.after(50,deplaceHaut)
    except:
        print("fin")

# fonction qui permet de déplacer le serpent vers la gauche
def deplaceGauche ():
    global ys
    global xs
    try:
        eatPomme()
        borderOutside()
        xs=xs-v
        canvas.coords(serpent,xs,ys,xs+20,ys+20)
        canvas.after(50,deplaceGauche)
    except:
        print("fin")
# le try et except m'aide à trouver les erreurs si il y en a

# fonction qui permet de déplacer le serpent vers la droite
def deplaceDroite ():
    global ys
    global xs
    try:
        eatPomme()
        borderOutside()
        xs=xs+v
        canvas.coords(serpent,xs,ys,xs+20,ys+20)
        canvas.after(50,deplaceDroite)
    except:
        print("fin")

# fonction qui permet de déplacer le serpent vers le bas
def deplaceBas ():
    global ys
    global xs
    try:
        eatPomme()
        borderOutside()
        ys=ys+v
        canvas.coords(serpent,xs,ys,xs+20,ys+20)
        canvas.after(50,deplaceBas)
    except:
        print("fin")   

# fonction qui récupère les coordonnées du serpent
def coordserpent():
    canvas.coords(serpent)

# fonction qui affiche le message pop up soit gagné ou perdu
def afficherMessage(title, msg, color):
    global pause
    pause = 1
    popup = Tk()
    popup.title(title)
    popup.geometry("200x100") # taille de la fentere pop up
    labelMsg = Label(popup, text =msg, fg=color, font=24)
    labelMsg.pack() # pour centrer le texte
    click_close = Button(popup, text="Quitter", fg=color, padx = 10, pady = 5, command=acc)
    # pour centrer le bouton
    click_close.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )
    popup.mainloop()
    

# fonction qui permet de quitter le jeu à la fin de la partie
def quitter(popup):
    print("fermer")
    popup.destroy()
    root.destroy()

# fonction qui fait disparaitre et aparaitre une nouvelle pomme d'une autre couleur
def eatPomme():
    global xp
    global yp
    global v
    global level
    if xs>=xp-5 and xs<=xp+5 and ys>=yp-5 and ys<=yp+5 and not pause:
        print("Pomme mangé")
        canvas.delete("apple") # pour supprimer la pomme
        level+=1
        if level >= 7:
            v=0
            afficherMessage("Terminé", "Vous avez gagné !", "GREEN")
        else :
            xp=random.randint(20,570)
            yp=random.randint(20,570)
            canvas.create_oval(xp,yp,xp+20,yp+20,width=0,fill=getColor(), tags="apple")
            v+=1

# fonction qui s'occupe des bordures
def borderOutside():
    global xs
    global ys
    if (xs>Largeur or xs<0 or ys>Hauteur or ys<0) and not pause:
        afficherMessage("Terminé", "Vous avez perdu !", "RED")

# fonction qui change la couleur de la nouvelle pomme en fonction de la variable level
def getColor():
    if level == 1:
        return "red"
    elif level == 2:
        return "yellow"    
    elif level == 3:
        return "orange"    
    elif level == 4:
        return "green"
    elif level == 5:
        return "purple"
    else:
        return "blue"
    

# initialisation de la fenetre
root = Tk()
root.title('The snake')
canvas = Canvas(root, width=Largeur, height=Hauteur, background="white")
canvas.pack(fill="both", expand=True)

#vitesse du serpent
v=5

# le serpent va à droite dès le lancement du jeu
d=4

# creation du serpent
xs, ys= 20,20
serpent = canvas.create_rectangle(xs,ys,xs+20,ys+20,width=0,fill="green")

# faire apparaître la pomme aleatoirement
xp=random.randint(20,570)
yp=random.randint(20,570)
canvas.create_oval(xp,yp,xp+20,yp+20,width=0,fill=getColor(), tags="apple")

# Ajout du cadre
canvas.create_rectangle(5,5,Largeur-5,Hauteur-5,fill="")

# choisir la direction du serpant
canvas.bind_all("<Up>",haut)
canvas.bind_all("<Down>",bas)
canvas.bind_all("<Left>",gauche)
canvas.bind_all("<Right>",droite)
canvas.bind_all("<Button-1>",coordserpent)

# conditions pour que le serpent avance vers la droite dès le début
if d==1 :
    deplaceHaut()
elif d==2:
    deplaceGauche ()
elif d==3:
    deplaceBas ()
else :
    deplaceDroite ()
    
print(ys,xs)
print(yp,xp)



