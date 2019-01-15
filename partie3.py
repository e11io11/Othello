from partie2 import *
from os import system
import os
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
    #Verifie si s=M ou si s correspond aux coordonées d'une case valide.
    #ord(s[0])-97 = i et int(s[1])-1)) = j
    if s == "M" or (len(s) == 2 and case_valide(partie["plateau"], ord(s[0])-97, int(s[1])-1) and mouvement_valide(partie["plateau"], ord(s[0])-97, int(s[1])-1, partie["joueur"])):
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
        print("\nAu tour du joueur", partie["joueur"])
        #le joueur saisi une action.
        s = input()
        #Verifie si l'input correspond a M ou aux coordonées un mouvement valide.
        while not saisie_valide(partie, s):
            print("Saisie invalide, réesayez:")
            s = input()
        if s != "M":
            #Si c'est un mouvement, il est effectué et True est renvoyé.
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
    #Teste si la saisie est correcte
    #Si il n'y a aucune partie en cours on ne peut pas sauvegarder(3) ni reprendre de partie(4). Il ne paut donc faire que 0,1 et 2.
    if partie == None:
        while s != "0" and s != "1" and s != "2":
            if s == "3" or s == "4":
                print("Vous n'avez aucune partie en cours, veuillez choisir une autre action:")
            else:
                print("Saisie invalide, réesayez:")
            s = input()
    #Si il y a une partie en cours il peut faire toutes les actions de 0 à 4.
    else:
        while s != "0" and s != "1" and s != "2" and s != "3" and s != "4":
            print("Saisie invalide, réesayez:")
            s = input()
    #Renvoie l'action saisie.
    return s




"""
Permet de jouer à la partie en cours (passée en paramètre).
Retourne True si la partie est terminée, False sinon.
"""
def jouer(partie):
    #Tant que la partie n'est pas terminée.
    while not fin_de_partie(partie["plateau"]):
        if tour_jeu(partie):
            #Si le joueur effectue un tour, on passe au joueur suivant.
            partie["joueur"] = pion_adverse(partie["joueur"])
        else:
            #Renvoie False si un joueur souhaite retourner au menu.
            return False
    #Si la partie est terminée, efface le terminal puis affiche le gagnant.
    #system('clear')   #LINUX
    system('cls')      #WINDOWS
    winner = gagnant(partie["plateau"])
    afficher_plateau(partie["plateau"])
    print("")
    print(70*"*"+"\n")
    print("La partie est terminée !\n")
    if winner == 0:
        print("Il y a ex æquo.")
    else:
        print("Le joueur "+str(winner)+" à gagné.")
    print("\n"+70*"*")
    #Et enfin renvoie True.
    return True




"""
Fait saisir un nombre parmi 4,6 ou 8 (saisie contrôlée).
"""
def saisir_taille_plateau():
    print("Veuillez saisir une taille de plateau (4, 6 ou 8).")
    s = input()
    #Verifie si la taille est valide.
    while s != "4" and s != "6" and s != "8":
        print("Taille invalide, réesayez:")
        s = input()
    #Renvoie la taille.
    return int(s)




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
        #Charge la partie si elle existe.
        with open("sauvegarde_partie.json", "r") as sauvegarde:
            return json.load(sauvegarde)
    else:
        #Sinon crée une nouvelle partie.
        print("Il n'y a pas de partie sauvegardée")
        return creer_partie(saisir_taille_plateau())




"""
Fonction permettant de jouer à Othello. On peut enchaîner, sauvegarder, charger et
recommencer des parties d'Othello.
"""
def othello():
    partie = None
    #Le joueur saisie une action.
    action = saisir_action(partie)
    #Tant que l'action n'est pas "terminer le jeu"(0):
    while action != "0":
        #Effectue les actions correspondantes.
        if action == "1":
            #Crée une nouvelle partie.
            partie = creer_partie(saisir_taille_plateau())
            jouer(partie)
        elif action == "2":
            #Charge une partie.
            partie = charger_partie()
            jouer(partie)
        elif action == "3":
            #Sauvegarde la partie.
            sauvegarder_partie(partie)
        else:
            #Reprend la partie.
            jouer(partie)
        #Une fois l'action effectuée, le joueur en resaisie une autre.
        action = saisir_action(partie)
    #Efface le terminal si le joueur decide d'arreter le jeu.
    #system('clear')   #LINUX
    system('cls')      #WINDOWS
