# -*- coding: utf-8 -*-

from tkinter import *
import time
import os

def afficher_l_image(fichier):
        global image
        image = PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + '/' + fichier)
        canvas.delete(ALL)
        canvas.create_image(0, 0, anchor=NW, image=image)
        tk.update()

tk = Tk()
image = ""
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
afficher_l_image('pendu(sans pendu).gif')
nombre_de_vies = 4
lettres_restantes = ""
mot_a_deviner = "_"
mot_a_afficher = ""
longueur_du_mot = ""

mot_a_deviner = input("Entrez le mot à faire deviner :")
lettres_restantes = mot_a_deviner
longueur_du_mot = len(mot_a_deviner)
for x in range(50):
        print()
        
print("Mot en ", longueur_du_mot, " lettres.")
while(nombre_de_vies != 0) and (lettres_restantes != ""):
        mot_a_afficher = mot_a_deviner
        for lettre in lettres_restantes:
                mot_a_afficher = mot_a_afficher.replace (lettre, " _ ")
        print(mot_a_afficher)
        réponse_joueur_2 = input("Entrez une lettre :")
        if réponse_joueur_2 in lettres_restantes:
                print("Trouvé")
                lettres_restantes = lettres_restantes.replace (réponse_joueur_2, "")
                if lettres_restantes == "":
                    print("Joueur 2 gagne !")
        else:
                print("Mauvaise réponse !")
                nombre_de_vies = nombre_de_vies - 1
                if nombre_de_vies == 0:
                        afficher_l_image('pendu.gif')
                elif nombre_de_vies == 3:
                        afficher_l_image('pendu(sans corps).gif')
                elif nombre_de_vies == 2:
                        afficher_l_image('pendu(sans bras).gif')
                elif nombre_de_vies == 1:
                        afficher_l_image('pendu(sans jambes).gif')
                
                print("Il vous reste", nombre_de_vies, "vies")
else:
        print("Fin de partie !")
        print("Le mot à deviner était :", mot_a_deviner)
        time.sleep(1.5)
