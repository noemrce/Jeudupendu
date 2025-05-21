print("welcome")

def supprimer_accents(mot): #Fonction pour retirer les accents
    mot_sans = "" #on va ici stocker le mot modifié
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
            mot_sans += remplacement[lettre] #on remplace la lettre accentué
        else:
            mot_sans += lettre
    return mot_sans #on retourne le même mot sans accents

def charger_mots_pendu():
    fichier = open("mots_pendu.txt", "r") #ouvrir le fichier
    mots = fichier.read().splitlines() #lit les lignes sans le \n lut par python
    fichier.close()

    mots_sans_accents = []

    for mot in mots:
        mots_sans_accents.append(supprimer_accents(mot))

    return mots_sans_accents

print(charger_mots_pendu())