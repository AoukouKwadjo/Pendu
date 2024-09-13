from Donnee.donnee import *
import os
from random import choice
import pickle

def identifiant():
    if os.path.exists(identifiants):
        with open(identifiants,"rb") as identifiants_file:
            unpickle=pickle.Unpickler(identifiants_file)
            nom,scores=unpickle.load()
            if scores<=0:
                scores=nb_coups
            
            
    else:
        scores=nb_coups
        suite=True
        while suite:
            nom=input("veuillez saisir un nom: ")
            if len(nom)<=2:
                print("le nom est trop court au moin trois caractere !")
            else:
                suite=False
    user=(nom,scores)
    return user

def sauver_score(user):
    with open(identifiants,"wb") as identifiant_file:
        pickler=pickle.Pickler(identifiant_file)
        pickler.dump(user)

def mot_pendu():
    return choice(liste_mots)

def verif_motPendu(mdr,mr):
    mot=""
    for c in mdr:
        if c in mr:
            mot+=c
        else:
            mot+='*'
    return mot
                
def saisi():
    mot=input("mot :")
    if len(mot)>taille:
        print("le mot est trop long au moins {} caracteres\n".format(taille))
        saisi()
    return mot
