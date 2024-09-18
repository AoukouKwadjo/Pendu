from tkinter import *
from Donnee.recup import *

class Interface (Frame):
    
    def __init__(self,fenetre,**args):
        
        
        Frame.__init__(self,width=500,height=200,**args)
        self.pack(fill="both")
        
        self.pendu=mot_pendu()
        self.choice=''
        self.score=self.coups=10
        self.jeu=StringVar()

        self.aide="*******************************Hohayo Sekai**********************************\n\n"
        self.aide+=" Bienvenue au jeu du pendu !\n"
        self.aide+="Les regles sont simples: vous devez deviner le mot mystere \na chaque iteration nous devoilons les bonne lettre de que vous taper\na chaque iterration vous perdez un point, vous avez {} point en tout.\n".format(self.coups)
    
        desc_frame=Frame(self,borderwidth=0)
        resultat_frame=Frame(self,bd=2,bg='black')
        joueur_frame=Frame(self,bd=5,bg='gray')
        score_frame=Frame(resultat_frame,bd=5)


        desc_lbl = Label(desc_frame,text=self.aide)
        score_lbl = Label(score_frame,text='score: '+str(self.score))
        resultat_lbl = Label(resultat_frame,text=self.choice)


        valider=Button(joueur_frame,text="Tenter",bg='green',fg='white',command=valider)

        jeu= Entry(joueur_frame,textvariable=self.jeu)

        desc_frame.pack(side='top',ipadx=20,padx=20)
        resultat_frame.pack(pady=20)
        joueur_frame.pack(fill='y',pady=100,ipadx=20)
        resultat_lbl.pack(fill='x',ipady=20)
        score_lbl.pack(fill='both',side='left')
        score_frame.pack(fill='x',ipadx=200)
        desc_lbl.pack(fill='x')
        jeu.pack(side='left')
        valider.pack(side="right")
        
        self.button_quitter=Button(self,text="quitter",command=quit,fg="red")
        self.button_quitter.pack(side="right")
        
    def valider(self):
        jeu=self.jeu.get()
        pendu=self.pendu
        verif=verif_motPendu(pendu,jeu)
        if verif!=pendu:
            self.coups-=1
        
if __name__=='__main__':
    fenetre=Tk()
    interface=Interface(fenetre)
    
    interface.mainloop()
    interface.destroy()
