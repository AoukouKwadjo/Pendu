import os
from Donnee.recup import *

def hohayo():
    os.system("clear")
    print ("*****************************Hohayo Sekai*********************************************",end="\n\n")
    print ("\t\t\t Bienvenue au jeu du pendu !\n")
    print("\tLes regles sont simples: vous devez deviner le mot mystere \n\
     a chaque iteration nous devoilons les bonne lettre de que vous taper\n.\
    a chaque iterration vous perdez un point, vous avez 10 point en tout.\n")
    
os.system("clear")
mot_mystere=mot_pendu()

hohayo()

user,scores=identifiant()
coups=scores

verif=saisis=""

while (verif!=mot_mystere)and coups>0:
    hohayo()
    print(verif,end="\nScore :{}\n".format(coups))
    
    saisis+=saisi()
    verif=verif_motPendu(mot_mystere,saisis)

    coups-=1

os.system("clear")
print ("**********************************Hohayo Sekai*********************************************",end="\n\n\n\t\t\t\t\t")

if coups<=0:
    print ("desoler u as perdus !\n")
else:
    print ("Bravos u as reussie")
    
print("\t\t\tle mot mystere etait {0} ton score est de: {1}".format(mot_mystere,coups),end="\n\n\n")
sauver_score((user,coups))