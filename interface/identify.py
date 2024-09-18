from tkinter import *
import os
import pickle

id='pendu_user'

class Identify (Frame):
    
    def __init__(self,fenetre,**args):
        
        Frame.__init__(self,fenetre,**args)
        self.pack(ipadx=150,pady=150)
        
        self.nom=StringVar()
        self.user=StringVar()
        self.passe=StringVar()

       
        principale_frame=Frame(self,bd=0)
        Nom_frame=Frame(principale_frame,bd=0)
        Passe_frame=Frame(principale_frame,bd=0)

        nom = Label(Nom_frame,text="Nom: ")
        passe = Label(Passe_frame,text="Mot de passe:")


        Nom=Entry(Nom_frame,textvariable=self.nom)
        Passe= Entry(Passe_frame,show="*",textvariable=self.passe,fg='green',exportselection=0)
        
        Nom_frame.pack(ipadx=15,pady=25)
        Passe_frame.pack(ipadx=10,pady=25)

        nom.pack()
        passe.pack()
        Nom.bind("<Return>",self.valider)
        Passe.bind("<Return>",self.valider)
        Nom.pack()
        Passe.pack()
        principale_frame.pack()
        
        
        self.button_quitter=Button(principale_frame,text="Valider",command=self.valider,fg="green")
        self.button_quitter.pack(side="bottom")
        
        self.identifi()
        
        
        
    def identifi(self):
        if os.path.exists(id):
            with open(id,"rb") as identifiants_file:
                unpickle=pickle.Unpickler(identifiants_file)
                noms,passes=unpickle.load()
                self.nom.set(noms)
                self.passe.set(passes)
                
    def valider(self,*args):
        if self.nom.get().strip()!='' and self.passe.get().strip()!='':
            self.quit()
            self.destroy()
        
                
    def __del__(self):
        
        with open(id,"wb") as identifiants_file:
            pickler=pickle.Pickler(identifiants_file)
            nom=self.nom.get()
            passe=self.passe.get()
            pickler.dump((nom,passe))
        return nom
        
            
        
if __name__=='__main__':
    fenetre=Tk()
    interface=Identify(fenetre)
    
    interface.mainloop()
    interface.destroy()
