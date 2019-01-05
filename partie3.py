from partie2 import *

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
    if s == "M" or len(s) == 2 and indice_valide(partie["plateau"], ord(s[0])-97) and indice_valide(partie["plateau"], int(s[1])):
        return True
    else:
        return False
