import numpy as np
from random import randint
from tkinter import *
import runpy

COL = 7
LIN = 6
j = randint(1,2)
cpt = 0
col = COL-1
lin = LIN-1
cptl = lin
couleur = ['#10DA9F','#EE2D5F']


tab = [[0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0]]



#placement du pion
        
def pion(x, y, cptl, c):
    r=40
    x0=x+c*100-100+2
    y0=y+cptl*100
    canvas.create_oval(x0-r, y0-r, x0+r, y0+r, fill = couleur[j-1])
    canvas.create_image(w/2, h/2, image=image)


#fin de partie

def reset():
    end.destroy()
    f.destroy()
    runpy.run_path(path_name='Puissance_4.py')
def accueil():
    end.destroy()
    f.destroy()
    runpy.run_path(path_name='accueil.py')


def fin():
    end.deiconify()



#vérifications

def verif(tab, c, COL, LIN, col, lin, cptl, cpt, j):
    
    #verification horizontale

    cpt = 0
    for i in range(COL):
        if tab[cptl][i] == j:
            cpt += 1
            if cpt > 3:
                return True
            print(cpt)
        else:
            cpt = 0


    #verification verticale

    cpt = 0
    for i in range(LIN):
        if tab[LIN-1-i][c-1] == j:
            cpt += 1
            if cpt > 3:
                return True
        else:
            cpt = 0


    #verification anti-diagonale /

    cpt = 0
    c1,l1 = c-1,cptl
    while c1 > 0 and l1 < lin:
        c1 -= 1
        l1 += 1
    while c1 < COL and l1 >= 0:
        if tab[l1][c1] == j:
            cpt += 1
            if cpt > 3:
                return True
        else:
            cpt = 0

        c1 += 1
        l1 -= 1


    #verification diagonale \

    cpt = 0
    c1,l1 = c-1,cptl
    while c1 >= 0 and l1 > 0:
        c1 -= 1
        l1 -= 1
    while c1 < COL and l1 < LIN:
        if tab[l1][c1] == j:
            cpt += 1
            if cpt > 3:
                return True
        else:
            cpt = 0

        c1 += 1
        l1 += 1

    return False


#boucle principale
        
def motion(event):
    global j
    x, y = event.x, event.y
    c = min(COL, x//100+1)
    if c > 0 and c <= COL:
        cptl = lin
        while tab[cptl][c-1] != 0 and cptl < 6:
            if cptl > 0:
                cptl -= 1
            else:
                return
        tab[cptl][c-1] = j
        print((np.array(tab)))
        print(x,y)
        print(verif(tab, c , COL, LIN, col, lin, cptl, cpt, j))
        pion(50, 50, cptl, c)
        if verif(tab, c , COL, LIN, col, lin, cptl, cpt, j):
            fin()
            print(f"le joueur {j} a gagné")
                
        #passage au joueur suivant
        j = j % 2 + 1


#fenetre

end = Tk()
end.withdraw()
end.title('Puissance 4')
end.geometry('400x400')
end.minsize(703, 603)
end.iconbitmap('cercle.ico')
img1 = PhotoImage(file='Fond.png')
bg = Label(end, image = img1)
bg.place(x = 0, y = 0)
lab = Label(end, text='Victoire du joueur '+str(j)+' !', fg='#526EAA', font=('arial' ,40), bg='white')
lab.pack(expand=YES)
P4_button = Button(end, text="Rejouer",font=('Arial',25),bg='white', fg='#526EAA',command = reset)
P4_button.pack(pady=25,fill=X)
P4_button = Button(end, text="Retourner à l'acceuil",font=('Arial',25),bg='white', fg='#526EAA',command = accueil)
P4_button.pack(pady=25,fill=X)
end.withdraw()

f = Tk()
f.title('Puissance 4')
f.geometry('1000x800')
f.minsize(703, 603)
f.iconbitmap('cercle.ico')

#image
w = 703
h = 603
image = PhotoImage(master=f, file='R.png')
canvas = Canvas(f, width=w, height=h)
canvas.create_image(w/2, h/2, image=image)
canvas.pack(expand=YES)

#bind
canvas.bind('<Button-1>', motion)

#affichage
f.mainloop()
