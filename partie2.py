from partie1 import *

"""
Retourne l'entier correspondant à l'adversaire :
- retourne 2 si joueur vaut 1,
- retourne 1 si joueur vaut 2.
Lève une erreur si joueur est différent de 1 et 2.
"""
def pion_adverse(joueur):

    #Lève une erreur si joueur est différent de 1 et 2.
    assert joueur == 1 or joueur == 2, "Joueur invalide"

    #Retourne 2 si joueur vaut 1
    if joueur == 1 :
        return 2
    #Retourne 1 si joueur vaut 2.
    else:
        return 1



"""
Retourne True si le joueur peut retourner un pion adverse
dans la direction (vertical,horizontal) en posant un pion dans la case (i,j),
False sinon.
"""
def prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
    #Si la case adjacente dans la direction (vertical,horizontal) possède un pion adverse:
    if case_valide(plateau, i+vertical, j+horizontal) and get_case(plateau, i+vertical, j+horizontal) == pion_adverse(joueur):
        k = i + 2*vertical
        l = j + 2*horizontal
        while case_valide(plateau, k, l):
            #Renvoie True si il y a un pion allié à l'autre bout.
            if get_case(plateau, k, l) == joueur:
                return True
            #False si il n'y en a pas.
            elif get_case(plateau, k, l) == 0:
                return False
            k += vertical
            l += horizontal
    #Renvoie False sinon.
    return False



"""
Retourne True si le joueur peut poser un pion à la case (i,j), False sinon.
"""
def mouvement_valide(plateau, i, j, joueur):
    #Si la case est vide:
    if get_case(plateau, i, j) == 0:
        #Renvoie True si l'une des direction est valide.
        if prise_possible_direction(plateau, i, j, -1, -1, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, -1, 0, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, -1, 1, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, 0, -1, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, 0, 1, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, 1, -1, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, 1, 0, joueur):
            return True
        elif prise_possible_direction(plateau, i, j, 1, 1, joueur):
            return True
    #Renvoie False sinon.
    return False



"""
Joue le pion du joueur à la case (i,j) si c'est possible.
"""
def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
    #Si on la prise est possible dans cette direction:
    if prise_possible_direction(plateau, i, j, vertical, horizontal, joueur):
        k = i + vertical
        l = j + horizontal
        #Tous les pions enemis entre les deux pions alliés sont mangés.
        while get_case(plateau, k, l) == pion_adverse(joueur):
            set_case(plateau, k, l, joueur)
            k += vertical
            l += horizontal



"""
Ajoute le pion du joueur à la case (i,j) et met à jour le plateau.
"""
def mouvement(plateau, i, j, joueur):
    #Si le mouvement est valide:
    if mouvement_valide(plateau, i, j, joueur):
        #Met un pion alliés sur la case (i,j).
        set_case(plateau, i, j, joueur)
        #Mange les pions enemis dans toutes les directions où c'est possible.
        mouvement_direction(plateau, i, j, -1, -1, joueur)
        mouvement_direction(plateau, i, j, -1, 0, joueur)
        mouvement_direction(plateau, i, j, -1, 1, joueur)
        mouvement_direction(plateau, i, j, 0, -1, joueur)
        mouvement_direction(plateau, i, j, 0, 1, joueur)
        mouvement_direction(plateau, i, j, 1, -1, joueur)
        mouvement_direction(plateau, i, j, 1, 0, joueur)
        mouvement_direction(plateau, i, j, 1, 1, joueur)


"""
Retourne True s'il existe une case sur laquelle le joueur peut jouer, False sinon.
"""
def joueur_peut_jouer(plateau, joueur):
    k = 0
    #Teste chaque case du tableau pour voir si il y a un mouvement valide possible.
    while k < plateau["n"]**2:
        if mouvement_valide(plateau, k//plateau["n"], k%plateau["n"], joueur):
            #Renvoie True si un mouvement valide à été trouvé
            return True
        k+=1
    #False sinon
    return False




"""
Retourne True si la partie est finie, 0 sinon.
"""
def fin_de_partie(plateau):
    #Renvoie True si les deux joueurs ne peuvent plus jouer.
    if not joueur_peut_jouer(plateau, 2) and not joueur_peut_jouer(plateau, 2):
        return True
    #0 sinon.
    else:
        return 0



"""
Retourne :
- 2 si le joueur 2 a plus de pions que le joueur 1,
- 1 si le joueur 1 a plus de pions que le joueur 2,
- 0 si égalité.
"""
def gagnant(plateau):
    joueur1 = 0
    joueur2 = 0
    i = 0
    #Calcule le nombre de pions de chaques joueurs
    while i < len(plateau["cases"]):
        if plateau["cases"][i] == 1:
            joueur1 += 1
        elif plateau["cases"][i] == 2:
            joueur2 += 1
        i+=1
    #Renvoie le gagnant.
    if joueur1 > joueur2:
        return 1
    elif joueur2 > joueur1:
        return 2
    else:
        return 0
