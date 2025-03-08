# importation des modules
from tkinter import *
import random
import runpy


def snake():
    window.destroy()
    runpy.run_path(path_name='TheSnake.py')


def puissance4():
    window.destroy()
    runpy.run_path(path_name="Puissance_4.py")
    

# creer une premiere fenetre
window =Tk()

# personaliser cette fenetre
window.title("Projet NSI")
window.geometry("1000x800")
window.minsize(480,360)
window.iconbitmap("python.ico")
window.config(background='#526EAA')

# creer la frame
frame= Frame(window,bg='#526EAA')


# ajouter texte
label_title = Label(window, text="Bienvenue sur l'application", font=('Arial',40),bg='#526EAA', fg='white') 
label_title.pack()

# second texte
label_subtitle = Label(frame, text="Choisi un jeu", font=('Arial',25),bg='#526EAA', fg='white') 
label_subtitle.pack(expand=YES)

# ajouter bouton

snake_button = Button(frame, text="Snake",font=('Arial',25),bg='white', fg='#526EAA',command = snake)
snake_button.pack(pady=25,fill=X)

# second bouton
P4_button = Button(frame, text="Puissance 4",font=('Arial',25),bg='white', fg='#526EAA',command = puissance4)
P4_button.pack(pady=25,fill=X)

#troisieme bouton
quitter_button = Button(frame, text="Quitter",font=('Arial',25),bg='white', fg='#526EAA',command = window.destroy)
quitter_button.pack(pady=25,fill=X)



frame.pack(expand=YES)


# afficher
window.mainloop()
