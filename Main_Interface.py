from tkinter import *
from Donnee.recup import *

class Interface (Frame):
     
    def __init__(self,fenetre,pendu=mot_pendu(),user='----',coups=10):
        
        
        Frame.__init__(self,fenetre)
        self.pack(fill="both")
        
        self.pendu=pendu
        self.score=StringVar()
        self.coups=coups+1
        self.user=user
        self.saisis=''
        if coups<=1:
            self.coups= 11
        
        
        self.jeu=StringVar()

        self.aide="*******************************Hohayo Sekai**********************************\n\n"
        self.aide+=" Bienvenue au jeu du pendu !\n"
        self.aide+="Les regles sont simples: vous devez deviner le mot mystere \na chaque iteration nous devoilons les bonne lettre de que vous taper\na chaque iterration vous perdez un point, vous avez {} point en tout.\n".format(self.coups-1)
    
        desc_frame=Frame(self,borderwidth=0)
        resultat_frame=Frame(self,bd=2,bg='black')
        joueur_frame=Frame(self,bd=5)
        score_frame=Frame(resultat_frame,bd=5)
        user_frame=Frame(score_frame,bd=5)


        desc_lbl = Label(desc_frame,text=self.aide,pady=15)
        self.score = Label(score_frame,text='score: ')
        user = Label(user_frame,text='joueur : '+self.user)
        self.resultat = Label(resultat_frame)


        valider=Button(joueur_frame,text="Tenter",bg='green',fg='white',command=self.valider,relief=FLAT,bd=5)

        self.entre= Entry(joueur_frame,textvariable=self.jeu)
        self.entre.bind('<Return>',self.valider)
        desc_frame.pack(side='top',ipadx=20,padx=20)
        resultat_frame.pack(pady=20)
        joueur_frame.pack(fill='y',pady=100,ipadx=20)
        self.resultat.pack(fill='x',ipady=20)
        user_frame.pack(fill='x',side='top')
        user.pack(fill='x',side='left')
        self.score.pack(fill='x',side='left')
        score_frame.pack(fill='x',ipadx=200)
        desc_lbl.pack(fill='x')
        self.entre.pack(side='left')
        valider.pack(side="right")
        
        if len(self.jeu.get())==0:
            self.valider('')
        
        
    def valider(self,*args):
        
        pendu=self.pendu
        self.saisis+=self.jeu.get()
        self.jeu.set('')
        verif=verif_motPendu(pendu,self.saisis)
        
        verifs=verif.split('  ')
        verifs=''.join(verifs)
        
        if verifs!=pendu:
            self.coups-=1
            
        if verifs==pendu or self.coups<=0:
            self.destroy()
            self.quit()
        
        self.resultat['text']=verif.upper()
        self.score['text']="score: "+str(self.coups)
        
        
            
    def __del__(self):
        return self.coups
            
        
if __name__=='__main__':
    fenetre=Tk()
    interface=Interface(fenetre)
    
    interface.mainloop()
    interface.destroy()
