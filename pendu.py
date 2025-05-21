def supprimer_accents(mot): #Fonction pour retirer les accents
    mot_sans_accents_1 = "" #on va ici stocker le mot modifié
    remplacement = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a', 'ä': 'a',
        'î': 'i', 'ï': 'i',
        'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
      } #on simplifie chaque accent
    for lettre in mot: #on parcourt chaque lettre du mot choisi
        if lettre in remplacement:
            mot_sans_accents_1 += remplacement[lettre] #on remplace la lettre accentué
        else:
            mot_sans_accents_1 += lettre
    return mot_sans_accents_1 #on retourne le même mot sans accents

def charger_mots_pendu():
    fichier = open("mots_pendu.txt", "r") #ouvrir le fichier
    mots = fichier.read().splitlines() #lit les lignes sans le \n lut par python
    fichier.close()
    mots_sans_accents_2 = []
    for mot in mots:
        mots_sans_accents_2.append(supprimer_accents(mot))
    return mots_sans_accents_2

import random

def choisir_mot(mots):
    return random.choice(mots)

def jouer():
    mot_secret = choisir_mot(charger_mots_pendu()) # mot aleatoire sans accents
    lettres_trouvees = [] # bonnes lettres trouvees
    chances = 6 # nombres d'essais autorises

    while chances > 0:
        affichage = "" # va nous permettre d'afficher l'etat du mot

        for lettre in mot_secret:
            if lettre in lettres_trouvees:
                affichage += lettre  # Lettre devinee : on l'affiche
            else:
                affichage += "_" # lettre pas devinee : on affiche _
        print("Mot à deviner", affichage) #on a replacer la lettre trouvée au bonne endroit

        if "_" not in affichage:
            print ("félicitation, mot trouvé !")
            return

        choix_de_lettre = input("choisissez une lettre : ").lower() # entree du choix du joueur s'assurer d'avoir une minuscule

        if choix_de_lettre in lettres_trouvees:
            print("lettre déjà trouvée")

        if choix_de_lettre in mot_secret :
            print ("bonne réponse")
            lettres_trouvees.append(choix_de_lettre) #

        else:
            print ("mauvaise réponse")
            chances -= 1
            print(f"il reste {chances} chances.")

    print ("vous avez perdu. Le mot à deviner était :", mot_secret)

jouer()

input("Appuyez sur Entrée pour quitter")#Permet de run depuis mon folder