from partie2 import *
from os import system
import json

"""
Crée une partie. Une partie est un dictionnaire contenant :
- le joueur dont c'est le tour (clé joueur) initialisé à 1,
- le plateau (clé plateau).
"""
def creer_partie(n):
    return {"plateau":creer_plateau(n), "joueur":1}




"""
Retourne True si la chaîne s correspond à un mouvement valide pour le joueur courant,
et False sinon.
La chaîne s est valide si :
- s est égal à la lettre M ou
- s correspond à une case (de la forme a1 pour la case (0,0), ..., h8 pour la case (7,7))
où le joueur courant peut poser son pion.
"""
def saisie_valide(partie, s):
    if s == "M" or len(s) == 2 and indice_valide(partie["plateau"], ord(s[0])-97) and indice_valide(partie["plateau"], int(s[1])-1):
        return True
    else:
        return False




"""
 Effectue un tour de jeu :
- efface le terminal,
- affiche le plateau,
- si le joueur courant peut jouer, effectue la saisie d'un mouvement valide (saisie contrôlée),
- Effectue le mouvement sur le plateau de jeu,
- Retourne True si le joueur courant a joué ou False s'il souhaite accéder au menu principal.
"""
def tour_jeu(partie):
    #Efface le terminal puis affiche le plateau.
    #system('clear')   #LINUX
    system('cls')      #WINDOWS
    afficher_plateau(partie["plateau"])
    #Si le joueur courant peut jouer:
    if joueur_peut_jouer(partie["plateau"], partie["joueur"]):
        print("Au tour du joueur", partie["joueur"])
        #le joueur saisi une action.
        s = input()
        while not saisie_valide(partie, s) and not mouvement_valide(partie["plateau"], ord(s[0])-97, int(s[1])-1, partie["joueur"]):
            s = input()
        if s != "M":
            #Si c'est un mouvement, il est effectué.
            mouvement(partie["plateau"], ord(s[0])-97, int(s[1])-1, partie["joueur"])
            return True
            #Si c'est un retour au menu, renvoie False.
        return False




"""
Retourne le choix du joueur pour menu (saisie contrôlée):
- 0 pour terminer le jeu,
- 1 pour commencer une nouvelle partie,
- 2 pour charger une partie,
- 3 pour sauvegarder une partie (si une partie est en cours),
- 4 pour reprendre la partie (si une partie est en cours).
"""
def saisir_action(partie):
    print(70*"*"+"\n")
    print("Choisissez une action:\n")
    print("0 pour terminer le jeu")
    print("1 pour commencer une nouvelle partie")
    print("2 pour charger une partie")
    print("3 pour sauvegarder une partie (si une partie est en cours)")
    print("4 pour reprendre la partie (si une partie est en cours)")
    print("\n"+70*"*")
    #Le joueur saisi une action.
    s = input()
    if partie == None:
        while s != "0" and s != "1" and s != "2":
            if s == "3" or s == "4":
                print("Vous n'avez aucune partie en cours, veuillez choisir une autre action:")
            else:
                print("Saisie invalide, réesayez:")
            s = input()
    else:
        while s != "0" and s != "1" and s != "2" and s != "3" and s != "4":
            print("Saisie invalide, réesayez:")
            s = input()
    if s == "0":
        #Termine le jeu.
        #system('clear')   #LINUX
        system('cls')      #WINDOWS
        return False
    elif s == "1":
        #Crée une partie.
        return creer_partie(saisir_taille_plateau())
    elif s == "2":
        #Charge une partie.
        return charger_partie()
    elif s == "3":
        #Sauvegarde la partie.
        sauvegarder_partie(partie)
    else:
        return partie




"""
Permet de jouer à la partie en cours (passée en paramètre).
Retourne True si la partie est terminée, False sinon.
"""
def jouer(partie):
    #Tant que la partie n'est pas terminée.
    while not fin_de_partie(partie["plateau"]):
        #Les joueurs jouent chacun leur tour.
        if tour_jeu(partie):
            partie["joueur"] = pion_adverse(partie["joueur"])
        else:
            #Renvoie False si un joueur souhaite retourner au menu.
            return False
    print("La partie est terminée !\nLe joueur", gagnant(partie["plateau"]), "a gagné")
    #Return True lorsque la partie est terminée.
    return True




"""
Fait saisir un nombre parmi 4,6 ou 8 (saisie contrôlée).
"""
def saisir_taille_plateau():
    print("Veuillez saisir une taille de plateau (4, 6 ou 8).")
    s = int(input())
    while s != 4 and s != 6 and s != 8:
        print("Taille invalide, réesayez:")
        s = int(input())
    return s





"""
Sauvegarde la partie passée en paramètre au format json
dans le fichier sauvegarde_partie.json
"""
def sauvegarder_partie(partie):
    with open("sauvegarde_partie.json", "w") as sauvegarde:
        json.dump(partie, sauvegarde)




"""
Crée la partie à partir des données du fichier sauvegarde_partie.json
ou crée une nouvelle partie 4*4.
Retourne la partie créée.
"""
def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):
        with open("sauvegarde_partie.json", "w") as sauvegarde:
            return json.load(sauvegarde)
    else:
        print("Il n'y a pas de partie sauvegardée")
        return creer_partie(saisir_taille_plateau())




"""
Fonction permettant de jouer à Othello. On peut enchaîner, sauvegarder, charger et
recommencer des parties d'Othello.
"""
def othello():
    partie = creer_partie(4)
    action = saisir_action(partie)
    a = True
    while a:
        while action == None:
            action = saisir_action(partie)
        if action == False:
            return
        else:
            partie = action
            jouer(partie)
        action = saisir_action(partie)
