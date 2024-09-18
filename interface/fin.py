from tkinter import *
import os
import pickle

id='pendu_user'

class terminer (Frame):
    
    def __init__(self,fenetre,score,users,pendu,**args):
        
        Frame.__init__(self,fenetre,**args)
        self.pack(ipadx=100,pady=50)

        if score>0:
            color='green'
            bilan='Bravos tu as trouver ! le mot mystere est:  ({}) :)'.format(pendu)
        else:
            color='red'
            bilan=' desoler tu as perdus ! le mot mystere etait: ({}) :('.format(pendu)

        self.test=False
        user='joueur: '+users
        user+='\nScore: '+str(score)
        
        bilan_frame=Frame(self,bd=0)
        choix_frame=Frame(self,bd=0)

        bilan_lbl = Label(bilan_frame,text=bilan,fg=color)
        user_lbl = Label(bilan_frame,text=user)

        bilan_lbl.pack(pady=10)
        user_lbl.pack()
        bilan_frame.pack()
        choix_frame.pack(ipadx=100,pady=10)
        
        
        self.button_quitter=Button(choix_frame,text="quitter",command=self.quit,fg='white',bg="red")
        self.button_rejouer=Button(choix_frame,text="rejouer",command=self.valider,fg='white',bg="green")
        self.button_quitter.pack(side="right")
        self.button_rejouer.pack(side="left")
        
    def quitter(self):
        self.quit()
        self.destroy()
        
    def valider(self):
        self.test=True
        self.quitter()
        
    def __del__(self):
        return self.test
        
if __name__=='__main__':
    fenetre=Tk()
    interface=terminer(fenetre,score=1,users="raph",pendu='mot mystere')
    
    interface.mainloop()
    interface.destroy()