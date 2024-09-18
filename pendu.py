import os
from tkinter import *
from Donnee.recup import *
from Main_Interface import *
from interface.identify import *
from interface.fin import *
test=True
    
fenetre=Tk()
Main_Bar=Menu(fenetre)

Menu_fichier=Menu(Main_Bar,tearoff=0)
Main_Bar.add_cascade(label='fichier',menu=Menu_fichier,background='whitesmoke',activebackground='yellow')

Menu_afichage=Menu(Main_Bar,tearoff=0)
Main_Bar.add_cascade(label='afficher',menu=Menu_afichage,background='whitesmoke',activebackground='green')

Menu_fichier.add_command(label='Enregistrer')
Menu_fichier.add_command(label="Ouvrir")
Menu_fichier.add_command(label="Aide")
Menu_fichier.add_command(label="Quitter",command=quit)


fenetre.config(menu=Main_Bar)

identify=Identify(fenetre)

identify.mainloop()
user,scores=identifiant()
user=identify.__del__()
while test:

    pendus=mot_pendu()

    MainInterface=Interface(fenetre,pendus,user,scores)
    
    MainInterface.mainloop()
    scores=MainInterface.__del__()

    finProgramme=terminer(fenetre,score=scores,users=user,pendu=pendus)
    finProgramme.mainloop()
    test=finProgramme.__del__()
sauver_score((user,scores))
